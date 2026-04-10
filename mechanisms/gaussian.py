import numpy as np

def gaussian_mechanism(true_value, sensitivity, epsilon, delta):
    sigma = sensitivity * np.sqrt(2 * np.log(1.25/delta)) / epsilon
    noise = np.random.normal(0, sigma)
    return true_value + noise