from job_template import JobTemplate

# def resnet18(batch_size):
#     model = 'ResNet-18 (batch size %d)' % (batch_size)
#     command = 'python3 main.py --data_dir=%s/cifar10'
#     command += ' --batch_size %d' % (batch_size)
#     working_directory = 'image_classification/cifar10'
#     num_steps_arg = '--num_steps'
#     return JobTemplate(model=model, command=command,
#                        working_directory=working_directory,
#                        num_steps_arg=num_steps_arg, distributed=True)

# def resnet50(batch_size):
#     model = 'ResNet-50 (batch size %d)' % (batch_size)
#     command = 'python3 main.py -j 8 -a resnet50 -b %d' % (batch_size)
#     command += ' %s/imagenet/'
#     working_directory = 'image_classification/imagenet'
#     num_steps_arg = '--num_minibatches'
#     return JobTemplate(model=model, command=command,
#                        working_directory=working_directory,
#                        num_steps_arg=num_steps_arg, distributed=True)

# def transformer(batch_size):
#     model = 'Transformer (batch size %d)' % (batch_size)
#     command = 'python3 train.py -data %s/translation/multi30k.atok.low.pt'
#     command += ' -batch_size %d -proj_share_weight' % (batch_size)
#     working_directory = 'translation'
#     num_steps_arg = '-step'
#     return JobTemplate(model=model, command=command,
#                        working_directory=working_directory,
#                        num_steps_arg=num_steps_arg, distributed=True)

# def lm(batch_size):
#     model = 'LM (batch size %d)' % (batch_size)
#     command = 'python main.py --cuda --data %s/wikitext2'
#     command += ' --batch_size %d' % (batch_size)
#     working_directory = 'language_modeling'
#     num_steps_arg = '--steps'
#     return JobTemplate(model=model, command=command,
#                        working_directory=working_directory,
#                        num_steps_arg=num_steps_arg, distributed=True)

# def recommendation(batch_size):
#     model = 'Recommendation (batch size %d)' % (batch_size)
#     command = 'python3 train.py --data_dir %s/ml-20m/pro_sg/'
#     command += ' --batch_size %d' % (batch_size)
#     working_directory = 'recommendation'
#     num_steps_arg = '-n'
#     return JobTemplate(model=model, command=command,
#                        working_directory=working_directory,
#                        num_steps_arg=num_steps_arg)

# def a3c():
#     model = 'A3C'
#     command = ('python3 main.py --env PongDeterministic-v4 --workers 4 '
#                '--amsgrad True')
#     working_directory = 'rl'
#     num_steps_arg = '--max-steps'
#     return JobTemplate(model=model, command=command,
#                        working_directory=working_directory,
#                        num_steps_arg=num_steps_arg,
#                        needs_data_dir=False)

# def cyclegan():
#     model = 'CycleGAN'
#     working_directory = 'cyclegan'
#     command = ('python3 cyclegan.py --dataset_path %s/monet2photo'
#                ' --decay_epoch 0')
#     num_steps_arg = '--n_steps'
#     return JobTemplate(model=model, command=command,
#                        working_directory=working_directory,
#                        num_steps_arg=num_steps_arg)

# JobTable = []
# 
# for batch_size in [16, 32, 64, 128, 256]:
#     JobTable.append(resnet18(batch_size))
# for batch_size in [16, 32, 64, 128]:
#     JobTable.append(resnet50(batch_size))
# for batch_size in [16, 32, 64, 128, 256]:
#     JobTable.append(transformer(batch_size))
# for batch_size in [5, 10, 20, 40, 80]:
#     JobTable.append(lm(batch_size))
# for batch_size in [512, 1024, 2048, 4096, 8192]:
#     JobTable.append(recommendation(batch_size))
# JobTable.append(a3c())
# JobTable.append(cyclegan())

def resnet50(batch_size, scale_factor):
    model = 'resnet50 (batch size %d)' % (batch_size)
    command = 'python3 main.py -j 8 -a resnet50 -b %d' % (batch_size)
    command += ' %s/imagenet/'
    working_directory = 'image_classification/imagenet'
    num_steps_arg = '--num_minibatches'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True, scale_factor=scale_factor)

