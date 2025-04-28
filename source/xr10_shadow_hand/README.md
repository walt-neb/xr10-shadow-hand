# XR10-Shadow Hand Integration

Integration of XR10 robotic arm with Shadow Hand in NVIDIA Isaac Sim for robotic manipulation tasks.

## Project Structure

```
xr10_shadow_hand/
├── assets/         # USD files and other assets
├── scripts/        # Python scripts
├── config/         # Configuration files
├── docs/          # Documentation
└── tests/         # Test scripts
```

## Prerequisites

- NVIDIA Isaac Sim 4.5.0 ([Installation Guide](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/))
- NVIDIA Isaac Lab 4.5.0 ([Installation Guide](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html))
- Python 3.10
- NVIDIA GPU with CUDA support
- Minimum 32GB RAM and 16GB VRAM (recommended)

## Development Environment Setup

The development environment is configured using `setup_dev_env.sh`, which:
- Sets up necessary environment variables
- Configures Python paths for Isaac Sim and Isaac Lab
- Creates symbolic links for easy access to development tools
- Is automatically sourced from your `.bashrc` file

To set up the development environment:
1. Ensure Isaac Sim and Isaac Lab are installed
2. Clone this repository
3. Source the setup script:
   ```bash
   source ~/IsaacLab/setup_dev_env.sh
   ```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/walt-neb/xr10-shadow-hand.git
   cd xr10-shadow-hand
   ```

2. Set up the development environment:
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # or
   .\venv\Scripts\activate  # On Windows

   # Install dependencies
   pip install -r requirements.txt
   ```

## Development

- Place USD files in the `assets/` directory
- Add Python scripts to the `scripts/` directory
- Update configuration in `config/` directory
- Add tests to the `tests/` directory

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 