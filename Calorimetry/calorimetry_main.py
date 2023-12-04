import numpy as np
from matplotlib import pyplot as plt
import dati
from sympy import *
from strumenti_utili_v4 import *

#CALCOLO DI M EQUIVALENTE
m_equivalente = - dati.m1_parte1 + (dati.m2_parte1*(dati.T2_parte1-dati.Teq_parte1)/(dati.Teq_parte1-dati.T1_parte1))

_m1, _m2, _T1, _T2, _Teq = symbols('_m1 _m2 _T1, _T2 _Teq', real=True) #raggio sferette
formula_funzione = - _m1 + (_m2*(_T2-_Teq)/(_Teq-_T1))

#genera uno scalare a partire dalla formula simbolica scritta sopra
def genera_derivata(incognita):
    formula_derivata = diff(formula_funzione, incognita)
    arrmagico = np.array([])
    for i in range(len(dati.m1_parte1)):
        scalare = formula_derivata.subs([(_m1, dati.m1_parte1[i]), (_m2, dati.m2_parte1[i]), (_T1, dati.T1_parte1[i]), (_T2, dati.T2_parte1[i]), (_Teq, dati.Teq_parte1[i])])
        arrmagico = np.append(arrmagico, [scalare.evalf()])
    return arrmagico

derivata_m1 = genera_derivata(_m1)
derivata_m2 = genera_derivata(_m2)
derivata_T1 = genera_derivata(_T1)
derivata_T2 = genera_derivata(_T2)
derivata_Teq = genera_derivata(_Teq)

sigma_m1 = 0.00001
sigma_m2 = 0.00001 #errore dello strumento: 0.01 grammi
sigma_T1 = 0.05 #errore dello strumento: 0.05 gradi celsius
sigma_T2 = 0.05
sigma_Teq = 0.05

incertezza_meq = (( np.power(derivata_m1, 2)*np.power(sigma_m1, 2) ) + ( np.power(derivata_m2, 2)*np.power(sigma_m2, 2) ) + ( np.power(derivata_T1, 2)*np.power(sigma_T1, 2) ) + ( np.power(derivata_T2, 2)*np.power(sigma_T2, 2) ) + ( np.power(derivata_Teq, 2)*np.power(sigma_Teq, 2) ))
incertezza_meq = incertezza_meq.astype(float)
incertezza_meq = np.sqrt(incertezza_meq)

pesi = 1/np.power(incertezza_meq, 2) 

media_massa_equivalente = sum(pesi*m_equivalente)/sum(pesi)
print("PARTE1-------------la media pesata delle masse equivalenti è: {}".format(media_massa_equivalente))

incertezza_media_meq = np.sqrt(1/sum(pesi))
print("l'incertezza sulla media è: {}".format(incertezza_media_meq))


#CALCOLO DEL CALORE SPECIFICO DEL SOLIDO
c_acqua = 4180.0 #J/KgK = J/KgC a 24 gradi C 
c_s = c_acqua*(dati.Teq_parte2-dati.T1_parte2)*(dati.m1_parte2+media_massa_equivalente)/((dati.Ts_parte2-dati.Teq_parte2)*dati.ms_parte2)

#prepara calcolo simbolico per generare derivate
_m1, _ms, _meq, _T_eq, _Ts, _T1 = symbols('_m1 _ms _meq _T_eq _Ts _T1', real=True) #raggio sferette
formula_funzione = c_acqua*(_T_eq-_T1)*(_m1+_meq)/((_Ts-_T_eq)*_ms)

#genera uno scalare a partire dalla formula simbolica scritta sopra
def genera_derivata(incognita):
    formula_derivata = diff(formula_funzione, incognita)
    arrmagico = np.array([])
    for i in range(len(dati.m1_parte2)):
        derivata = formula_derivata.subs([(_m1, dati.m1_parte2[i]), (_ms, dati.ms_parte2[i]), (_T_eq, dati.Teq_parte2[i]), (_Ts, dati.Ts_parte2[i]), (_T1, dati.T1_parte2[i]), (_meq, media_massa_equivalente)])
        arrmagico = np.append(arrmagico, [derivata.evalf()])
    return arrmagico

sigma_T1 = 0.05 #errore dello strumento: 0.05 gradi celsius
sigma_Ts = 0.05
sigma_Teq = 0.05

derivata_m1 = genera_derivata(_m1)
derivata_ms = genera_derivata(_ms)
derivata_T1 = genera_derivata(_T1)
derivata_Ts = genera_derivata(_Ts)
derivata_Teq = genera_derivata(_Teq)
derivata_meq = genera_derivata(_meq)

sigma_cs = (  np.power(derivata_meq*incertezza_media_meq, 2) + ( np.power(derivata_m1, 2)*np.power(dati.sigma_m1_parte2, 2) ) + ( np.power(derivata_ms, 2)*np.power(dati.sigma_ms_parte2, 2) ) + ( np.power(derivata_T1, 2)*np.power(sigma_T1, 2) ) + ( np.power(derivata_Ts, 2)*np.power(sigma_Ts, 2) ) + ( np.power(derivata_Teq, 2)*np.power(sigma_Teq, 2) ))
sigma_cs = np.array(sigma_cs, dtype=np.float64)
sigma_cs = np.sqrt( sigma_cs )
#media pesata delle 3 misure di calore specifico del solido
pesi_cs = 1/np.power(sigma_cs, 2) 

media_cs = sum(pesi_cs*c_s)/sum(pesi_cs)
print("PARTE2-------------la media pesata dei calori specifici in J/CKg è: {}".format(media_cs))

incertezza_media_cs = np.sqrt(1/sum(pesi_cs))
print("l'incertezza sulla media pesata è: {}".format(incertezza_media_cs))

