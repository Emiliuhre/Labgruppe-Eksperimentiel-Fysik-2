import numpy as np

b = 2.897771955e-3 # m * K
sigmaLambda = 2e-9 # m

temperatures = np.array([])
sigmaTs = np.array([])
for i in range(3):
    data = np.loadtxt(f"Exercise 4/Data/Day 1/sol {i + 1}.txt", skiprows=1)
    intensity = data[:,1] # W
    wavelengths = data[:,0] # nm
    maxWavelength = wavelengths[intensity.argmax()] * 1e-9 # m
    T = b / maxWavelength 
    temperatures = np.append(temperatures, T)
    sigmaT = np.abs(T * sigmaLambda / maxWavelength)
    sigmaTs = np.append(sigmaTs, sigmaT)

weigthedT = np.average(temperatures, weights = sigmaTs**(-2))
weigthedSigma = (np.sum(sigmaTs**(-2)))**(-1/2)

print(f"The temperature of the photosphere is {T:.1f} +- {weigthedSigma:.1f} Kelvin")

    