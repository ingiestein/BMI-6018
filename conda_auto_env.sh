#!/bin/zsh
# Based on https://github.com/vallops99/Conda-autoactivate-env

autoload -U add-zsh-hook

conda_chpwd() {

  if [[ -n "${CONDACONFIGDIR:-}" ]] && [[ $PWD != *"${CONDACONFIGDIR:-}"* ]]; then 
    conda deactivate 2>/dev/null
    unset CONDACONFIGDIR
  fi
    
  if [ -f "$PWD/.conda_config" ]; then 
    export CONDACONFIGDIR=$PWD
    local conda_env
    conda_env=$(< "$PWD/.conda_config")
    [[ -n "$conda_env" ]] && conda activate "$conda_env"

  fi 

}

if [[ -n "${CONDA_SHLVL:-}" ]]; then 
  add-zsh-hook chpwd conda_chpwd
  conda_chpwd
fi 