# UR10 Picker Project Board

## Project Structure
```
ur10_picker/
├── assets/           # USD and URDF files
├── scripts/          # Python scripts for simulation
└── setup/           # Environment setup scripts
```

## Tasks

### Completed
- [x] Set up development environment with Isaac Sim
- [x] Create basic USD files for UR10 arm and picker
- [x] Implement script to combine USD models
- [x] Create test script for robot movements
- [x] Set up Git repository and project structure

### In Progress
- [ ] Implement grasping logic for picker
- [ ] Create reinforcement learning environment
- [ ] Test combined robot movements
- [ ] Document API and usage

### To Do
- [ ] Implement inverse kinematics for UR10 arm
- [ ] Add collision detection
- [ ] Create visualization tools
- [ ] Set up CI/CD pipeline
- [ ] Write comprehensive documentation

## Notes
- Main development directory: `~/src/ur10_picker`
- Assets are stored in the `assets` directory
- Environment setup scripts in root directory
- Python scripts for simulation in `scripts` directory

## Dependencies
- Isaac Sim 2023.1.1
- Python 3.7+
- NVIDIA GPU with appropriate drivers
- Git for version control

## Setup Instructions
1. Clone the repository
2. Run `setup_dev_env.sh` to set up the environment
3. Source `isaac_python_env.sh` to activate the Python environment
4. Run test scripts to verify setup

## References
- [Isaac Sim Documentation](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/overview.html)
- [UR10 Documentation](https://www.universal-robots.com/products/ur10-robot/) 