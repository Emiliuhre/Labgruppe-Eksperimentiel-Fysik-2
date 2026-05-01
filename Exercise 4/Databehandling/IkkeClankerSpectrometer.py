import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CONFIGURATION
# Define input angle (theta_i) relative to the normal of the entry face of the prism (in degrees).
theta_i_deg = 60  # Change this to your experimental value
theta_i = np.radians(theta_i_deg)

def sellmeier_eqn(lmbda):
    l2 = lmbda**2
    n2_minus_1 = (1.73759695 * l2) / (l2 - 0.013188707) + \
                 (0.313747346 * l2) / (l2 - 0.0623068142) + \
                 (1.89878101 * l2) / (l2 - 155.23629)
    return np.sqrt(n2_minus_1 + 1)

def theta_o(lamb):
    n = sellmeier_eqn(lamb)
    return np.arcsin(n * np.sin(np.radians(60) - np.arcsin(np.sin(theta_i) / n)))


fig, axes = plt.subplots(3,1)
data = pd.read_excel("Exercise 4/Data/Day 3/OurSpectrometer.xlsx")
angles = data["Angle [deg]"]
elements = [col for col in data.columns if col != "Angle [deg]"]

for element, ax in zip(elements, axes):
    if element != "Angle [deg]":

        our_data = data[element][1:] # mV
        our_background = data[element][0] # mV
        reference_data = pd.read_table(f"Exercise 4/Data/Day 2/{element[:2]}.txt", skiprows=1, header = None, index_col = False, names = ["Wavelength", "Intensity"])
        reference_background = pd.read_table(f"Exercise 4/Data/Day 2/{element[:2]} BG.txt", skiprows=1, header = None, index_col = False, names = ["Wavelength", "Intensity"])
        reference_intensity = reference_data.Intensity - reference_background.Intensity

        our_theta_o = 1
        ax.plot(reference_data.Wavelength, reference_intensity)

plt.show()