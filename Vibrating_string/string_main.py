import numpy as np
from matplotlib import pyplot as plt
import data
from strumenti_utili_v4 import *

#----------------PARTE1 con rotazione ----------------
coefficiente_atteso = (1/ (2*1.08) ) * np.sqrt( (dati.pesetti[0]*9.81) / 0.00219691) #1.08 è la distanza tra i due vincoli della corda; 0.00219691 è la massa lineare della corda 1 (kg/m)
velocità_attesa = np.sqrt( (dati.pesetti[0]*9.81) / 0.00219691)

#grafico atteso
x = np.arange(0.0, 100., 0.01)
cost = np.sqrt(9.81*0.2/0.00219691)/(2*1.08)
y = cost*x
plt.plot(x, y, label=r"$y = \frac{x}{2L}\sqrt{\frac{\tau}{\mu}}$", color="DarkTurquoise")

#plt.errorbar(dati.n, dati.frequenze, 0.01, fmt='o', ls='none', label=r"$\nu_{n}$", color="FireBrick")
plt.scatter(dati.n, dati.frequenze, label=r"$\nu_{n}$", color="FireBrick")
#plt.plot(dati.n, dati.frequenze, color="Crimson")

plt.xlim(0.0, 6.0)
plt.ylim(0.0, 80.0)

plt.xlabel('n', fontsize = 12)
plt.ylabel('frequenza (Hz)', fontsize = 12) 
plt.legend() # aggiungo una legenda
plt.grid()
plt.savefig('computed_data/grafico_parte1.png')
plt.show()


#interpolazione
x  = dati.n
y = dati.frequenze
s_y = 0.01

#calcolo del coefficiente
delta = ( x.size*sum(np.power(x, 2)) ) - np.power(sum(x), 2) 
coefficiente = ( (x.size*sum(x*y)) - (sum(x)*sum(y)) )/delta
intercetta = ( (sum(np.power(x, 2))*sum(y))-(sum(x)*sum(x*y)) )/delta
print("il coefficiente è: B={0:.3f} da confrontare con {1:.3f}".format(coefficiente, coefficiente_atteso))
print("l'intercetta è: A={0:.3f} ".format(intercetta))

#calcolo sigma coefficiente
sigma_B = np.sqrt( x.size/delta )*s_y
sigma_A = np.sqrt(sum(x**2)/delta)*0.01
print("l'incertezza su B è: sigma_B={}".format(sigma_B))
print("l'incertezza su A è: sigma_A={}".format(sigma_A))


#calcolo sigma velocità con la propagazione degli errori e il valore della velocità
sigma_velocità = 2*1.08*sigma_B
velocità = 2*1.08*coefficiente

print('velocità: = {0:.3f}±{1:.3f} da confrontare con il valore atteso di {2:.3f}'.format(velocità, sigma_velocità, velocità_attesa))

r = sum((x-np.mean(x))*(y-np.mean(y)))/np.sqrt(sum((x-np.mean(x))**2)*sum((y-np.mean(y))**2) )
print("coefficiente di correlazione lineare: {}".format(r))
#----------------PARTE2 con rotazione ----------------
#plt.errorbar(dati.Tensioni, dati.frequenze_T, 0.01, fmt='o', ls='none', label=r"$\nu_{T}, seconda armonica$", color="DarkOrange")
plt.scatter(dati.Tensioni, dati.frequenze_T, label=r"$\nu_{T}, seconda armonica$", color="DarkOrange")
#plt.plot(dati.Tensioni, dati.frequenze_T, color="Orange")

#grafico atteso
x = np.arange(0.0, 100., 0.1)
cost = 1/( 1.08 * np.sqrt(0.00219691) )     
y = cost*np.sqrt(x)
plt.plot(x, y, label=r"$y = \frac{n}{2L\sqrt{\mu}}\sqrt{x}$", color="DarkTurquoise")
plt.xlim(0.0, 6.0)
plt.ylim(20.0, 50.0)

plt.xlabel('tensione (N)', fontsize = 12)
plt.ylabel('frequenza (Hz)', fontsize = 12) 
plt.legend() # aggiungo una legenda
plt.grid() #aggiungo la griglia
plt.savefig('computed_data/grafico_parte2.png')
plt.show()

#----------------PARTE3 con rotazione ----------------
#plt.errorbar(dati.Lunghezze, dati.frequenze_L, 0.01, fmt='o', ls='none', label=r"$\nu_{L}, terza armonica$", color="RebeccaPurple")
plt.scatter(dati.Lunghezze, dati.frequenze_L, label=r"$\nu_{L},terza armonica$", color="RebeccaPurple")
#plt.plot(dati.Lunghezze, dati.frequenze_L, color="MediumPurple")

#grafico atteso
x = np.arange(0.0, 1.5, 0.001)
cost = (np.sqrt(9.81*0.55/0.00219691)*3)/2     
y = cost/x
plt.plot(x, y, label=r"$y = \frac{3}{2x}\sqrt{\frac{\tau}{\mu}}$", color="DarkTurquoise")
plt.xlim(1.0, 1.5)
plt.ylim(60.0, 75.0)

plt.xlabel('lunghezza (m)', fontsize = 12)
plt.ylabel('frequenza (Hz)', fontsize = 12) 
plt.legend() # aggiungo una legenda
plt.grid()
plt.savefig('computed_data/grafico_parte3.png')
plt.show()

#----------------PARTE4 con rotazione ----------------
#plt.errorbar(dati.masse_lineari, dati.frequenze_corde, 0.01, fmt='o', ls='none', label=r"$\nu_{\mu}, terza armonica$", color="DarkGreen")
plt.scatter(dati.masse_lineari, dati.frequenze_corde, label=r"$\nu_{\mu}, terza armonica$", color="DarkGreen")
#plt.plot(dati.masse_lineari, dati.frequenze_corde, color="ForestGreen")

#grafico atteso
x = np.arange(0.0, 100., 0.0001)
cost = (3*np.sqrt(0.550504 * 9.81))/( 2 * 1.215 )     
y = cost/np.sqrt(x)
plt.plot(x, y)
plt.xlim(0.0, 0.01)
plt.ylim(35.0, 160.0)
plt.plot(x, y, label=r"$y = \frac{3\sqrt{9.81 m_{pesetto}}}{2 L}\frac{1}{\sqrt{x}}$", color="DarkOrange")
plt.xlabel('massa lineare (kg/m)', fontsize = 12)
plt.ylabel('frequenza (Hz)', fontsize = 12) 
plt.legend() # aggiungo una legenda
plt.grid()
plt.savefig('computed_data/grafico_parte4.png')
plt.show()
