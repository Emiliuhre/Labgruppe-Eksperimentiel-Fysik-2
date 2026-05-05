import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, fsolve

# CONFIGURATION
# Define input angle (theta_i) relative to the normal of the entry face of the prism (in degrees).
theta_i_deg = 60  # Change this to your experimental value
theta_i = np.radians(theta_i_deg)

def sellmeier_eqn(lamb, n_target):
    B1, C1 = 1.73759695, 0.013188707
    B2, C2 = 0.313747346, 0.0623068142
    B3, C3 = 1.89878101, 155.23629
    
    term1 = (B1 * lamb**2) / (lamb**2 - C1)
    term2 = (B2 * lamb**2) / (lamb**2 - C2)
    term3 = (B3 * lamb**2) / (lamb**2 - C3)
    
    # Dette er n^2 ifølge formlen
    n2_calc = 1 + term1 + term2 + term3
    
    # TRICK: Returner forskellen i n^2 i stedet for n. 
    # Så slipper vi for np.sqrt() helt!
    return n2_calc - n_target**2

def theta_o(n):
    return np.arcsin(n * np.sin(np.radians(60) - np.arcsin(np.sin(theta_i) / n)))

fig, axes = plt.subplots(3,1)
data = pd.read_excel("Exercise 4/Data/Day 3/OurSpectrometer.xlsx")
angles = data["Angle [deg]"][1: ].astype(float)
elements = [col for col in data.columns if col != "Angle [deg]"]
t = 0
for element, ax in zip(elements, axes):
    if element != "Angle [deg]":

        our_data = data[element][1:] # mV
        our_background = data[element][0] # mV
        intensity = our_data - our_background
        reference_data = pd.read_table(f"Exercise 4/Data/Day 2/{element[:2]}.txt", skiprows=1, header = None, index_col = False, names = ["Wavelength", "Intensity"])
        reference_background = pd.read_table(f"Exercise 4/Data/Day 2/{element[:2]} BG.txt", skiprows=1, header = None, index_col = False, names = ["Wavelength", "Intensity"])
        reference_intensity = reference_data.Intensity - reference_background.Intensity

        our_theta_o = np.radians(angles)
        f  = lambda n, theta: np.abs(theta_o(n) - theta)
        ns = []
        nner = np.linspace(1.7, 1.9, 1000)
        
        for theta in our_theta_o:       
            n = nner[min(f(nner, theta)) == f(nner, theta)]
            ns.append(n)
        
        lambs = []
        for n in ns:
            lamb = fsolve(sellmeier_eqn, 0.4, args=(n,)) #mu m
            lambs.append(lamb*1e3) #nm
        
        ax.stem(lambs, intensity/max(intensity), linefmt='grey', markerfmt='o', basefmt=" ")
        ax.plot(reference_data.Wavelength, reference_intensity/max(reference_intensity))
        # Find ud af hvilket element vi kigger på (sikrer at navnet matcher dict)
        
        

        ax.legend() # Vis en boks, der forklarer farverne
        t += 1
        #ax.plot(our_theta_o, intensity)

axes[1].set_ylabel("Intensity $\\left[\\text{mV}\\right]$")
axes[2].set_xlabel("Wavelength $\\left[\\text{nm}\\right]$")



plt.show()