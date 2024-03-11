# exit when any command fails
set -e

# directory
cd ~/Github/tareqmahmood/gavel/scheduler || cd ~/gavel/scheduler

# environment
source ~/miniconda3/etc/profile.d/conda.sh # Or path to where your conda is
conda activate gavel

# trace
trace="poisson_trace_220+5.0"

# logs
mkdir -p check/logs

# policy
policy="fifo"

python  -u scripts/drivers/simulate_scheduler_with_trace.py \
        -t "evaluate/poisson_gavel_trace/$trace.csv" \
        --throughputs_file norm_speed/norm_to_throughput.json \
        -p $policy \
        --seed 0 \
        -c 64:0:0 &> "check/logs/$policy.txt"