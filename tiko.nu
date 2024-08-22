match $(uname) {
    "Darwin" => {
        $env.PATH = ($env.PATH | split row (char esep) | prepend '/opt/homebrew/bin')
    }
    "Linux" => {
        $env.PATH = ($env.PATH | split row (char esep) | prepend $env.HOME + '/.homebrew/bin')
    }
}

match $(uname) {
    "Darwin" => {
        brew install miniforge
    }
    "Linux" => {
        let CONDA_URL = "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-" + $(uname) + "-" + $(uname -m) + ".sh"
        if $(which curl) != '' then
          {curl -L -O $CONDA_URL}
        else
          {wget $CONDA_URL}
        end
        bash "Miniforge3-" + $(uname) + "-" + $(uname -m) +".sh" -b -p "${HOME}/.miniforge3"
        bash "${HOME}/.miniforge3/condabin/conda config --set auto_activate_base false"
        bash "${HOME}/.miniforge3/condabin/conda init bash"
    }
}

conda config --set auto_activate_base false
let tiko_install_env_name = 'tiko_install_env'
conda create --name=$tiko_install_env_name python
conda activate tiko_install_env

brew install rustup

brew install helix

brew install zellij

brew install bottom

brew install dua-cli

conda deactivate
conda remove -n tiko_install_env --all
