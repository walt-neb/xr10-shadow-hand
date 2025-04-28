#!/bin/bash

# Set base paths
export ISAACLAB_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export ISAACSIM_PATH="$ISAACLAB_PATH/../isaacsim"

# Create and activate virtual environment if it doesn't exist
if [ ! -d "$ISAACLAB_PATH/isaaclab_venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$ISAACLAB_PATH/isaaclab_venv"
fi

# Activate virtual environment
source "$ISAACLAB_PATH/isaaclab_venv/bin/activate"

# Install/upgrade pip and required packages
pip install --upgrade pip
if [ -f "$ISAACLAB_PATH/requirements.txt" ]; then
    pip install -r "$ISAACLAB_PATH/requirements.txt"
fi

# Set core Isaac Sim environment variables
export CARB_APP_PATH="$ISAACSIM_PATH/kit"
export ISAAC_PATH="$ISAACSIM_PATH"
export EXP_PATH="$ISAACSIM_PATH/apps"

# Append Isaac Sim paths to PYTHONPATH (don't overwrite)
ISAAC_PYTHON_PATHS=(
    "$ISAACSIM_PATH/kit/python/lib/python3.10"
    "$ISAACSIM_PATH/kit/python/lib/python3.10/site-packages"
    "$ISAACSIM_PATH/python_packages"
    "$ISAACSIM_PATH/exts/isaacsim.simulation_app"
    "$ISAACSIM_PATH/kit/kernel/py"
    "$ISAACSIM_PATH/kit/plugins/bindings-python"
    "$ISAACSIM_PATH/exts"
)

# Combine paths with existing PYTHONPATH
export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}$(IFS=:; echo "${ISAAC_PYTHON_PATHS[*]}")"

# Append Isaac Sim library paths to LD_LIBRARY_PATH
ISAAC_LIB_PATHS=(
    "$ISAACSIM_PATH/kit"
    "$ISAACSIM_PATH/kit/plugins"
    "$ISAACSIM_PATH/kit/plugins/bindings-python"
    "$ISAACSIM_PATH/kit/libs"
    "$ISAACSIM_PATH/exts"
)

# Combine paths with existing LD_LIBRARY_PATH
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH:+${LD_LIBRARY_PATH}:}$(IFS=:; echo "${ISAAC_LIB_PATHS[*]}")"

# Create symbolic link for isaac_python wrapper
mkdir -p ~/.local/bin
ln -sf "$ISAACLAB_PATH/isaac_python_env.sh" ~/.local/bin/isaac_python

# Print diagnostic information
echo "=== Environment Setup ==="
echo "ISAACLAB_PATH: $ISAACLAB_PATH"
echo "ISAACSIM_PATH: $ISAACSIM_PATH"
echo "Virtual Environment: $ISAACLAB_PATH/isaaclab_venv"
echo "PYTHONPATH: $PYTHONPATH"
echo "LD_LIBRARY_PATH: $LD_LIBRARY_PATH"
echo "========================="

echo "Environment setup complete!"
echo "You can now run scripts either way:"
echo "1. Directly with Python (for RL scripts): python your_script.py"
echo "2. With Isaac Sim's environment: isaac_python your_script.py" 