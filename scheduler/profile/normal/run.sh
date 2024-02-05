# exit when any command fails
set -e

# policy
policy="max_min_fairness_packed"

# directory
cd ~/gavel/scheduler

# environment
source ~/miniconda3/etc/profile.d/conda.sh # Or path to where your conda is
conda activate gavel

# logs
mkdir -p profile/normal/logs

python  -u scripts/sweeps/run_sweep_static.py \
        -l profile/normal/logs \
        -p $policy \
        --generate-multi-gpu-jobs \
        --seeds 0 \
        -c 2:0:0 \
        -a 0 \
        -b 3 \
        -n 2