import pandas as pd
import json

norm = pd.read_csv('norm_speed.csv')

tput = {
    'k80': {}
}

large_model_list = ['Bert-Base', 'Bert-Large', 'GPT2', 'GPT2-Medium', 'GPT2-XL']
small_model_list = ['resnet50', 'vgg19', 'DCGAN', 'PointNet']

unique_jobs = set()

for i, row in norm.iterrows():
    model = [row['model1'], row['model2']]
    batch_size = [row['batch_size1'], row['batch_size2']]

    # model1 cannot be large
    assert model[1] not in large_model_list

    # ignore if model1 is empty
    if model[1] == 'Empty':
        continue

    # ignore if large model does not have DP24
    if model[0] in large_model_list and row['pipeline_strategy'] != 'DP24':
        continue

    # has to be same gpu
    if row['gpu_num2'] != 0 and row['gpu_num1'] != row['gpu_num2']:
        continue

    num_gpu = row['gpu_num1']

    if model[0] in large_model_list:
        batch_size[0] = "NA"

    job1 = f"('{model[0]} (batch size {batch_size[0]})', {num_gpu})"
    job2 = f"('{model[1]} (batch size {batch_size[1]})', {num_gpu})"
    unique_jobs.add(job1)
    unique_jobs.add(job2)

    if job1 not in tput['k80']:
        tput['k80'][job1] = {}
        tput['k80'][job1]['null'] = 1.0
    tput['k80'][job1][job2] = [row['speed1'], row['speed2']]

    if job2 not in tput['k80']:
        tput['k80'][job2] = {}
        tput['k80'][job2]['null'] = 1.0
    tput['k80'][job2][job1] = [row['speed2'], row['speed1']]

# add missing values
for job1 in unique_jobs:
    num_gpu1 = int(job1.split(',')[-1][:-1])
    for job2 in unique_jobs:
        num_gpu2 = int(job2.split(',')[-1][:-1])
        if num_gpu1 == num_gpu2 and job2 not in tput['k80'][job1]:
            tput['k80'][job1][job2] = [0.0, 0.0]


for model in small_model_list:
    for num_gpu in [1, 2, 4]:
        for batch_size in [32, 64, 128]:
            job1 = f"('{model} (batch size {batch_size})', {num_gpu})"
            if job1 not in tput['k80']:
                tput['k80'][job1] = {}
                tput['k80'][job1]['null'] = 1.0

for model in large_model_list:
    for num_gpu in [2, 4, 8]:
        job1 = f"('{model} (batch size NA)', {num_gpu})"
        if job1 not in tput['k80']:
            tput['k80'][job1] = {}
            tput['k80'][job1]['null'] = 1.0

tput['v100'] = tput['p100'] = tput['k80']
json.dump(tput, open('norm_to_throughput.json', 'w'), indent=4)


unique_jobs = list(unique_jobs)
unique_jobs.sort()
with open('jobs.txt', 'w') as file:
    for job in unique_jobs:
        file.write(job + '\n')
