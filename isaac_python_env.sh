#!/bin/bash

# Check if a script was provided
if [ $# -eq 0 ]; then
    echo "Error: No Python script provided"
    echo "Usage: $0 <python_script> [args...]"
    exit 1
fi

# Get the script path and arguments
SCRIPT="$1"
shift
ARGS="$@"

# Check if the script exists
if [ ! -f "$SCRIPT" ]; then
    echo "Error: Script '$SCRIPT' not found!"
    exit 1
fi

# Get the Isaac Sim path from the parent directory
ISAACSIM_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Set core Isaac Sim environment variables
export CARB_APP_PATH="$ISAACSIM_PATH/kit"
export ISAAC_PATH="$ISAACSIM_PATH"
export EXP_PATH="$ISAACSIM_PATH/apps"

# Set Python paths
export PYTHONPATH="$ISAACSIM_PATH/kit/python/lib/python3.10:$ISAACSIM_PATH/kit/python/lib/python3.10/site-packages:$ISAACSIM_PATH/python_packages:$ISAACSIM_PATH/exts/isaacsim.simulation_app:$ISAACSIM_PATH/kit/kernel/py:$ISAACSIM_PATH/kit/plugins/bindings-python:$ISAACSIM_PATH/exts"

# Set library paths
export LD_LIBRARY_PATH="$ISAACSIM_PATH/kit:$ISAACSIM_PATH/kit/plugins:$ISAACSIM_PATH/kit/plugins/bindings-python:$ISAACSIM_PATH/kit/libs:$ISAACSIM_PATH/exts"

# Execute the Python script with the Isaac Sim environment
"$ISAACSIM_PATH/python.sh" "$SCRIPT" $ARGS 