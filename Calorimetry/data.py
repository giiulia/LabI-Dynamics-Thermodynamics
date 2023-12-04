import numpy as np
from strumenti_utili_v4 import *

#-------------PARTE 1-------------
#m1 
m1_parte1 = np.array([0.09972, 0.09075, 0.09975, 0.14294])

#m2 
m2_parte1 = np.array([0.10343, 0.09253, 0.10040, 0.08663])

#T1
T1_1 = 24.5 #gradi celsius
T1_2 = np.mean(np.array([23.8, 23.6, 23.6, 23.7, 23.6])) #0.05
T1_3 = np.mean(np.array([23.6, 23.8, 23.6, 23.6, 23.6]))
T1_4 = 22.0

T1_parte1 = np.array([T1_1, T1_2, T1_3, T1_4])

#T2
T2_parte1 = np.array([85.5, 40.3, 53.2, 88.0])

#T equilibrio
Teq_parte1 = np.array([50, 32.1, 39.3, 44.5])

#-------------PARTE 2-------------

#m1
m1_1 = np.array([0.19075, 0.19074, 0.19074, 0.19073])
m1_2 = np.array([0.22347, 0.22345, 0.22345, 0.22345])
m1_3 = np.array([0.24876, 0.24877, 0.24878, 0.24876])


m1_parte2 = np.array([
    np.mean(m1_1),
    np.mean(m1_2),
    np.mean(m1_3)
])

sigma_m1_parte2 = np.array([
    deviazione(m1_1, np.mean(m1_1)),
    deviazione(m1_2, np.mean(m1_2)),
    deviazione(m1_3, np.mean(m1_3))

])


#ms
ms_1 = np.array([0.12993, 0.12991]) #RAME
ms_2 = np.array([0.12993, 0.12991]) #RAME
ms_3 = np.array([0.12993, 0.12991]) #RAME


ms_parte2 = np.array([
    np.mean(ms_1),
    np.mean(ms_2),
    np.mean(ms_3)
])

sigma_ms_parte2 = np.array([
    deviazione(ms_1, np.mean(ms_1)),
    deviazione(ms_2, np.mean(ms_2)),
    deviazione(ms_3, np.mean(ms_3))

])

#T1
T1_parte2 = np.array([22.5, 22.3, 22.5])

#T2
Ts_parte2 = np.array([100, 100, 100])

#T equilibrio
Teq_parte2 = np.array([26, 25.5, 25.4])

#-------------PARTE 3-------------
#m1 = np.array([271.88])

#m1_parte3 = np.mean( m1 )
#sigma_m1_parte3 = deviazione(m1, m1_parte3),

#T_iniziale = 25 
#Delta_t = np.array([120, 120, 120, 120, 480]) #intervalli di tempo, l'ultimo elemento dell'array è il delta t totale= somma di tutti gli intervallini
#Delta_T = np.array([]) #sbalzi di Temperatura corrispondenti ai tempi sopra, l'ultimo è il delta T totale
#I = np.array([1.4, 1.7, 2.1, 2.4]) #corrente corrispondente a ogni intervallo di tempo
#V = np.array([10, 12, 14, 16]) #voltaggio corrispondente a ogni intervallo di tempo
#T = np.array([26.5, 28.5, 31.5, 35])

m1_parte3 = 0.30998
c_acqua_parte3 = np.array([4180.0, 4178.8, 4178.3, 4178.3, 4180.0]) #24, 28, 32, 32, 24  J/KgK
Delta_t = np.array([120, 120, 120, 120, 480]) #intervalli di tempo, l'ultimo elemento dell'array è il delta t totale= somma di tutti gli intervallini
Delta_T = np.array([2.5, 3.0, 2.5, 3.5, 11.5]) #sbalzi di Temperatura corrispondenti ai tempi sopra, l'ultimo è il delta T totale
I = 2.2   #costante 0.1
V = 15 #costante 1
#-
T_iniziale = 25 
T = np.array([27.5, 30.5, 33, 36.5])
#-
#-------------PARTE 4-------------

#m1
m1_parte4 = 0.24098

#m2
m2_parte4 = 0.0142

#T1
T1_parte4 = 26

#T2
T2_parte4 = -17

#T equilibrio
Teq_parte4 = 19.5
