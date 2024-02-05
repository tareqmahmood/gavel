import pandas as pd
import json

norm = pd.read_csv('norm_speed.csv')

tput = {
    'k80': {}
}

unique_jobs = set()

for i, row in norm.iterrows():
    model = [row['model1'], row['model2']]
    batch_size = [row['batch_size1'], row['batch_size2']]

    # has to be same gpu
    if row['gpu_num2'] != 0 and row['gpu_num1'] != row['gpu_num2']:
        continue

    num_gpu = row['gpu_num1']

    job1 = f"('{model[0]} (batch size {batch_size[0]})', {num_gpu})"

    if job1 not in tput['k80']:
        tput['k80'][job1] = {}

    unique_jobs.add(job1)

    if model[1] == 'Empty':
        job2 = 'null'
        tput['k80'][job1][job2] = row['speed1']
        
    else:
        job2 = f"('{model[1]} (batch size {batch_size[1]})', {num_gpu})"
        tput['k80'][job1][job2] = [row['speed1'], row['speed2']]

        if job2 not in tput['k80']:
            tput['k80'][job2] = {}
        unique_jobs.add(job2)

        tput['k80'][job2][job1] = [row['speed2'], row['speed1']]

# add missing values
for job1 in tput['k80']:
    num_gpu1 = int(job1.split(',')[-1][:-1])
    if "null" not in tput['k80'][job1]:
        tput['k80'][job1]['null'] = 1.0
    for job2 in unique_jobs:
        num_gpu2 = int(job2.split(',')[-1][:-1])
        if num_gpu1 == num_gpu2 and job2 not in tput['k80'][job1]:
            tput['k80'][job1][job2] = [0.0, 0.0]


tput['v100'] = tput['p100'] = tput['k80']
json.dump(tput, open('norm_to_throughput.json', 'w'), indent=4)


unique_jobs = list(unique_jobs)
unique_jobs.sort()
with open('jobs.txt', 'w') as file:
    for job in unique_jobs:
        file.write(job + '\n')
