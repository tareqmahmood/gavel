# exit when any command fails
set -xe

# pre

sudo apt update
sudo apt install -y htop aria2
curl https://tareqmahmood.github.io/s/zellij.sh | bash



# git

git config --global user.name "Md. Tareq Mahmood"
git config --global user.email "tareq.py@gmail.com"


# miniconda

echo '[INFO] download miniconda'
mkdir -p ~/miniconda3
cd ~/miniconda3
aria2c -x 8 https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh 

echo '[INFO] install miniconda'
mv Miniconda3-latest-Linux-x86_64.sh miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh

echo '[INFO] setup miniconda'
~/miniconda3/bin/conda init bash



# gavel

source ~/.bashrc
source ~/miniconda3/etc/profile.d/conda.sh # Or path to where your conda is
conda activate base

echo '[INFO] Creating gavel'
conda create -n gavel python=3.8 -y

echo '[INFO] Activate gavel'
conda activate gavel

sudo apt-get -y install cmake g++ gcc libnuma-dev make numactl zlib1g-dev
cd ~/gavel
pip install -r scheduler/requirements.txt
cd scheduler
make
