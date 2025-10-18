"""
Main analysis script for population growth data.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
import json
import os
from models import exponential_model, logistic_model

def load_data(time_file, pop_file):
    """Load and validate input data."""
    time_data = np.loadtxt(time_file)
    population_data = np.loadtxt(pop_file)
    return time_data, population_data

def fit_models(time_data, population_data):
    """Fit both exponential and logistic models to the data."""
    # Initial parameter guesses
    exp_p0 = [2, 0.1]  # Initial population and growth rate
    log_p0 = [100, 0.5, 2]  # Carrying capacity, growth rate, initial population
    
    # Fit models
    exp_params, exp_cov = curve_fit(exponential_model, time_data, population_data, p0=exp_p0)
    log_params, log_cov = curve_fit(logistic_model, time_data, population_data, p0=log_p0)
    
    return exp_params, exp_cov, log_params, log_cov

def calculate_metrics(time_data, population_data, exp_params, log_params):
    """Calculate R-squared values for both models."""
    exp_r2 = r2_score(population_data, exponential_model(time_data, *exp_params))
    log_r2 = r2_score(population_data, logistic_model(time_data, *log_params))
    return exp_r2, log_r2

def create_visualization(time_data, population_data, exp_params, log_params, exp_r2, log_r2):
    """Create and save the visualization."""
    t_smooth = np.linspace(min(time_data), max(time_data), 1000)
    exp_pred = exponential_model(t_smooth, *exp_params)
    log_pred = logistic_model(t_smooth, *log_params)
    
    plt.figure(figsize=(12, 8))
    
    # Plot data and fitted models
    plt.scatter(time_data, population_data, c='blue', s=30, alpha=0.6, label='Observed Data')
    plt.plot(t_smooth, exp_pred, 'r-', linewidth=2, label=f'Exponential Model (R² = {exp_r2:.4f})')
    plt.plot(t_smooth, log_pred, 'g-', linewidth=2, label=f'Logistic Model (R² = {log_r2:.4f})')
    
    # Customize the plot
    plt.xlabel('Time (days)', fontsize=12)
    plt.ylabel('Population Size', fontsize=12)
    plt.title('Population Growth: Data and Model Fitting', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(loc='upper left', fontsize=10)
    
    # Add text box with model parameters
    exp_text = f'Exponential Model:\nN₀ = {exp_params[0]:.2f}\nr = {exp_params[1]:.4f}'
    log_text = f'Logistic Model:\nK = {log_params[0]:.2f}\nr = {log_params[1]:.4f}\nN₀ = {log_params[2]:.2f}'
    
    plt.text(0.02, 0.98, exp_text, transform=plt.gca().transAxes, 
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    plt.text(0.02, 0.78, log_text, transform=plt.gca().transAxes,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('results/population_growth_analysis.png', dpi=300, bbox_inches='tight')
    return plt.gcf()

def save_results_json(exp_params, log_params, exp_r2, log_r2):
    """Save analysis results to JSON file."""
    results = {
        "exponential_model": {
            "parameters": {
                "initial_population": float(exp_params[0]),
                "growth_rate": float(exp_params[1])
            },
            "r_squared": float(exp_r2)
        },
        "logistic_model": {
            "parameters": {
                "carrying_capacity": float(log_params[0]),
                "growth_rate": float(log_params[1]),
                "initial_population": float(log_params[2])
            },
            "r_squared": float(log_r2)
        },
        "model_comparison": {
            "better_model": "Logistic" if log_r2 > exp_r2 else "Exponential",
            "variance_difference_percentage": float((log_r2 - exp_r2)*100 if log_r2 > exp_r2 else (exp_r2 - log_r2)*100)
        }
    }
    
    # Ensure results directory exists
    os.makedirs('results/analysis', exist_ok=True)
    
    # Save to JSON file
    with open('results/analysis/model_results.json', 'w') as f:
        json.dump(results, f, indent=4)

def print_results(exp_params, log_params, exp_r2, log_r2):
    """Print analysis results."""
    print("\nModel Comparison and Analysis:")
    print("-" * 50)
    print(f"Exponential Model R²: {exp_r2:.4f}")
    print(f"Exponential Model Parameters:")
    print(f"- Initial Population (N₀): {exp_params[0]:.2f}")
    print(f"- Growth Rate (r): {exp_params[1]:.4f}")
    
    print(f"\nLogistic Model R²: {log_r2:.4f}")
    print("Logistic Model Parameters:")
    print(f"- Carrying Capacity (K): {log_params[0]:.2f}")
    print(f"- Growth Rate (r): {log_params[1]:.4f}")
    print(f"- Initial Population (N₀): {log_params[2]:.2f}")
    
    print("\nModel Selection:")
    if log_r2 > exp_r2:
        print("The Logistic Model provides a better fit to the data.")
        print(f"It explains {(log_r2 - exp_r2)*100:.2f}% more variance than the Exponential Model.")
    else:
        print("The Exponential Model provides a better fit to the data.")
        print(f"It explains {(exp_r2 - log_r2)*100:.2f}% more variance than the Exponential Model.")

def main():
    """Main analysis workflow."""
    # Load data
    time_data, population_data = load_data('data/time04', 'data/popsize04')
    
    # Fit models
    exp_params, exp_cov, log_params, log_cov = fit_models(time_data, population_data)
    
    # Calculate metrics
    exp_r2, log_r2 = calculate_metrics(time_data, population_data, exp_params, log_params)
    
    # Create visualization
    fig = create_visualization(time_data, population_data, exp_params, log_params, exp_r2, log_r2)
    
    # Print results
    print_results(exp_params, log_params, exp_r2, log_r2)
    
    # Save results to JSON
    save_results_json(exp_params, log_params, exp_r2, log_r2)
    
    plt.show()

if __name__ == "__main__":
    main()
