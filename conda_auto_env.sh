#!/bin/zsh
# Based on https://github.com/vallops99/Conda-autoactivate-env
autoload -Uz add-zsh-hook

# Store the project root that triggered activation
typeset -g CONDA_AUTO_ROOT=""

conda_chpwd() {
  local config_file="$PWD/.conda_config"
  local current_env

  # CASE 1: We're in a directory (or subdirectory) with .conda_config
  if [[ -f "$config_file" ]]; then
    # Read environment name
    current_env=$(<"$config_file")
    current_env=${current_env//[$'\t\r\n']}  # trim whitespace

    # If we're not already in the right env or under the right root
    if [[ "${CONDA_AUTO_ROOT:-}" != "$PWD" || "${CONDA_DEFAULT_ENV:-}" != "$current_env" ]]; then
      CONDA_AUTO_ROOT="$PWD"

      if [[ -n "$current_env" ]]; then
        echo "Activating Conda env: $current_env"
        conda activate "$current_env" || echo "Failed to activate $current_env"
      else
        echo "Empty .conda_config — skipping activation"
      fi
    fi

  # CASE 2: We're NOT in the auto-activated project root (or its subdirs)
  elif [[ -n "${CONDA_AUTO_ROOT:-}" ]] && [[ "$PWD" != "${CONDA_AUTO_ROOT:-}"* ]]; then
    echo "Leaving project — deactivating Conda env"
    conda deactivate
    unset CONDA_AUTO_ROOT
  fi
}

# Only enable if Conda is loaded
if [[ -n "${CONDA_SHLVL:-}" ]]; then
  add-zsh-hook chpwd conda_chpwd
  # Run once on load in case we're already in a project
  conda_chpwd
fi