# exit when any command fails
set -e

# directory
cd ~/Github/tareqmahmood/gavel/scheduler || cd ~/gavel/scheduler

# environment
source ~/miniconda3/etc/profile.d/conda.sh # Or path to where your conda is
conda activate gavel

# trace
trace="poisson_trace_900+5.0"
num_gpu=128

# policy
policy="max_min_fairness_packed"

# logs
folder="logs"
full_folder="check/$folder/$trace/$num_gpu"
mkdir -p "$full_folder"

python  -u scripts/drivers/simulate_scheduler_with_trace.py \
        -t "evaluate-fixed/poisson_gavel_trace/$trace.csv" \
        --throughputs_file norm_speed/norm_to_throughput.json \
        -p $policy \
        --seed 0 \
        -c $num_gpu:0:0 &> "$full_folder/$policy.txt"
