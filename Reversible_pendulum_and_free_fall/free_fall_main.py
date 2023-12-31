import numpy as np
import math
from matplotlib import pyplot as plt

import dati
from strumenti_utili_v2 import *


x = dati.tempi**2
y = dati.altezze
s_t = np.array([
    deviazione(dati.tempo_caduta1, np.mean(dati.tempo_caduta1)),
    deviazione(dati.tempo_caduta2, np.mean(dati.tempo_caduta2)),
    deviazione(dati.tempo_caduta3, np.mean(dati.tempo_caduta3)),
    deviazione(dati.tempo_caduta4, np.mean(dati.tempo_caduta4)),
    deviazione(dati.tempo_caduta5, np.mean(dati.tempo_caduta5)),
    deviazione(dati.tempo_caduta6, np.mean(dati.tempo_caduta6))
])/np.sqrt(10) #divido ogni deviazione per la radice di N (misurazioni)
print("incertezze sui tempi{}".format(s_t))
s_x = 2*dati.tempi*s_t 
print("le incertezze sulle x : {}".format(s_x))

s_y = np.array([
    deviazione(dati.h1, np.mean(dati.h1)),
    deviazione(dati.h2, np.mean(dati.h2)),
    deviazione(dati.h3, np.mean(dati.h3)),
    deviazione(dati.h4, np.mean(dati.h4)),
    deviazione(dati.h5, np.mean(dati.h5)),
    deviazione(dati.h6, np.mean(dati.h6))
])/np.sqrt(4)
print("le incertezze sulle y : {}".format(s_y))

#grafico parabola
#plt.errorbar(dati.tempi, dati.altezze, s_y, fmt='o', ls='none', label='altezze', color= "DarkSlateBlue")
plt.scatter(dati.tempi, dati.altezze, label='$h_{t}$', color= "DarkSlateBlue")
#plt.plot(dati.tempi, dati.altezze, color= "CornflowerBlue")

a = np.arange(0.0, 0.4, 0.001) # Interi tra 0 e 0.4 con intervallo 0.001
cost = 9.81/2      
b = cost*np.power(a, 2) 
plt.plot(a, b, label=r'$h = \frac{1}{2}g t^{2}$')
plt.xlim(0.0, 0.32)
plt.ylim(0.0, 0.70)

plt.xlabel('tempo di caduta (millisecondi)')
plt.ylabel('altezze (metri)') 

plt.legend() # aggiungo una legenda
#plt.savefig('computed_data/retta.pgf')
plt.savefig('computed_data/parabola.png')
plt.show()

#interpolazione dati

#calcolo il coefficiente B
pesi = 1/np.power(s_x, 2)

delta = (sum(pesi*np.power(y, 2))*sum(pesi))-np.power(sum(pesi*y),2) 
coefficiente = ((sum(pesi)*sum(pesi*x*y))-(sum(pesi*y)*sum(pesi*x)))/delta

print("il coefficiente è: B={}".format(coefficiente))

#calcolo l'intercetta A 
intercetta = ((sum(pesi*np.power(y,2))*sum(pesi*x))-(sum(pesi*y)*sum(pesi*x*y)))/delta

print("l'intercetta è: A={} dunque non posso trascurarla".format(intercetta))

#calcolo sigma intercetta
sigma_A = np.sqrt(sum(pesi*np.power(y, 2)))/math.sqrt(delta)
print("l'incertezza su A è: sigma_A={}".format(sigma_A))

#calcolo sigma coefficiente
sigma_B = np.sqrt(sum(pesi))/math.sqrt(delta)
print("l'incertezza su B è: sigma_B={}".format(sigma_B))

#calcolo sigma g con la propagazione degli errori e il valore di g
sigma_g = 2*sigma_B/(coefficiente**2)
print("incertezza su g: sigma_g={}".format(sigma_g))

g = 2/coefficiente
print('accelerazione di gravità: g = {0:.3f}±{1:.3f} '.format(g, sigma_g))


#retta interpolata
plt.errorbar(y, x, s_x, fmt='o', ls='none', label='data', color="OliveDrab")

plt.xlim(left=0)
plt.ylim(bottom=0)

xmin = 0
xmax = max(y)+0.1*(max(y)-min(y))

t = np.linspace(xmin,xmax) # stessa funzione ad alta densità
plt.plot(t,line(t,coefficiente, intercetta),label=r"$y = {0:.2f}x{1:.2f}$".format(coefficiente, intercetta), color="darkOrange")
plt.plot(t,line(t,coefficiente, intercetta))
plt.legend() # aggiungo una legenda
#plt.savefig('computed_data/retta.pgf')
plt.savefig('computed_data/retta.png')
plt.show()

#=======================    generazione tabelle   =======================
#tabella altezze
#crea_tabella(dati.h1, 4, "computed_data/tableHeights.tex")