#CALCOLO LA COSTANTE DI JOULE
J = dati.I*dati.V*dati.Delta_t/(dati.c_acqua_parte3*(dati.m1_parte3+media_massa_equivalente)*dati.Delta_T)
print(J)
_m1, _meq, _DeltaT, _Deltat, _I, _V, _c_acqua = symbols('_m1 _meq _DeltaT _Deltat _I _V _c_acqua', real=True) #raggio sferette
formula_funzione = _I*_V*_Deltat/(_c_acqua*(_m1+_meq)*_DeltaT)

#genera uno scalare a partire dalla formula simbolica scritta sopra
def genera_derivata(incognita):
    formula_derivata = diff(formula_funzione, incognita)
    arrmagico = np.array([])
    for i in range(len(dati.Delta_T)):
        derivata = formula_derivata.subs([(_m1, dati.m1_parte3), (_meq, media_massa_equivalente), (_DeltaT, dati.Delta_T[i]), (_Deltat, dati.Delta_t[i]), (_I, dati.I), (_V, dati.V), (_c_acqua, dati.c_acqua_parte3[i])])
        arrmagico = np.append(arrmagico, [derivata.evalf()])
    return arrmagico

derivata_m1 = genera_derivata(_m1)
derivata_Deltat = genera_derivata(_Deltat)
derivata_DeltaT = genera_derivata(_DeltaT)
derivata_I = genera_derivata(_I)
derivata_V = genera_derivata(_V)
derivata_meq = genera_derivata(_meq)

sigma_I = 0.1
sigma_V = 1
sigma_m1 = 0.00001
sigma_DeltaT = 0.1 #errore dello strumento: 0.05 gradi celsius ,moltiplicato per 2
sigma_Deltat = 1 #errore del cronometro

sigma_J = np.power(derivata_meq*incertezza_media_meq, 2) + ( np.power(derivata_m1, 2)*np.power(sigma_m1, 2) ) + ( np.power(derivata_I, 2)*np.power(sigma_I, 2) ) + ( np.power(derivata_V, 2)*np.power(sigma_V, 2) ) + ( np.power(derivata_Deltat, 2)*np.power(sigma_Deltat, 2) ) + ( np.power(derivata_DeltaT, 2)*np.power(sigma_DeltaT, 2) )
sigma_J = np.array(sigma_J, dtype=np.float64)
sigma_J = np.sqrt(sigma_J)
print(sigma_J)
#media pesata delle 5 misure della costante di Joule del solido
pesi_J = 1/np.power(sigma_J, 2) 

media_J = sum(pesi_J*J)/sum(pesi_J)
print("PARTE3-------------la media pesata della costante di Joule è (in J/J): {}".format(media_J))
print("la media pesata della costante di Joule è (in J/Cal): {}".format(media_J/0.000239006)) #0.000239006 è 1 J espresso in Cal

incertezza_media_J = np.sqrt(1/sum(pesi_J))
print("l'incertezza sulla media pesata è: {}".format(incertezza_media_J))
print("l'incertezza sulla media pesata è (J/Cal): {}".format(incertezza_media_J/0.000239006))


#CALCOLO DEL CALORE LATENTE DEL GHIACCIO
T0 = 0 #Celsius
c_ghiaccio = 2051.5
c_l = ( ((dati.m1_parte4+media_massa_equivalente)*4179*(dati.T1_parte4-dati.Teq_parte4)) - (dati.m2_parte4*c_ghiaccio*(T0-dati.T2_parte4)) - (dati.m2_parte4*(dati.Teq_parte4-T0)*4217.7) )/dati.m2_parte4
print("PARTE4-------------il valore del calore latente è {}".format(c_l))

_m1, _m2, _meq, _T_eq, _T2, _T1= symbols('_m1 _m2 _meq _T_eq _T2 _T1', real=True) #raggio sferette
formula_funzione = ( ((_m1+_meq)*4179*(_T1-_T_eq)) - (_m2*c_ghiaccio*(T0-_T2)) - (_m2*(_T_eq-_T1)*4217.7) )/_m2

def genera_derivata(incognita):
    formula_derivata = diff(formula_funzione, incognita)
    derivata = formula_derivata.subs([(_m1, dati.m1_parte4), (_m2, dati.m2_parte4), (_meq, media_massa_equivalente), (_T_eq, dati.Teq_parte4), (_T2, dati.T2_parte4), (_T1, dati.T1_parte4)])
    return derivata.evalf()

derivata_m1 = genera_derivata(_m1)
derivata_meq = genera_derivata(_meq)
derivata_T1 = genera_derivata(_T1)
derivata_Teq = genera_derivata(_T_eq)
derivata_m2 = genera_derivata(_m2)
derivata_T2 = genera_derivata(_T2)

sigma_m1 = 0.00001
sigma_m2 = 0.00001 #errore dello strumento: 0.01 grammi
sigma_T1 = 0.05 #errore dello strumento: 0.05 gradi celsius
sigma_T2 = 0.05
sigma_Teq = 0.05

sigma_lc = np.power(derivata_meq*incertezza_media_meq, 2) + ( np.power(derivata_m1, 2)*np.power(sigma_m1, 2) ) + ( np.power(derivata_m2, 2)*np.power(sigma_m2, 2) ) + ( np.power(derivata_T1, 2)*np.power(sigma_T1, 2) ) +( np.power(derivata_T2, 2)*np.power(sigma_T2, 2) ) + ( np.power(derivata_Teq, 2)*np.power(sigma_Teq, 2) )
sigma_lc = np.array(derivata_meq, dtype=np.float64) #perchè numpy non saprebbe gestire i float di sympy
sigma_lc = np.sqrt( sigma_lc )
print("l'incertezza sul calore latente è {}".format(sigma_lc))