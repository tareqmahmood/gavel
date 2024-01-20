# exit when any command fails
set -e

# directory
cd ~/gavel/scheduler

# environment
source ~/miniconda3/etc/profile.d/conda.sh # Or path to where your conda is
conda activate gavel

# logs
mkdir -p profile/solver/logs

# run
python  -u scripts/sweeps/run_sweep_continuous.py \
        -s 100 \
        -e 110 \
        -l profile/solver/logs \
        -j 20 \
        -p max_min_fairness \
        --seeds 0 \
        -c 36:36:36 \
        -a 0.0 \
        -b 1.0 \
        -n 2