import numpy as np
from matplotlib import pyplot as plt
import dati2
from strumenti_utili_v4 import *

#----------------PARTE1 senza rotazione ----------------
print("-----------parte1-----------")
coefficiente_atteso = (1/ (2*1.08) ) * np.sqrt( (dati2.pesetti[0]*9.81) / 0.00219691) #1.08 è la distanza tra i due vincoli della corda; 0.00219691 è la massa lineare della corda 1 (kg/m)
velocità_attesa = np.sqrt( (dati2.pesetti[0]*9.81) / 0.00219691)

#plt.errorbar(dati2.n, dati2.frequenze, 0.01, fmt='o', ls='none', label=r"$\nu_{n}$", color="FireBrick")
plt.scatter(dati2.n, dati2.frequenze, label=r"$\nu_{n}$", color="FireBrick")
#plt.plot(dati2.n, dati2.frequenze, color="Crimson")

#grafico atteso
x = np.arange(0.0, 100., 0.01)
cost = np.sqrt(9.81*0.2/0.00219691)/(2*1.08)
y = cost*x
plt.plot(x, y, label=r"$y = \frac{x}{2L}\sqrt{\frac{\tau}{\mu}}$", color="DarkTurquoise")

plt.xlim(0.0, 6.0)
plt.ylim(0.0, 80.0)

plt.xlabel('n')
plt.ylabel('frequenza (Hz)') 
plt.legend() # aggiungo una legenda
plt.grid()
plt.savefig('computed_data/grafico_parte1.png')
plt.show()


#interpolazione
x  = dati2.n
y = dati2.frequenze
s_y = 0.01

#calcolo del coefficiente
delta = ( x.size*sum(np.power(x, 2)) ) - np.power(sum(x), 2) 
coefficiente = ( (x.size*sum(x*y)) - (sum(x)*sum(y)) )/delta
intercetta = ( (sum(np.power(x, 2))*sum(y))-(sum(x)*sum(x*y)) )/delta
print("il coefficiente è: B={0:.3f} da confrontare con {1:.3f}".format(coefficiente, coefficiente_atteso))
print("l'intercetta è: A={0:.3f} ".format(intercetta))
plt.errorbar(x, y, s_y, fmt='o', ls='none', label='data')

plt.xlim(left=0)
plt.ylim(bottom=-10)

xmin = 0
xmax = max(x)+0.1*(max(x)-min(x))

t = np.linspace(xmin,xmax) # stessa funzione ad alta densità
plt.plot(t,line(t,coefficiente, intercetta),label=r"$y = {0:.2f}x{1:.2f}$".format(coefficiente, intercetta), color="darkOrange")
plt.xlabel("n")
plt.ylabel(r"$ \nu(Hz)$")
plt.legend() # aggiungo una legenda
plt.savefig('computed_data/retta_parte1.png')
plt.show()
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
print("coefficiente di correlazione lineare PARTE1: {}".format(r))
#----------------PARTE2 senza rotazione ----------------

print("-----------parte2-----------")
plt.scatter(dati2.Tensioni, dati2.frequenze_T, label=r"$\nu_{T}, seconda armonica$", color="DarkOrange")

x = np.arange(0.0, 100., 0.1)
cost = 1/( 1.08 * np.sqrt(0.00219691) )     
y = cost*np.sqrt(x)
plt.plot(x, y, label=r"$y = \frac{n}{2L\sqrt{\mu}}\sqrt{x}$", color="DarkTurquoise")

plt.xlim(0.0, 6.0)
plt.ylim(0.0, 50.0)

plt.xlabel('tensione (N)')
plt.ylabel('frequenza (Hz)') 
plt.legend() # aggiungo una legenda
plt.grid()
plt.savefig('computed_data/grafico_parte2.png')
plt.show()

#interpolazione
x  = np.sqrt(dati2.Tensioni)
y = dati2.frequenze_T
s_y = 0.01

