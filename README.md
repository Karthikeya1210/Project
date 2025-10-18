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
│   └── population_growth_analysis.png
│
└── README.md          # Project documentation
```

## Requirements
- Python 3.x
- Required packages:
  - numpy: Data handling and mathematical operations
  - matplotlib: Data visualization
  - scipy: Curve fitting
  - scikit-learn: Statistical metrics

## Installation
```bash
pip install numpy matplotlib scipy scikit-learn
```

## Usage
To run the analysis:
1. Ensure you're in the project root directory
2. Execute:
```bash
python3 src/analysis.py
```

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
