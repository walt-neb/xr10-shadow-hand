# UR10 Picker Project

A robotic manipulation project combining a UR10 robotic arm with a custom picker end-effector, simulated in NVIDIA Isaac Sim.

## Overview

This project implements a robotic manipulation system that combines a Universal Robots UR10 arm with a custom-designed picker end-effector. The system is simulated in NVIDIA Isaac Sim, providing a realistic environment for testing and development of robotic manipulation tasks.

## Project Structure

```
ur10_picker/
├── assets/           # USD and URDF files for robots and environment
├── scripts/         # Python scripts for simulation and control
│   ├── combine_models.py    # Combines UR10 and picker USD files
│   └── test_movements.py    # Tests basic robot movements
└── setup/          # Environment setup scripts
    ├── setup_dev_env.sh     # Sets up development environment
    └── isaac_python_env.sh  # Activates Isaac Sim Python environment
```

## Prerequisites

- NVIDIA Isaac Sim 2023.1.1 or later
- Python 3.7+
- NVIDIA GPU with appropriate drivers
- Git for version control

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ur10_picker.git
   cd ur10_picker
   ```

2. Set up the development environment:
   ```bash
   ./setup/setup_dev_env.sh
   ```

3. Activate the Isaac Sim Python environment:
   ```bash
   source setup/isaac_python_env.sh
   ```

## Usage

1. Combine the UR10 and picker models:
   ```bash
   python scripts/combine_models.py
   ```

2. Test the robot movements:
   ```bash
   python scripts/test_movements.py
   ```

## Development Status

See [Project Board](project_board.md) for current development status and upcoming tasks.

### Current Features
- Basic USD model combination
- Robot movement testing
- Development environment setup

### In Progress
- Grasping logic implementation
- Reinforcement learning environment
- Movement testing
- API documentation

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- NVIDIA Isaac Sim team for the simulation environment
- Universal Robots for the UR10 robot model and documentation 