#calcolo del coefficiente
delta = ( x.size*sum(np.power(x, 2)) ) - np.power(sum(x), 2) 
coefficiente = ( (x.size*sum(x*y)) - (sum(x)*sum(y)) )/delta
intercetta = ( (sum(np.power(x, 2))*sum(y))-(sum(x)*sum(x*y)) )/delta
print("il coefficiente è: B={0:.3f}".format(coefficiente))
print("l'intercetta è: A={0:.3f} ".format(intercetta))
sigma_B = np.sqrt( x.size/delta )*s_y
sigma_A = np.sqrt(sum(x**2)/delta)*0.01
print("l'incertezza su B è: sigma_B={}".format(sigma_B))
print("l'incertezza su A è: sigma_A={}".format(sigma_A))

plt.errorbar(x, y, s_y, fmt='o', ls='none', label='data')
plt.xlabel(r"$\tau(N)$")
plt.ylabel(r"$ \nu(Hz) $")
plt.xlim(left=0)
plt.ylim(bottom=-10)

xmin = 0
xmax = max(x)+0.1*(max(x)-min(x))

t = np.linspace(xmin,xmax) # stessa funzione ad alta densità
plt.plot(t,line(t,coefficiente, intercetta),label=r"$y = {0:.2f}x{1:.2f}$".format(coefficiente, intercetta), color="darkOrange")
plt.legend() # aggiungo una legenda
plt.savefig('computed_data/retta_parte2.png')
plt.show()

r = sum((x-np.mean(x))*(y-np.mean(y)))/np.sqrt(sum((x-np.mean(x))**2)*sum((y-np.mean(y))**2) )
print("coefficiente di correlazione lineare PARTE2: {}".format(r))
#----------------PARTE3 senza rotazione ----------------
print("---------parte3---------")
plt.scatter(dati2.Lunghezze, dati2.frequenze_L, label=r"$\nu_{L},terza armonica$", color="RebeccaPurple")

#grafico atteso
x = np.arange(0.0, 1.5, 0.001)
cost = (np.sqrt(9.81*0.55/0.00219691)*3)/2     
y = cost/x
plt.plot(x, y, label=r"$y = \frac{3}{2x}\sqrt{\frac{\tau}{\mu}}$", color="DarkTurquoise")

plt.xlim(1.0, 1.5)
plt.ylim(60.0, 75.0)

plt.xlabel('lunghezza (m)')
plt.ylabel('frequenza (Hz)') 
plt.legend() # aggiungo una legenda
plt.grid()
plt.savefig('computed_data/grafico_parte3.png')
plt.show()

#correggiamo l'errore sistematico
plt.scatter(dati2.Lunghezze_corrette, dati2.frequenze_L, label=r"$\nu_{L},terza armonica$", color="RebeccaPurple")

#grafico atteso
x = np.arange(0.0, 1.5, 0.001)
cost = (np.sqrt(9.81*0.55/0.00219691)*3)/2     
y = cost/x
plt.plot(x, y, label=r"$y = \frac{3}{2x}\sqrt{\frac{\tau}{\mu}}$", color="DarkTurquoise")

plt.xlim(1.0, 1.5)
plt.ylim(60.0, 75.0)

plt.xlabel('lunghezza (m)')
plt.ylabel('frequenza (Hz)') 
plt.legend() # aggiungo una legenda
plt.grid()
plt.savefig('computed_data/grafico_parte3_corretto.png')
plt.show()

#interpolazione
x = 1/dati2.Lunghezze_corrette
y = dati2.frequenze_L
s_y = 0.01

#calcolo del coefficiente
delta = ( x.size*sum(np.power(x, 2)) ) - np.power(sum(x), 2) 
coefficiente = ( (x.size*sum(x*y)) - (sum(x)*sum(y)) )/delta
intercetta = ( (sum(np.power(x, 2))*sum(y))-(sum(x)*sum(x*y)) )/delta
print("il coefficiente è: B={0:.3f}".format(coefficiente))
print("l'intercetta è: A={0:.3f} ".format(intercetta))
sigma_B = np.sqrt( x.size/delta )*s_y
sigma_A = np.sqrt(sum(x**2)/delta)*s_y
print("l'incertezza su B è: sigma_B={}".format(sigma_B))
print("l'incertezza su A è: sigma_A={}".format(sigma_A))