def vgg19(batch_size, scale_factor):
    model = 'vgg19 (batch size %d)' % (batch_size)
    command = 'python3 main.py -j 8 -a vgg19 -b %d' % (batch_size)
    command += ' %s/imagenet/'
    working_directory = 'image_classification/imagenet'
    num_steps_arg = '--num_minibatches'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True, scale_factor=scale_factor)

def pointnet(batch_size, scale_factor):
    model = 'PointNet (batch size %d)' % (batch_size)
    command = 'python3 main.py'
    working_directory = 'pointnet'
    num_steps_arg = '--num_minibatches'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True, scale_factor=scale_factor)

def dcgan(batch_size, scale_factor):
    model = 'DCGAN (batch size %d)' % (batch_size)
    command = 'python3 main.py'
    working_directory = 'dcgan'
    num_steps_arg = '--num_minibatches'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True, scale_factor=scale_factor)

def gpt2xl(batch_size, micro_batch_size, scale_factor):
    model = 'GPT2-XL (batch size %d/%d)' % (batch_size, micro_batch_size)
    command = 'python3 main.py'
    working_directory = 'gpt'
    num_steps_arg = '--steps'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True, scale_factor=scale_factor)


def gpt2medium(batch_size, micro_batch_size, scale_factor):
    model = 'GPT2-Medium (batch size %d/%d)' % (batch_size, micro_batch_size)
    command = 'python3 main.py'
    working_directory = 'gpt'
    num_steps_arg = '--steps'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True, scale_factor=scale_factor)

def gpt2(batch_size, micro_batch_size, scale_factor):
    model = 'GPT2 (batch size %d/%d)' % (batch_size, micro_batch_size)
    command = 'python3 main.py'
    working_directory = 'gpt'
    num_steps_arg = '--steps'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True, scale_factor=scale_factor)

def bertbase(batch_size, micro_batch_size, scale_factor):
    model = 'Bert-Base (batch size %d/%d)' % (batch_size, micro_batch_size)
    command = 'python3 main.py'
    working_directory = 'gpt'
    num_steps_arg = '--steps'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True, scale_factor=scale_factor)

def bertlarge(batch_size, micro_batch_size, scale_factor):
    model = 'Bert-Large (batch size %d/%d)' % (batch_size, micro_batch_size)
    command = 'python3 main.py'
    working_directory = 'gpt'
    num_steps_arg = '--steps'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True, scale_factor=scale_factor)

JobTable = []

for batch_size in [32]:
    for scale_factor in [2]:
        JobTable.append(resnet50(batch_size, scale_factor))

for batch_size in [32]:
    for scale_factor in [2]:
        JobTable.append(vgg19(batch_size, scale_factor))

for batch_size in [32]:
    for scale_factor in [2]:
        JobTable.append(pointnet(batch_size, scale_factor))

for batch_size in [128]:
    for scale_factor in [2]:
        JobTable.append(dcgan(batch_size, scale_factor))

# for batch_size in [256, 512]:
#     for micro_batch_size in [2, 4]:
#         for scale_factor in [8]:
#             JobTable.append(gpt2xl(batch_size, micro_batch_size, scale_factor))

# for batch_size in [256, 512]:
#     for micro_batch_size in [8, 32]:
#         for scale_factor in [4]:
#             JobTable.append(gpt2medium(batch_size, micro_batch_size, scale_factor))

for batch_size in [256, 512]:
    for micro_batch_size in [8, 16]:
        for scale_factor in [2]:
            JobTable.append(gpt2(batch_size, micro_batch_size, scale_factor))

for batch_size in [256]:
    for micro_batch_size in [16, 32]:
        for scale_factor in [2]:
            JobTable.append(bertbase(batch_size, micro_batch_size, scale_factor))

# for batch_size in [256]:
#     for micro_batch_size in [16, 64]:
#         for scale_factor in [4]:
#             JobTable.append(bertlarge(batch_size, micro_batch_size, scale_factor))
