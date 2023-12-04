# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:48:29 2021

@author: giuly
"""

import numpy as np
from matplotlib import pyplot as plt

#codice necessario per esportare grafici per latex
import matplotlib
import math
#decommentare per grafici belli
#matplotlib.use("pgf")
#imposta il font per essere uguale a quello di latex. potrebbe non funzionare se eseguito su anaconda
# matplotlib.rcParams.update({
#    "pgf.texsystem": "pdflatex",
 #   'font.family': 'serif',
  #  'text.usetex': True,
   # 'pgf.rcfonts': False,
#})

# from scipy.stats import chi2
import dati 
from strumenti_utili_v1 import *


#=======================    parte A1 e A2    =======================
array_dati = np.array(dati.data1)
#array_dati = array_dati/2


#calcolo la media
media = np.sum(array_dati)/array_dati.size
print('la media : m={0:.6f}'.format(media)) #uguale a np.mean

#calcolo la deviazione standard
dev = deviazione(array_dati, media)
print('la deviazione standard sulle misure è: dev={0:.6f}'.format(dev)) #più imparziale di np.std

# calcolo l'errore sulla media
Errore = dev/np.sqrt(array_dati.size)
print('errore standard sulla media: Errore={0:.6f}'.format(Errore))

print('x = {0:.6f} ± {1:.6f}'.format(media,Errore))

#istogramma a barre
min_array = np.floor(10.*min(array_dati))/10 #barbatrucco per arrontondare per difetto (floor) a decimali
max_array = np.ceil(10.*max(array_dati))/10
n = (max_array-min_array)*2/dev #numero degli intervalli
h = int(round(n))
print(h)
plt.hist(array_dati, bins = h, range = [min_array, max_array], alpha = 1, density=True, label='data', color='PaleGreen')

plt.xlabel('$Periodo$ (s)')
plt.ylabel('Frequenza assoluta') 

#distribuzione gaussiana
t = np.linspace(min_array,max_array) # questa funzione definisce un vettore ad alta densità (50 numeri) per calcolare la funzione da disegnare lungo l'asse x
plt.plot(t,gaus(t,media, dev),label=r"$G(x;\bar{T},\sigma)$", color = "darkOrange")

plt.legend()
#salva immagine in formato .pgf (importabile da latex) e in png
#plt.savefig('computed_data/hist_and_gauss.pgf')
plt.savefig('computed_data/hist_and_gauss.png')
plt.show()

#calcolo del chi quadro
chi = chi_sq(dati.data1, media, dev)
print('CALCOLO DEL CHI QUADRO \n il chi quadro per la gaussiana risulta: chi = {0:.3f}'.format(chi))

d = 1
chi_ridotto = chi/d #chi quadro ridotto
print('consultare la tabella delle probabilità relative al chi quadro con chi ridotto = {0:.2f} relativo a {1:.0f} gradi di libertà'.format(chi_ridotto, d))
# pchi_ridotto = 1-chi2.cdf(chi_ridotto,d)
# print('P(chi_ridotto) = {:.1f}%'.format(100.*pchi_ridotto))

#=======================    parte A3    =======================
D1 = np.array(dati.dataD1)
D2 = np.array(dati.dataD2)
D3 = np.array(dati.dataD3)
D4 = np.array(dati.dataD4)


#calcolo la media
medie_D = np.array([
    np.mean(D1),
    np.mean(D2),
    np.mean(D3),
    np.mean(D4),
    ])
print('PARTE A3 \n le medie sono: {}'.format(medie_D)) #uguale a np.mean


#calcolo la deviazione standard
dev_D = np.array([
    deviazione(D1, np.mean(D1)),
    deviazione(D2, np.mean(D2)),
    deviazione(D3, np.mean(D3)),
    deviazione(D4, np.mean(D4)),
    ])
print('la deviazione standard sulle misure è: dev={}'.format(dev_D)) #più imparziale di np.std

# calcolo l'errore sulla media
Errore_D = dev_D/np.sqrt(D1.size)
print('errore standard sulla media: Errore={}'.format(Errore_D))

print('Dx = {} ± {}'.format(medie_D,Errore_D))

#=======================    parte B    =======================

#calcolo delle y
D_sq = np.power(medie_D, 2) 
y = D_sq/100 #dividere per 100 delta t quadro è come dividere per 10 delta t

print(y)

#calcolo delle sigma_y con la propagazione
T = medie_D/10
s_T = Errore_D/10
s_y = 2*T*s_T

print("gli errori sulle y {}".format(s_y))

x = np.array([
    np.mean(dati.datal1),
    np.mean(dati.datal2),
    np.mean(dati.datal3),
    np.mean(dati.datal4),
])
print(x)


#calcolo il coefficiente B
pesi = 1/np.power(s_y,2)
#print(sum(pesi))
delta = (sum(pesi)*sum(pesi*np.power(x,2)))-(np.power(sum(pesi*x),2)) 
coefficiente = ((sum(pesi)*sum(pesi*x*y))-(sum(pesi*x)*sum(pesi*y)))/delta

print("il coefficiente è: B={0:.3f}".format(coefficiente))

#calcolo l'intercetta A 
intercetta = ((sum(pesi*np.power(x,2))*sum(pesi*y))-(sum(pesi*x)*sum(pesi*x*y)))/delta

print("l'intercetta è: A={} dunque non posso trascurarla".format(intercetta))

#calcolo sigma intercetta
sigma_A = np.sqrt(sum(pesi*np.power(x, 2)))/math.sqrt(delta)
print("l'incertezza su A è: sigma_A={}".format(sigma_A))

#calcolo sigma coefficiente
sigma_B = np.sqrt(sum(pesi))/math.sqrt(delta)
print("l'incertezza su B è: sigma_B={}".format(sigma_B))

#calcolo sigma g con la propagazione degli errori e il valore di g
sigma_g = (4*np.power(np.pi,2))/np.power(coefficiente,2)
sigma_g = sigma_g*sigma_B
print("incertezza su g: sigma_g={}".format(sigma_g))

g = (4*np.power(np.pi, 2))/coefficiente
print('accelerazione di gravità: g = {0:.3f}±{1:.3f} '.format(g, sigma_g))

#interpolazione dei dati e retta
plt.errorbar(x, y, s_y, fmt='o', ls='none', label='data')

plt.xlim(left=0)
plt.ylim(bottom=0)

xmin = 0
xmax = max(x)+0.1*(max(x)-min(x))

t = np.linspace(xmin,xmax) # stessa funzione ad alta densità
plt.plot(t,line(t,coefficiente, intercetta),label=r"$y = {0:.2f}x+{1:.2f}$".format(coefficiente, intercetta), color="darkOrange")
#plt.plot(t,line(t,coefficiente, intercetta))
plt.legend() # aggiungo una legenda
#plt.savefig('computed_data/retta.pgf')
plt.savefig('computed_data/retta.png')
plt.show()
#=======================    parte C1 corretta  =======================
l = np.mean(np.array(dati.datal))

teta = np.arccos(dati.h/l) #già restituito in radianti
print(teta)

g1 = 4*np.power(np.pi, 2)*np.power(1+(teta**2/16), 2) /coefficiente
sigma_g1 = (4*np.power(np.pi,2))*np.power(1+(teta**2/16), 2)/np.power(coefficiente,2)
sigma_g1 = sigma_g1*sigma_B
print('accelerazione di gravità senza approssimazione di angolo infinitesimo (correzione): g1 = {0:.3f}±{1:.3f} '.format(g1, sigma_g1))

#=======================    parte C1   =======================
T_osservato = media

l = np.mean(np.array(dati.datal))
teta = np.arccos(dati.h/l) #già restituito in radianti
print("l'angolo vale: {}".format(teta))

#calcolo il periodo senza l'approssimaione di TETA INFINITESIMO
T_vero1 = (1+(teta ** 2/16))
T_vero1 = T_vero1 * T_osservato

print("il valore per T senza approssimazione di angolo infinitesimo è: {0:.4f}".format(T_vero1)) 
Err_sist1 = T_osservato - T_vero1
print("l'errore sistematico dovuto a questa prima approssimazione è: {0:.4f}".format(Err_sist1))

#propagazione dell'errore sistematico sulle y
T = medie_D/10
T = T*(1+((teta ** 2)/16))
y = np.power(T, 2)

s_T_tot1 = np.sqrt(((Errore_D/10)**2)+(Err_sist1**2))
s_y_tot1 = 2*T*s_T_tot1

print("gli errori sulle y considerando anche l'errore sistematico dovuto all'angolo {}".format(s_y_tot1))

#ricalcolo il coefficiente
pesi1 = 1/np.power(s_y_tot1,2)
delta1 = (sum(pesi1)*sum(pesi1*np.power(x,2)))-(np.power(sum(pesi1*x),2)) 
coefficiente1 = ((sum(pesi1)*sum(pesi1*x*y))-(sum(pesi1*x)*sum(pesi1*y)))/delta1
print("il coefficiente è: B1={0:.3f}".format(coefficiente1))

#ricalcolo sigma coefficiente
sigma_B1 = np.sqrt(sum(pesi1)/delta1)
print("l'incertezza su B1 è: sigma_B1={}".format(sigma_B1))

#ricalcolo sigma g con la propagazione degli errori e il valore di g
sigma_g1 = (4*np.power(np.pi,2))/np.power(coefficiente1,2)
sigma_g1 = sigma_g1*sigma_B1
print("incertezza su g1: sigma_g1={}".format(sigma_g1))

g1 = (4*np.power(np.pi, 2))/coefficiente1
print('accelerazione di gravità senza approssimazione di angolo infinitesimo: g1 = {0:.3f}±{1:.3f} '.format(g1, sigma_g1))

#=======================    parte C2 corretta  =======================
R = np.mean(np.array(dati.datadiametro)/2) #raggio in metri
print(R)
l = x
print(l)
g2 = 4*np.power(np.pi, 2)* (1+ ( (2/5)* np.power(R/l, 2) )) /coefficiente
print(g2)
sigma_g2 = 4*np.power(np.pi,2)* (1+ ( (2/5)* np.power(R/l, 2) )) /np.power(coefficiente,2)
sigma_g2 = sigma_g2*sigma_B
print(sigma_g2)
#print('accelerazione di gravità senza approssimazione di massa puntiforme (corretta): g2 = {0:.3f}±{1:.3f} '.format(g2, sigma_g2))

#=======================    parte C2   =======================

l = np.mean(np.array(dati.datal)) #lunghezza in metri
print("lunghezza {}".format(l))
M = np.mean(np.array(dati.datam)/1000) #massa in kg
print("massa {}".format(M))
R = np.mean(np.array(dati.datadiametro)/2) #raggio in metri
print("raggio {}".format(R))

#calcolo il periodo senza l'approssimazione di MASSA PUNTIFORME
T_vero2 = math.sqrt(((M*l*l)+(0.4*M*R*R)))/math.sqrt(M*9.81*l)
T_vero2 = 2*np.pi*T_vero2
print(T_vero2)
Err_sist2 = T_osservato - T_vero2

print("l'errore sistematico dovuto alla seconda approssimazione è: {0:.4f}".format(Err_sist2))

#propagazione dell'errore sistematico sulle y
l1 = np.mean(np.array(dati.datal1)) #lunghezza in metri
l2 = np.mean(np.array(dati.datal2)) #lunghezza in metri
l3 = np.mean(np.array(dati.datal3)) #lunghezza in metri
l4 = np.mean(np.array(dati.datal4)) #lunghezza in metri

T = np.array([
    math.sqrt(((M*l1*l1)+(0.4*M*R*R)))/math.sqrt(M*9.81*l1),
    math.sqrt(((M*l2*l2)+(0.4*M*R*R)))/math.sqrt(M*9.81*l2),
    math.sqrt(((M*l3*l3)+(0.4*M*R*R)))/math.sqrt(M*9.81*l3),
    math.sqrt(((M*l4*l4)+(0.4*M*R*R)))/math.sqrt(M*9.81*l4)
])
T = 2*np.pi*T
y = np.power(T, 2)
s_T_tot2 = np.sqrt(((Errore_D/10)**2)+(Err_sist2**2))
s_y_tot2 = 2*T*s_T_tot2

print("gli errori sulle y considerando anche l'errore sistematico dovuto alla massa non puntiforme {}".format(s_y_tot2))

#ricalcolo il coefficiente
pesi2 = 1/np.power(s_y_tot2,2)
delta2 = (sum(pesi2)*sum(pesi2*np.power(x,2)))-(np.power(sum(pesi2*x),2)) 
coefficiente2 = ((sum(pesi2)*sum(pesi2*x*y))-(sum(pesi2*x)*sum(pesi2*y)))/delta2
print("il coefficiente è: B2={0:.3f}".format(coefficiente2))

#ricalcolo sigma coefficiente
sigma_B2 = np.sqrt(sum(pesi2)/delta2)
print("l'incertezza su B2 è: sigma_B={}".format(sigma_B2))

#ricalcolo sigma g con la propagazione degli errori e il valore di g
sigma_g2 = (4*np.power(np.pi,2))/np.power(coefficiente2,2)
sigma_g2 = sigma_g2*sigma_B2
print("incertezza su g2: sigma_g2={}".format(sigma_g2))

g2 = (4*np.power(np.pi, 2))/coefficiente2
print('accelerazione di gravità senza approssimazione di massa puntiforme: g2 = {0:.3f}±{1:.3f} '.format(g2, sigma_g2))

#=======================    generazione tabelle   =======================
#tabella lunghezze
#crea_tabella(dati.datal, 15, "computed_data/tableLength.tex")
#tabella masse
#crea_tabella(dati.datam, 15, "computed_data/tableMass.tex", "centrata")
#tabella diametro
#crea_tabella(dati.datadiametro, 9, "computed_data/tableDiameter.tex", "centrata")
#tabella periodo
#crea_tabella(dati.dataT1, 15, "computed_data/tablePeriod1.tex", "centrata")

