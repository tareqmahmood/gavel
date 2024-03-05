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


def resnet50(batch_size):
    model = 'resnet50 (batch size %d)' % (batch_size)
    command = 'python3 main.py -j 8 -a resnet50 -b %d' % (batch_size)
    command += ' %s/imagenet/'
    working_directory = 'image_classification/imagenet'
    num_steps_arg = '--num_minibatches'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True)


def vgg19(batch_size):
    model = 'vgg19 (batch size %d)' % (batch_size)
    command = 'python3 main.py -j 8 -a vgg19 -b %d' % (batch_size)
    command += ' %s/imagenet/'
    working_directory = 'image_classification/imagenet'
    num_steps_arg = '--num_minibatches'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True)


def pointnet(batch_size):
    model = 'PointNet (batch size %d)' % (batch_size)
    command = 'python3 main.py'
    working_directory = 'pointnet'
    num_steps_arg = '--num_minibatches'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True)


def dcgan(batch_size):
    model = 'DCGAN (batch size %d)' % (batch_size)
    command = 'python3 main.py'
    working_directory = 'dcgan'
    num_steps_arg = '--num_minibatches'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True)


def gpt2xl(batch_size):
    model = f'GPT2-XL (batch size {batch_size})'
    command = 'python3 main.py'
    working_directory = 'gpt'
    num_steps_arg = '--steps'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True)


def gpt2medium(batch_size):
    model = f'GPT2-Medium (batch size {batch_size})'
    command = 'python3 main.py'
    working_directory = 'gpt'
    num_steps_arg = '--steps'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True)


def gpt2(batch_size):
    model = f'GPT2 (batch size {batch_size})'
    command = 'python3 main.py'
    working_directory = 'gpt'
    num_steps_arg = '--steps'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True)


def bertbase(batch_size):
    model = f'Bert-Base (batch size {batch_size})'
    command = 'python3 main.py'
    working_directory = 'gpt'
    num_steps_arg = '--steps'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True)


def bertlarge(batch_size):
    model = f'Bert-Large (batch size {batch_size})'
    command = 'python3 main.py'
    working_directory = 'gpt'
    num_steps_arg = '--steps'
    return JobTemplate(model=model, command=command,
                       working_directory=working_directory,
                       num_steps_arg=num_steps_arg, distributed=True)


SmallJobTable = []
LargeJobTable = []
JobTable = []
JobScaleTable = {
    1: [],
    2: [],
    4: [],
    8: []
}

# large_model_list = ['Bert-Base', 'Bert-Large', 'GPT2', 'GPT2-Medium', 'GPT2-XL']
# small_model_list = ['resnet50', 'vgg19', 'DCGAN', 'PointNet']

for batch_size in [32]:
    SmallJobTable.append(resnet50(batch_size))
    for scale_factor in [1, 2, 4, 8]:
        JobScaleTable[scale_factor].append(resnet50(batch_size))

for batch_size in [32]:
    SmallJobTable.append(vgg19(batch_size))
    for scale_factor in [1, 2, 4, 8]:
        JobScaleTable[scale_factor].append(vgg19(batch_size))

for batch_size in [32]:
    SmallJobTable.append(pointnet(batch_size))
    for scale_factor in [1, 2, 4, 8]:
        JobScaleTable[scale_factor].append(pointnet(batch_size))

for batch_size in [128]:
    SmallJobTable.append(dcgan(batch_size))
    for scale_factor in [1, 2, 4, 8]:
        JobScaleTable[scale_factor].append(dcgan(batch_size))

# ignoring batch size of large models
# they are the same always

for batch_size in ["NA"]:
    LargeJobTable.append(gpt2(batch_size))
    for scale_factor in [2]:
        JobScaleTable[scale_factor].append(
            gpt2(batch_size))

for batch_size in ["NA"]:
    LargeJobTable.append(gpt2medium(batch_size))
    for scale_factor in [4]:
        JobScaleTable[scale_factor].append(
            gpt2medium(batch_size))

for batch_size in ["NA"]:
    LargeJobTable.append(gpt2xl(batch_size))
    for scale_factor in [8]:
        JobScaleTable[scale_factor].append(
            gpt2xl(batch_size))

for batch_size in ["NA"]:
    LargeJobTable.append(bertbase(batch_size))
    for scale_factor in [2]:
        JobScaleTable[scale_factor].append(
            bertbase(batch_size))

for batch_size in ["NA"]:
    LargeJobTable.append(bertlarge(batch_size))
    for scale_factor in [4]:
        JobScaleTable[scale_factor].append(
            bertlarge(batch_size))

JobTable = SmallJobTable + LargeJobTable
