import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import find_peaks

plt.rc("xtick", labelsize = 20, top = True, bottom = True, direction = "in")   
plt.rc("ytick", labelsize = 20, left = True, right = True, direction = "in")
plt.rc("axes", grid = True, linewidth = 1.2, axisbelow = True)
plt.rc("grid", ls = "dotted", lw = 1)     
plt.rc("font", size = 30, family = "serif", serif = ["Computer Modern Serif"])
plt.rc("text", usetex = True)
plt.rc("figure", figsize = (12, 8), dpi = 72)
plt.rc("ytick.major", width = 1)
plt.rc("xtick.major", width = 1)
plt.rc("legend", fontsize = 15, framealpha = 0.5, edgecolor = "black", fancybox = True)

fig, ax = plt.subplots()

#elements = ["H2","He","Ar","Hg","Ne"]
elements = ["H2","He","Ar"]
colors = plt.cm.tab10.colors  # or any colormap
color_map = {element: colors[i] for i, element in enumerate(elements)}

for element in elements:
    
    data = pd.read_table(f"Exercise 4/Data/Day 2/{element}.txt", skiprows=1, header = None, index_col = False, names = ["wavelength", "intensity"])
    background = pd.read_table(f"Exercise 4/Data/Day 2/{element} BG.txt", skiprows=1, header = None, index_col = False, names = ["wavelength", "intensity"])
    intensity = data.intensity - background.intensity
    peaks = find_peaks(intensity, height = intensity.max() / 5)[0]
    for i, lamb in enumerate([data.wavelength[i] for i in peaks]):
        ax.axvline(lamb,color = color_map[element], label = element if i == 0 else None)
    #fig, ax = plt.subplots()
    #for i in peaks[0]:
        #ax.axvline(data.wavelength[i], color = "black")
    #ax.plot(data.wavelength, intensity)

data = np.loadtxt(f"Exercise 4/Data/Day 1/sol {3}.txt", skiprows=1)
intensity = data[:,1] # W
wavelengths = data[:,0] # nm
ax.plot(wavelengths,intensity, color = "black")

ax.set_ylabel("Intensity [counts]")
ax.set_xlabel("Wavelength [nm]")
ax.set_title("Sun spectra compared to major emission lines")
ax.legend()
plt.show()
fig.savefig("Exercise 4/Figurer/SunComparison.svg")