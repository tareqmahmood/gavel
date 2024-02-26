# exit when any command fails
set -e

# directory
cd ~/Github/tareqmahmood/gavel/scheduler || cd ~/gavel/scheduler

# environment
source ~/miniconda3/etc/profile.d/conda.sh # Or path to where your conda is
conda activate gavel

# logs
mkdir -p check/logs

python  -u scripts/sweeps/run_sweep_continuous.py \
        -s 0 \
        -e 220 \
        -l check/logs \
        --throughputs-file norm_speed/norm_to_throughput.json \
        -p max_min_fairness \
        --seeds 0 \
        -m \
        -c 64:0:0 \
        -a 0.0 \
        -b 720 \
        -n 2