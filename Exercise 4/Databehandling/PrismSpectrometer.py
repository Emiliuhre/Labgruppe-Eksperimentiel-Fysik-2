import pandas as pd
import numpy as np
from scipy.optimize import brentq
import matplotlib.pyplot as plt

# CONFIGURATION
# Define input angle (theta_i) relative to the normal of the entry face of the prism (in degrees).
THETA_I_DEG = 15.0  # Change this to your experimental value
THETA_I = np.radians(THETA_I_DEG)

# PHYSICAL EQUATIONS
def get_theta_o_from_n(n, theta_i):
    """Calculates outgoing angle based on Refractive Index n."""
    # Snell's law geometry provided in lab manual
    # theta_o = arcsin(n * sin(60 - arcsin(sin(theta_i)/n)))
    term_inner = np.arcsin(np.sin(theta_i) / n)
    return np.degrees(np.arcsin(n * np.sin(np.radians(60) - term_inner)))

def sellmeier_eqn(n, lmbda):
    """
    Returns the difference (n^2 - 1) - Sellmeier_result.
    We want this to be zero to find the correct wavelength.
    Note: Sellmeier equations usually assume lambda in micrometers (um).
    """
    l2 = lmbda**2
    n2_minus_1 = (1.73759695 * l2) / (l2 - 0.013188707) + \
                 (0.313747346 * l2) / (l2 - 0.0623068142) + \
                 (1.89878101 * l2) / (l2 - 155.23629)
    return (n**2 - 1) - n2_minus_1

def solve_for_n(target_theta_o, theta_i):
    """Finds n that produces the target theta_o."""
    # We define a function f(n) = calculated_theta - target
    func = lambda n: get_theta_o_from_n(n, theta_i) - target_theta_o
    # Search range for n (Glass typically between 1.5 and 2.0)
    return brentq(func, 1.5, 2.0)

# MAIN PROCESSING
def process_spectrum(file_path):
    df = pd.read_csv(file_path) # Assumes .txt or .csv with headers 'angle', 'intensity'
    
    wavelengths = []
    
    print(f"Processing {len(df)} data points...")
    
    for _, row in df.iterrows():
        # Find the refractive index n for this specific angle
        n = solve_for_n(row['angle'], THETA_I)
        
        # Find wavelength lambda that corresponds to that n
        # We solve sellmeier_eqn(n, lambda) = 0
        # Wavelength search range (0.3 to 1.0 um for visible)
        lmbda = brentq(lambda l: sellmeier_eqn(n, l), 0.3, 1.0)
        wavelengths.append(lmbda * 1000) # Convert to nanometers (nm)

    df['wavelength_nm'] = wavelengths
    return df

# EXECUTION
# Usage:
# data = process_spectrum('your_data.txt')
# print(data.head())

# Plotting
# plt.plot(data['wavelength_nm'], data['intensity'])
# plt.xlabel('Wavelength (nm)')
# plt.ylabel('Intensity')
# plt.show()