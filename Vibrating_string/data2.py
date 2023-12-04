import numpy as np
from strumenti_utili_v4 import *

#in cm
lunghezza_corda1 = np.array([160.0, 160.5, 160.2, 159.9, 160.0])/100 #corda bianca
lunghezza_corda2 = np.array([174.5, 174.0, 174.3, 174.5, 174.0])/100 #corda viola lunghezza in metri(ho diviso per 100)
lunghezza_corda3 = np.array([197.5, 198.3, 198.0, 197.7, 198.0])/100 #corda fucsia

lunghezze_corde = np.array([
    np.mean(lunghezza_corda1),
    np.mean(lunghezza_corda2),
    np.mean(lunghezza_corda3)
])
print(lunghezze_corde)

sigma_lunghezze = np.array([
    deviazione(lunghezza_corda1, np.mean(lunghezza_corda1)),
    deviazione(lunghezza_corda2, np.mean(lunghezza_corda2)),
    deviazione(lunghezza_corda3, np.mean(lunghezza_corda3))
])/np.sqrt(3)
print(sigma_lunghezze)

#in grammi
massa_corda1 = np.array([0.73, 0.73, 0.72, 0.72, 0.73, 0.72])/1000 #corda bianca
massa_corda2 = np.array([3.82, 3.83, 3.83, 3.82, 3.84, 3.83])/1000 # corda viola in kg (ho diviso per 100)
massa_corda3 = np.array([12.56, 12.57, 12.56, 12.56, 12.58, 12.57])/1000 #corda fucsia

masse_corde = np.array([
    np.mean(massa_corda1),
    np.mean(massa_corda2),
    np.mean(massa_corda3),
])
print(masse_corde)

sigma_masse = np.array([
    deviazione(massa_corda1, np.mean(massa_corda1)),
    deviazione(massa_corda2, np.mean(massa_corda2)),
    deviazione(massa_corda3, np.mean(massa_corda3))
])/np.sqrt(3)
print(sigma_masse)

peso_200g = np.array([201.10, 201.11, 201.11, 201.09, 201.10])/1000
peso_350g = np.array([350.59, 350.58, 350.50, 350.55, 350.57])/1000
peso_450g = np.array([450.96, 450.95, 450.96, 450.96, 450.97])/1000
peso_550g = np.array([550.50, 550.51, 550.50, 550.50, 550.51])/1000

pesetti = np.array([
    np.mean(peso_200g),
    np.mean(peso_350g),
    np.mean(peso_450g),
    np.mean(peso_550g)
])
print(pesetti)

sigma_pesi = np.array([
    deviazione(peso_200g, np.mean(peso_200g)),
    deviazione(peso_350g, np.mean(peso_350g)),
    deviazione(peso_450g, np.mean(peso_450g)),
    deviazione(peso_550g, np.mean(peso_550g)),
])/np.sqrt(4)
print(sigma_pesi)

#----------------PARTE1 senza rotazione ----------------
n = np.array([1, 2, 3, 4, 5])
frequenze = np.array([13.88, 27.89,  42.13, 56.85, 71.87])#n = 1, 2, 3, 4, 5, L = 108, tensione=200g

#----------------PARTE2 senza rotazione ----------------
Tensioni = pesetti*9.81
frequenze_T = np.array([27.89, 36.29, 41.46, 46.23]) #n=2, L=108

#----------------PARTE3 senza rotazione ----------------
Lunghezze = np.array([108, 110.2, 113, 118.3, 121.5])/100 #in metri (ho diviso per 100)
Lunghezze_corrette = np.array([107, 109.2, 112, 117.3, 120.5])/100 #in metri (ho diviso per 100)
frequenze_L = np.array([69.90, 68.68, 66.60, 63.60, 61.96]) #n = 3, tensione=550g (!al secondo posto c'era 69.30)

#----------------PARTE4 senza rotazione----------------
masse_lineari = masse_corde/lunghezze_corde #in kg/m
print("masse lineari: {}".format(masse_lineari))
frequenze_corde = np.array([134.9, 61.96, 39.26]) #corda 1, 2, 3, n= 3, L=121.5, tensione=550g
