#!/bin/bash

LOG_PATH=tiko_install.log

echo "Logging to ${LOG_PATH}."

echo "Installing conda."
CONDA_URL="https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
if command -v curl &> /dev/null; then
  curl -L -O "$CONDA_URL" > ${LOG_PATH} 2> >(tee -a ${LOG_PATH} >&2)
else
  wget "$CONDA_URL" > ${LOG_PATH} 2> >(tee -a ${LOG_PATH} >&2)
fi
bash "Miniforge3-$(uname)-$(uname -m).sh" -b > ${LOG_PATH} 2> >(tee -a ${LOG_PATH} >&2)
miniforge3/condabin/conda config --set auto_activate_base false > ${LOG_PATH} 2> >(tee -a ${LOG_PATH} >&2)
miniforge3/condabin/conda init bash > ${LOG_PATH} 2> >(tee -a ${LOG_PATH} >&2)
source $HOME/.bashrc > ${LOG_PATH} 2> >(tee -a ${LOG_PATH} >&2)

echo "Creating the default Conda environment."
DEFAULT_CONDA_ENV_NAME="default_env"
conda create --name=${DEFAULT_CONDA_ENV_NAME} python > ${LOG_PATH} 2> >(tee -a ${LOG_PATH} >&2)
conda activate ${DEFAULT_CONDA_ENV_NAME} > ${LOG_PATH} 2> >(tee -a ${LOG_PATH} >&2)

echo "Installing tiko Python package."
pip install tiko > ${LOG_PATH} 2> >(tee -a ${LOG_PATH} >&2)

echo "Switching to the Python package portion of tiko."
python -m tiko.install