#----------------PARTE CORRETTA 2-------------------
x = dati.tempi**2
y = dati.altezze - (0.44*dati.tempi) #stimo un errore di 1 cm (la pallina era più in alto della fotocellula)
print("!!!!!!!!!!!!!!!{}".format(y))
s_t = np.array([
    deviazione(dati.tempo_caduta1, np.mean(dati.tempo_caduta1)),
    deviazione(dati.tempo_caduta2, np.mean(dati.tempo_caduta2)),
    deviazione(dati.tempo_caduta3, np.mean(dati.tempo_caduta3)),
    deviazione(dati.tempo_caduta4, np.mean(dati.tempo_caduta4)),
    deviazione(dati.tempo_caduta5, np.mean(dati.tempo_caduta5)),
    deviazione(dati.tempo_caduta6, np.mean(dati.tempo_caduta6))
])/np.sqrt(10) #divido ogni deviazione per la radice di N (misurazioni)

s_x = 2*dati.tempi*s_t 
print("le incertezze sulle x : {}".format(s_x))

s_y = np.array([
    deviazione(dati.h1, np.mean(dati.h1)),
    deviazione(dati.h2, np.mean(dati.h2)),
    deviazione(dati.h3, np.mean(dati.h3)),
    deviazione(dati.h4, np.mean(dati.h4)),
    deviazione(dati.h5, np.mean(dati.h5)),
    deviazione(dati.h6, np.mean(dati.h6))
])/np.sqrt(4)
print("le incertezze sulle y : {}".format(s_y))

#grafico parabola
#plt.errorbar(dati.tempi, dati.altezze, s_y, fmt='o', ls='none', label='altezze', color= "DarkSlateBlue")
plt.scatter(dati.tempi, dati.altezze, label='$h_{t}$', color= "DarkSlateBlue")
#plt.plot(dati.tempi, dati.altezze, color= "CornflowerBlue")

a = np.arange(0.0, 0.4, 0.001) # Interi tra 0 e 0.4 con intervallo 0.001
cost = 9.81/2      
b = (0.44*a)+cost*np.power(a, 2) 
plt.plot(a, b, label=r'$h = 0.44t + \frac{1}{2}g t^{2}$')
plt.xlim(0.0, 0.32)
plt.ylim(0.0, 0.70)

plt.xlabel('tempo di caduta (millisecondi)')
plt.ylabel('altezze (metri)') 

plt.legend() # aggiungo una legenda
#plt.savefig('computed_data/retta.pgf')
plt.savefig('computed_data/parabola_corretta.png')
plt.show()

#interpolazione dati

#calcolo il coefficiente B
pesi = 1/np.power(s_x, 2)

delta = (sum(pesi*np.power(y, 2))*sum(pesi))-np.power(sum(pesi*y),2) 
coefficiente = ((sum(pesi)*sum(pesi*x*y))-(sum(pesi*y)*sum(pesi*x)))/delta

print("il coefficiente è: B={}".format(coefficiente))

#calcolo l'intercetta A 
intercetta = ((sum(pesi*np.power(y,2))*sum(pesi*x))-(sum(pesi*y)*sum(pesi*x*y)))/delta

print("l'intercetta è: A={} dunque non posso trascurarla".format(intercetta))

#calcolo sigma intercetta
sigma_A = np.sqrt(sum(pesi*np.power(y, 2)))/math.sqrt(delta)
print("l'incertezza su A è: sigma_A={}".format(sigma_A))

#calcolo sigma coefficiente
sigma_B = np.sqrt(sum(pesi))/math.sqrt(delta)
print("l'incertezza su B è: sigma_B={}".format(sigma_B))

#calcolo sigma g con la propagazione degli errori e il valore di g
sigma_g = 2*sigma_B/(coefficiente**2)
print("incertezza su g: sigma_g={}".format(sigma_g))

g = 2/coefficiente
print('accelerazione di gravità: g = {0:.3f}±{1:.3f} '.format(g, sigma_g))


#retta interpolata
plt.errorbar(y, x, s_x, fmt='o', ls='none', label='data', color="OliveDrab")

plt.xlim(left=0)
plt.ylim(bottom=0)

xmin = 0
xmax = max(y)+0.1*(max(y)-min(y))

t = np.linspace(xmin,xmax) # stessa funzione ad alta densità
plt.plot(t,line(t,coefficiente, intercetta),label=r"$y = {0:.2f}x{1:.2f}$".format(coefficiente, intercetta), color="darkOrange")
plt.plot(t,line(t,coefficiente, intercetta))
plt.legend() # aggiungo una legenda
#plt.savefig('computed_data/retta.pgf')
plt.savefig('computed_data/retta_corretta.png')
plt.show()