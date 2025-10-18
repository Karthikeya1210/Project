"""
Mathematical models for population growth analysis.
"""
import numpy as np

def exponential_model(t, N0, r):
    """
    Exponential growth model.
    
    Parameters:
    -----------
    t : array-like
        Time points
    N0 : float
        Initial population
    r : float
        Growth rate
    
    Returns:
    --------
    array-like
        Population size at each time point
    """
    return N0 * np.exp(r * t)

def logistic_model(t, K, r, N0):
    """
    Logistic growth model.
    
    Parameters:
    -----------
    t : array-like
        Time points
    K : float
        Carrying capacity
    r : float
        Growth rate
    N0 : float
        Initial population
    
    Returns:
    --------
    array-like
        Population size at each time point
    """
    return K / (1 + ((K - N0) / N0) * np.exp(-r * t))
