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
    num_gpu = [row['gpu_num1'], row['gpu_num2']]

    job0 = f"('{model[0]} (batch size {batch_size[0]})', {num_gpu[0]})"

    if job0 not in tput['k80']:
        tput['k80'][job0] = {}

    unique_jobs.add(job0)

    if model[1] == 'Empty':
        job1 = 'null'
        tput['k80'][job0][job1] = row['speed1']
        
    else:
        job1 = f"('{model[1]} (batch size {batch_size[1]})', {num_gpu[1]})"
        tput['k80'][job0][job1] = [row['speed1'], row['speed2']]

        if job1 not in tput['k80']:
            tput['k80'][job1] = {}
        unique_jobs.add(job1)

        tput['k80'][job1][job0] = [row['speed2'], row['speed1']]

tput['v100'] = tput['p100'] = tput['k80']
json.dump(tput, open('norm_to_throughput.json', 'w'), indent=4)


unique_jobs = list(unique_jobs)
unique_jobs.sort()
with open('jobs.txt', 'w') as file:
    for job in unique_jobs:
        file.write(job + '\n')