plt.errorbar(x, y, s_y, fmt='o', ls='none', label='data')
plt.xlabel(r"$\frac{1}{L}(\frac{1}{m})$")
plt.ylabel(r"$ \nu(Hz) $")
plt.xlim(left=0, right=1)
plt.ylim(bottom=-10, top=90)

xmin = 0
xmax = max(x)+0.1*(max(x)-min(x))

t = np.linspace(xmin,xmax) # stessa funzione ad alta densità
plt.plot(t,line(t,coefficiente, intercetta),label=r"$y = {0:.2f}x{1:.2f}$".format(coefficiente, intercetta), color="darkOrange")
plt.legend() # aggiungo una legenda
plt.savefig('computed_data/retta_parte3.png')
plt.show()

r = sum((x-np.mean(x))*(y-np.mean(y)))/np.sqrt(sum((x-np.mean(x))**2)*sum((y-np.mean(y))**2) )
print("coefficiente di correlazione lineare PARTE3: {}".format(r))

#----------------PARTE4 senza rotazione ----------------
print("---------parte4---------")
plt.scatter(dati2.masse_lineari, dati2.frequenze_corde, label=r"$\nu_{\mu}, terza armonica$", color="DarkGreen")

#grafico atteso
x = np.arange(0.0, 100., 0.0001)
cost = (3*np.sqrt(0.550504 * 9.81))/( 2 * 1.215 )     
y = cost/np.sqrt(x)
plt.plot(x, y)
plt.xlim(0.0, 0.01)
plt.ylim(35.0, 160.0)
plt.plot(x, y, label=r"$y = \frac{3\sqrt{9.81 m_{pesetto}}}{2 L}\frac{1}{\sqrt{x}}$", color="DarkOrange")

plt.xlim(0.0, 0.01)
plt.ylim(35.0, 160.0)

plt.xlabel('massa lineare (kg/m)')
plt.ylabel('frequenza (Hz)') 
plt.legend() # aggiungo una legenda
plt.grid()
plt.savefig('computed_data/grafico_parte4.png')
plt.show()

#interpolazione
x = 1/np.sqrt(dati2.masse_lineari)
print(x)
y = dati2.frequenze_corde
s_y = 0.01

#calcolo del coefficiente
delta = ( x.size*sum(np.power(x, 2)) ) - np.power(sum(x), 2) 
coefficiente = ( (x.size*sum(x*y)) - (sum(x)*sum(y)) )/delta
intercetta = ( (sum(np.power(x, 2))*sum(y))-(sum(x)*sum(x*y)) )/delta
print("il coefficiente è: B={}".format(coefficiente))
print("l'intercetta è: A={} ".format(intercetta))
sigma_B = np.sqrt( x.size/delta )*s_y
sigma_A = np.sqrt(sum(x**2)/delta)*s_y
print("l'incertezza su B è: sigma_B={}".format(sigma_B))
print("l'incertezza su A è: sigma_A={}".format(sigma_A))

plt.errorbar(x, y, s_y, fmt='o', ls='none', label='data')
plt.xlabel(r"$\frac{1}{\sqrt{\mu}} (\sqrt{\frac{m}{Kg}})$")
plt.ylabel(r"$ \nu(Hz) $")
plt.xlim(left=0, right=50)
plt.ylim(bottom=0, top=150)

xmin = 0
xmax = max(x)+0.1*(max(x)-min(x))

t = np.linspace(xmin,xmax) # stessa funzione ad alta densità
plt.plot(t,line(t,coefficiente, intercetta),label=r"$y = {0:.2f}x+{1:.2f}$".format(coefficiente, intercetta), color="darkOrange")
plt.legend() # aggiungo una legenda
plt.savefig('computed_data/retta_parte4.png')
plt.show()

r = sum((x-np.mean(x))*(y-np.mean(y)))/np.sqrt(sum((x-np.mean(x))**2)*sum((y-np.mean(y))**2) )
print("coefficiente di correlazione lineare PARTE4: {}".format(r))
