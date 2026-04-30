import numpy as np
import matplotlib.pyplot as plt

plt.rc("xtick", labelsize = 15, top = False, bottom = False, direction = "in")   
plt.rc("ytick", labelsize = 15, left = False, right = False, direction = "in")
plt.rc("axes", grid = False, linewidth = 1.2, axisbelow = True)
plt.rc("grid", ls = "dotted", lw = 1)     
plt.rc("font", size = 30, family = "serif", serif = ["Computer Modern Serif"])
plt.rc("text", usetex = True)
plt.rc("figure", figsize = (12, 6), dpi = 72)
plt.rc("ytick.major", width = 1)
plt.rc("xtick.major", width = 1)
plt.rc("legend", fontsize = 15, framealpha = 0.5, edgecolor = "black", fancybox = True)

data = np.loadtxt("Exercise 4/Data/Day 2/H2.txt", skiprows=1)
background = np.loadtxt("Exercise 4/Data/Day 2/H2 BG.txt", skiprows=1)

wavelengths = data[::,0]
intensity = data[::,1]-background[::,1]

fig, ax = plt.subplots()
spectra_plot, = ax.plot(wavelengths, intensity, color = "C3", label = "Measurements")

rydberg_constant = 1.097e7 * 1e-9 # nm^-1
Balmer = [(rydberg_constant * (1/4 - 1/(i)**2))**(-1) for i in range(3,100)]
for i,lamb in enumerate(Balmer):
    line = ax.axvline(lamb, color = "black", linestyle = "--", alpha = 0.5, label = "Balmer Series" if i == 5 else None)

inset_ax = ax.inset_axes((0.65, 0.5, 0.3, 0.3))
condition = (wavelengths >= Balmer[-1]) & (wavelengths <= Balmer[3])
inset_ax.set_ylim(np.min(intensity[condition]), np.max(intensity[condition]))
for i,lamb in enumerate(Balmer[3:]):
    inset_ax.axvline(lamb, color = "black", linestyle = "--", alpha = 0.5)
inset_ax.plot(wavelengths[condition], intensity[condition], color = "C3")
ax.indicate_inset_zoom(inset_ax, edgecolor="C0", alpha = 1)

ax.set_ylim(min(intensity), max(intensity))
ax.set_title("Hydrogen Spectra")
ax.set_xlabel("Wavelength [nm]")
ax.set_ylabel("Intensity [counts]")
ax.legend()

#plt.show()

fig.savefig("Exercise 4/Figures/HydrogenSpecta.svg")