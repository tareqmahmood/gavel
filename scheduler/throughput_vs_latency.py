import argparse
import json
import matplotlib.pyplot as plt
import numpy as np
import os

import job
from job_id_pair import JobIdPair
import policies
import scheduler

np.random.seed(42)

def get_policy(policy_name):
    if policy_name == "isolated":
        policy = policies.IsolatedPolicy()
    elif policy_name == "max_min_fairness":
        policy = policies.MaxMinFairnessPolicy()
    elif policy_name == "max_min_fairness_packed":
        policy = policies.MaxMinFairnessPolicyWithPacking()
    elif policy_name == "min_total_duration":
        policy = policies.MinTotalDurationPolicy()
    elif policy_name == "min_total_duration_packed":
        policy = policies.MinTotalDurationPolicyWithPacking()
    elif policy_name == "fifo":
        policy = policies.FIFOPolicy()
    else:
        raise Exception("Unknown policy!")
    return policy

def parse_trace(trace_file, throughputs_file):
    jobs = []
    arrival_times = []
    durations = []

    with open(throughputs_file, 'r') as f:
        throughputs = json.load(f)

    with open(trace_file, 'r') as f:
        for line in f:
            (job_type, command, num_steps_arg, total_steps,
             arrival_time, scale_factor) = line.split('\t')
            jobs.append(job.Job(job_id=None,
                                job_type=job_type,
                                command=command,
                                num_steps_arg=num_steps_arg,
                                total_steps=int(total_steps),
                                duration=None,
                                scale_factor=int(scale_factor)))
            arrival_times.append(int(arrival_time))
            v100_throughput = float(throughputs['k80'][job_type]['null'])
            durations.append(int(total_steps) / v100_throughput)
    return jobs, arrival_times, durations


def debug_packing_for_rounds_with_timelines():
    trace_file = 'traces/generated/msr/msr_debug.trace'
    throughputs_file = 'combined_throughputs.json'
    cluster_spec = {'v100': 25}
    x = {}
    colors = {}
    ranges = [(0, 10)]

    all_colors = np.random.rand(100)

    all_jobs, all_arrival_times, durations = \
            parse_trace(trace_file, throughputs_file)
    for (i, j) in ranges:
        jobs = all_jobs[i:j]
        arrival_times = all_arrival_times[i:j]
        results = {}
        for use_rounds in [True, False]:
            x[(i, j, use_rounds)] = {}
            policy = get_policy('max_min_fairness_packed')
            results[use_rounds] = {}
            sched = \
                scheduler.Scheduler(policy,
                                    schedule_in_rounds=use_rounds,
                                    throughputs_file=throughputs_file,
                                    emulate=True)
            sched.emulate_from_trace(cluster_spec, arrival_times, jobs,
                                     ideal=False)
            start_times, end_times = sched.get_job_start_and_end_times()
            x[(i, j, use_rounds)]['start'] = start_times
            x[(i, j, use_rounds)]['end'] = end_times
            colors[(i, j, use_rounds)] = all_colors[i:j]
            assert(len(start_times) == len(all_colors[i:j]))
            assert(len(end_times) == len(start_times))


    labels = []
    for k, (i, j) in enumerate(ranges):
        for m, use_rounds in enumerate([True, False]):
            y = [k*2+m for _ in range(len(x[(i, j, use_rounds)]['start']))]
            if use_rounds:
                label = '%d:%d w/ rounds' % (i, j)
            else:
                label = '%d:%d w/out rounds' % (i, j)
            labels.append(label)
            plt.scatter(x[(i, j, use_rounds)]['start'], y,
                        c=colors[(i, j, use_rounds)], marker='o')
            plt.scatter(x[(i, j, use_rounds)]['end'], y,
                        c=colors[(i, j, use_rounds)], marker='^')
            for n, (x_coord, y_coord) in enumerate(zip(x[(i, j, use_rounds)]['start'], y)):
                plt.annotate(str(i+n),
                             (x_coord, y_coord),
                             textcoords='offset points',
                             xytext=(0,10),
                             ha='center')
            for n, (x_coord, y_coord) in enumerate(zip(x[(i, j, use_rounds)]['end'], y)):
                plt.annotate(str(i+n),
                             (x_coord, y_coord),
                             textcoords='offset points',
                             xytext=(0,10),
                             ha='center')
    plt.yticks(list(range(len(ranges) * 2)), labels, rotation=30)

    plt.tight_layout()
    plt.show()


def main():
    # TODO: convert to command line arguments
    schedule_in_rounds = False
    throughputs_file = 'combined_throughputs.json'
    num_v100s = 25
    policy_names = ['fifo']
    ratios = [
            {'v100': 1, 'p100': 0, 'k80': 0},
            #{'v100': 1, 'p100': 1, 'k80': 0},
            #{'v100': 1, 'p100': 1, 'k80': 1},
            #{'v100': 2, 'p100': 1, 'k80': 0},
        ]
    job_range = (0, 100)
    with open(throughputs_file, 'r') as f:
        throughputs = json.load(f)
    lams = [16384]
    for ratio in ratios:
        cluster_spec = {}
        total_gpu_fraction = sum([ratio[gpu_type] for gpu_type in ratio])
        for gpu_type in ratio:
            fraction = ratio[gpu_type] / total_gpu_fraction
            cluster_spec[gpu_type] = int(fraction * num_v100s)
        all_lams_str = ','.join([str(lam) for lam in lams])
        output_file = ('latency_vs_throughput_cluster_spec_'
                       '%d_%d_%d_lambda=%s_'
                       'jobs_to_complete_%d-%d.csv') % (cluster_spec['v100'],
                                                        cluster_spec['p100'],
                                                        cluster_spec['k80'],
                                                        all_lams_str,
                                                        job_range[0],
                                                        job_range[1])
        with open(output_file, 'w') as f:
            f.write('# v100,# p100,# k80,Rounds,Policy,Lambda,Utilization,'
                    'Average JCT\n')
            for use_rounds in [True]:
                for policy_name in policy_names:
                    for lam in lams:
                        # TODO: can this be moved to previous for loop?
                        policy = get_policy(policy_name)
                        sched = scheduler.Scheduler(
                                policy, schedule_in_rounds=use_rounds,
                                throughputs_file=throughputs_file,
                                emulate=True)
                        jobs_to_complete = set()
                        for i in range(job_range[0], job_range[1]):
                            jobs_to_complete.add(JobIdPair(i, None))
                        sched.emulate(cluster_spec,
                                      throughputs=throughputs,
                                      lam=lam,
                                      jobs_to_complete=jobs_to_complete)
                        utilization = sched.get_cluster_utilization()
                        average_jct = sched.get_average_jct(jobs_to_complete)
                        average_jct = sched.get_average_jct()
                        f.write('%d,%d,%d,%s,%s,%d,'
                                '%.3f,%.3f\n' % (cluster_spec['v100'],
                                                 cluster_spec['p100'],
                                                 cluster_spec['k80'],
                                                 str(use_rounds),
                                                 policy.name,
                                                 lam,
                                                 utilization,
                                                 average_jct))
                        f.flush()


if __name__=='__main__':
    #debug_packing_for_rounds_with_timelines()
    main()
