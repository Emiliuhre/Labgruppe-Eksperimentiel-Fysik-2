import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rc("xtick", labelsize = 15, top = False, bottom = True, direction = "in")   
plt.rc("ytick", labelsize = 15, left = True, right = False, direction = "in")
plt.rc("axes", grid = False, linewidth = 1.2, axisbelow = True)
plt.rc("grid", ls = "dotted", lw = 1)     
plt.rc("font", size = 30, family = "serif", serif = ["Computer Modern Serif"])
plt.rc("text", usetex = True)
plt.rc("figure", figsize = (12, 10), dpi = 72)
plt.rc("ytick.major", width = 1)
plt.rc("xtick.major", width = 1)
plt.rc("legend", fontsize = 15, framealpha = 0.5, edgecolor = "black", fancybox = True)

dataR = [pd.read_table(f"Exercise 4/Data/Day 1/R{i}.txt",skiprows = 1, header = None, index_col = False, names = ["Wavelength", "Intensity"]) for i in range(1,5)]
dataG = [pd.read_table(f"Exercise 4/Data/Day 1/G{i}.txt",skiprows = 1, header = None, index_col = False, names = ["Wavelength", "Intensity"]) for i in range(1,5)]
dataB = [pd.read_table(f"Exercise 4/Data/Day 1/B{i}.txt",skiprows = 1, header = None, index_col = False, names = ["Wavelength", "Intensity"]) for i in range(1,5)]
data = [dataR,dataG,dataB]
water = pd.read_table(f"Exercise 4/Data/Day 1/R.txt",skiprows = 1, header = None, index_col = False, names = ["Wavelength", "Intensity"])
air = pd.read_table(f"Exercise 4/Data/Day 1/R background.txt",skiprows = 1, header = None, index_col = False, names = ["Wavelength", "Intensity"])

fig, axes = plt.subplots(3,1, sharex = True)
for dataX, color, ax in zip(data, ["R", "G", "B"], axes):
    for i, dat in enumerate(dataX):
        intensity = dat.Intensity.replace(0,np.nan) - water.Intensity
        if i == 0:
            max_index = np.argmax(intensity[300:1100]) + 300
            max_intensity = intensity[max_index]
        ax.plot(dat.Wavelength, intensity, label = f"{color}{i+1}, $N = {intensity[max_index] / max_intensity:.2f}N_{{{color}1}}$")
        ax.plot(dat.Wavelength[max_index],intensity[max_index], "o", color = "black")
    ax.grid()
    ax.legend()
fig.suptitle("Absorbtion spectre of solutions of 3 different salts")
axes[0].set_title("CoSO$_4$")
axes[1].set_title("NiSO$_4$")
axes[2].set_title("CuSO$_4$")
axes[2].set_xlabel("Wavelength [nm]")
axes[1].set_ylabel("Absorption")
#fig.subplots_adjust(hspace=1,top = 0.9)
fig.tight_layout()
plt.show()
fig.savefig("Exercise 4/Figurer/AbsorbtionSpectra.svg")
