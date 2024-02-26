import os
import sys

import argparse
import csv
import math
import numpy as np
import random
from random import choice


def generate_interarrival_time(rng, lam):
    return -math.log(1.0 - rng.random()) * lam


def _generate_scale_factor_Philly(rng):
    # Sample the scale factor from the Philly distribution.
    scale_factor = 1
    r = rng.uniform(0, 1)
    if 0.7 < r <= 0.8:
        scale_factor = 2
    elif 0.8 < r <= 0.95:
        scale_factor = 4
    elif 0.95 < r:
        scale_factor = 8
    return scale_factor


def _generate_duration_Philly(rng):
    # Sample the job duration from the Philly distribution.
    if rng.random() >= 0.8:
        run_time = 60 * (10 ** rng.uniform(3, 4))
    else:
        run_time = 60 * (10 ** rng.uniform(1.5, 3))
    return run_time


def main(args):
    output_file = f"{args.dir}/poisson_trace_{args.num_jobs}+{args.lam}.csv"

    np.random.seed(args.seed)
    job_generator = random.Random()
    job_generator.seed(args.seed)

    interarrival_time_generator = random.Random()
    interarrival_time_generator.seed(args.seed + 1)

    duration_generator = random.Random()
    duration_generator.seed(args.seed + 2)

    scale_factor_generator = random.Random()
    scale_factor_generator.seed(args.seed + 3)

    single_gpu_model_list = ['resnet50', 'vgg19', 'DCGAN', 'PointNet']
    multi_gpu_model_list = ['Bert-Large', 'GPT2-Medium']
    all_model_list = single_gpu_model_list + multi_gpu_model_list
    batch_size_range = [32, 64, 128]

    fields = ['job_id', 'num_gpus', 'submit_time',
              'duration', 'model', 'batch_size']
    rows = []
    init_time = random.randint(10, 100)  # randomly set the init time
    prev_arrival_time = None
    for i in range(args.num_jobs):
        scale_factor = _generate_scale_factor_Philly(scale_factor_generator)
        if scale_factor == 1:
            model_name = choice(single_gpu_model_list)
        elif scale_factor > 1 and scale_factor <= 4:
            model_name = choice(all_model_list)
        elif scale_factor > 4:
            model_name = choice(multi_gpu_model_list)
        else:
            raise ValueError("scale factor is not considered now.")
        batch_size = choice(batch_size_range)
        run_time = int(_generate_duration_Philly(duration_generator))
        if prev_arrival_time is None:
            arrival_time = 0
        elif args.lam > 0:
            interarrival_time = generate_interarrival_time(
                interarrival_time_generator, args.lam)
            arrival_time = prev_arrival_time + int(interarrival_time * 60)
        else:
            raise ValueError("lam is not equal to zero")
        prev_arrival_time = arrival_time
        start_time = init_time + arrival_time
        # ('job_id', 'num_gpus', 'submit_time', 'duration', 'model', 'batch_size')
        row = [i + 1, scale_factor, start_time,
               run_time, model_name, batch_size]
        rows.append(row)

    with open(output_file, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the fields
        csvwriter.writerow(fields)
        # writing the data rows
        csvwriter.writerows(rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate synthetic trace')
    parser.add_argument('--num_jobs', type=int, default=900,
                        help='Number of jobs to generate')
    parser.add_argument('-l', '--lam', type=float, default=20.0,
                        help='Lambda for Poisson arrival rate. '
                             'lam=3 means submitting a job every 3 minutes')
    parser.add_argument('--seed', type=int, default=0,
                        help='Random seed')
    parser.add_argument('-d', '--dir', type=str, default="poisson_gavel_trace")

    args = parser.parse_args()
    if not os.path.exists(args.dir):
        os.mkdir(args.dir)
    num_jobs_list = [50, 220, 460, 900]
    lam_list = [3.0, 5.0, 10.0, 20.0]
    for num_jobs in num_jobs_list:
        for lam in lam_list:
            args.num_jobs = num_jobs
            args.lam = lam
            main(args)
