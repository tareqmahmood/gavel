# exit when any command fails
set -e

# directory
cd ~/Github/tareqmahmood/gavel/scheduler || cd ~/gavel/scheduler

# environment
source ~/miniconda3/etc/profile.d/conda.sh # Or path to where your conda is
conda activate gavel

# logs
mkdir -p check/logs


python  -u scripts/drivers/simulate_scheduler_with_trace.py \
        -t evaluate/poisson_gavel_trace/poisson_trace_220+20.0.csv \
        --throughputs_file norm_speed/norm_to_throughput.json \
        -p max_min_fairness \
        --seed 0 \
        -c 64:0:0 