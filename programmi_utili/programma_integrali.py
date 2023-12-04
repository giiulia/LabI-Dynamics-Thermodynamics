import numpy as np
import scipy
from scipy.integrate import quad
from strumenti_utili_v4 import *

def integrand(x):
    return np.exp(-x**2/2)/np.sqrt(2*np.pi)

t = 0.14
I =  quad(integrand, -t, t)
print(I)

deltap = np.array([0.00, 0.001,0.001,  -0.001, -0.001])
#I = np.array([0.327,0.330,0.209,0.282,0.272])
print(np.mean(deltap))
#print(np.mean(I))
print(deviazione(deltap, np.mean(deltap))/np.sqrt(5))
#print(deviazione(I, np.mean(I))/np.sqrt(5))