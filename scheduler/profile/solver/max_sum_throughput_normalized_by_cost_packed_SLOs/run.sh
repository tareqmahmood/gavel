# exit when any command fails
set -e

# policy
policy="max_sum_throughput_normalized_by_cost_packed_SLOs"

# directory
cd ~/gavel/scheduler

# environment
source ~/miniconda3/etc/profile.d/conda.sh # Or path to where your conda is
conda activate gavel

# logs
mkdir -p profile/solver/$policy/logs

python  -u scripts/sweeps/run_sweep_static.py \
        -l profile/solver/$policy/logs \
        --per_instance_type_prices_dir profile/solver/$policy/prices \
        --assign_SLOs \
        -j 20 \
        -p $policy \
        --seeds 0 1 2 3 \
        -c 36:36:36 \
        -a 1 \
        -b 100 \
        -n 10