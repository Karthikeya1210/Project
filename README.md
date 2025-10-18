# Population Growth Analysis Project

## Project Overview
This project analyzes population growth data using mathematical models to understand and predict population dynamics. It compares exponential and logistic growth models to determine which better describes the observed data.

## Data Interpretation
The population data reveals several key characteristics:
1. The population starts with a small initial size (around 2-3 individuals) and shows clear growth over time
2. The growth pattern exhibits two distinct phases: rapid initial growth followed by gradual deceleration
3. As time progresses, the population appears to stabilize, suggesting the presence of environmental carrying capacity
4. The data shows minor fluctuations around the stabilization point, indicating natural population variations
5. The final population size (approximately 94 individuals) suggests resource limitations affecting growth
6. The growth pattern strongly aligns with logistic growth characteristics (R² = 0.9564), indicating density-dependent factors
7. The carrying capacity estimate of 117 individuals represents the environment's maximum sustainable population
8. The transition from exponential to limited growth occurs around the midpoint of the observation period

## Features
- Data visualization of population growth over time
- Implementation of two growth models:
  - Exponential Growth Model: N(t) = N₀eʳᵗ
  - Logistic Growth Model: N(t) = K/(1 + ((K-N₀)/N₀)e⁻ʳᵗ)
- Statistical analysis using R² for model comparison
- Parameter estimation using curve fitting
- Detailed visualization with model comparisons

## Project Structure
```
Project/
│
├── data/               # Data files
│   ├── time04         # Time points data
│   └── popsize04      # Population size measurements
│
├── src/               # Source code
│   ├── models.py      # Mathematical model definitions
│   └── analysis.py    # Main analysis script
│
├── results/           # Analysis outputs
│   ├── analysis/      # Analysis results in various formats
│   │   └── model_results.json    # Model parameters and statistics
│   └── population_growth_analysis.png  # Visualization plot
│
├── .gitignore         # Git ignore rules
└── README.md          # Project documentation
```

## Setup and Installation

### 1. Install Python
If you haven't installed Python 3.x yet, here's how to install it:

#### On macOS:
```bash
# Using Homebrew (recommended)
# First, install Homebrew if you haven't:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then install Python
brew install python3
```

#### On Windows:
1. Download the installer from [Python's official website](https://www.python.org/downloads/)
2. Run the installer
3. Make sure to check "Add Python to PATH" during installation

#### On Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

Verify the installation:
```bash
python3 --version
```

### 2. Set Up Python Environment
It's recommended to use a virtual environment:
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 2. Install Requirements
- Required packages:
  - numpy: Data handling and mathematical operations
  - matplotlib: Data visualization
  - scipy: Curve fitting
  - scikit-learn: Statistical metrics

### Install Required Packages
```bash
pip install numpy matplotlib scipy scikit-learn
```

## Usage

### 1. Prepare the Environment
Ensure you're in the project root directory and your virtual environment is activated (if using one).

### 2. Run the Analysis
```bash
python3 src/analysis.py
```

### 3. View Results
After running the analysis:
- Check `results/population_growth_analysis.png` for the visualization
- Review `results/analysis/model_results.json` for detailed model parameters and statistics

## Results
The analysis compares two population growth models:

### Exponential Model Results
- Initial Population (N₀): 26.64
- Growth Rate (r): 0.1696
- R² Score: 0.7787

### Logistic Model Results
- Carrying Capacity (K): 117.13
- Growth Rate (r): 0.7922
- Initial Population (N₀): 4.23
- R² Score: 0.9564

### Key Findings
- The Logistic Model provides a significantly better fit
- Explains 17.77% more variance than the Exponential Model
- Suggests a carrying capacity of approximately 117 individuals
- Shows initial rapid growth followed by population stabilization

## Visualizations
The script generates a comprehensive plot showing:
- Original data points
- Fitted exponential model
- Fitted logistic model
- Model parameters and R² values
- Clear comparison of model performances

## Course Information
This project is part of the MA3080/4080/7080 Mathematical Modelling course.

## Author
ponnadabalakousik-ux
