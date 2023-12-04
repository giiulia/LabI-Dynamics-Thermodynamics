import numpy as np
from matplotlib import pyplot as plt
from sympy import *
import dati
from strumenti_utili_v4 import *

print("-------------parte 1-------------")
angoli_parte1 = np.array([
    np.mean(dati.alpha_1),
    np.mean(dati.alpha_2),
    np.mean(dati.alpha_3),
    np.mean(dati.alpha_4),
    np.mean(dati.alpha_5),
    np.mean(dati.alpha_6)
])

deviazioni_parte1 = np.array([
    deviazione(dati.alpha_1, np.mean(dati.alpha_1)),
    deviazione(dati.alpha_2, np.mean(dati.alpha_2)),
    deviazione(dati.alpha_3, np.mean(dati.alpha_3)),
    deviazione(dati.alpha_4, np.mean(dati.alpha_4)),
    deviazione(dati.alpha_5, np.mean(dati.alpha_5)),
    deviazione(dati.alpha_6, np.mean(dati.alpha_6))
])
errori_parte1 = deviazioni_parte1/np.sqrt(5) #errori sulle medie
print("le medie degli angoli non corretti per la parte 1 sono: {}".format(angoli_parte1))
print("gli errori sulle medie non corrette per la parte 1 sono: {}".format(errori_parte1))

#correzione di teta
R = 1.9/100 #raggio delle sfere = 1.9cm
r = dati.distanze 
B = 1-(4*((R/r)**3))
angoli_parte1 = angoli_parte1/B
print("le medie degli angoli corretti per la parte 1 sono: {}".format(angoli_parte1))
errori_parte1 = errori_parte1/B
print("gli errori sulle medie corrette per la parte 1 sono: {}".format(errori_parte1))

#grafico1
r_reciproco = np.power(1/r, 2)
plt.errorbar(r_reciproco, angoli_parte1, errori_parte1, fmt='o', ls='none', label=r"$\theta_{(\frac{1}{r^{2}})}$", color="SkyBlue")
plt.scatter(r_reciproco, angoli_parte1)
#plt.plot(r_reciproco, angoli_parte1, color="PowderBlue")

#x = np.arange(0.0, 650.0, 0.1)
#cost = (np.power(6000*0.019, 2)*4*np.pi*0.00000000000885)/( 0.00000725 ) #Ktor = 0.00000725    
#y = cost*x
#plt.plot(x, y)

plt.xlim(15.0, 650.0)
plt.ylim(-35.0, 200.0)

plt.xlabel(r'$\frac{1}{r^{2}} (m^{-2})$')
plt.ylabel(r'$\theta (deg)$') 
plt.legend() # aggiungo una legenda
plt.savefig('computed_data/grafico1.png')
plt.show()

#test della dipendenza lineare
ccl = sum( (r_reciproco-np.mean(r_reciproco) )*( angoli_parte1-np.mean(angoli_parte1) ) )/np.sqrt(sum(np.power(r_reciproco-np.mean(r_reciproco), 2)) * sum(np.power(angoli_parte1-np.mean(angoli_parte1), 2)) ) #coefficiente di correlazione lineare
print("il coefficiente di correlazione lineare per la parte 1 è :{}".format(ccl))

print("-------------parte 2a-------------")
angoli_parte2a = np.array([
    np.mean(dati.beta_1),
    np.mean(dati.beta_2),
    np.mean(dati.beta_3),
    np.mean(dati.beta_4),
    np.mean(dati.beta_5),
    np.mean(dati.beta_6),
    np.mean(dati.beta_7),
    np.mean(dati.beta_8),
    np.mean(dati.beta_9)
])

deviazioni_parte2a = np.array([
    deviazione(dati.beta_1, np.mean(dati.beta_1)),
    deviazione(dati.beta_2, np.mean(dati.beta_2)),
    deviazione(dati.beta_3, np.mean(dati.beta_3)),
    deviazione(dati.beta_4, np.mean(dati.beta_4)),
    deviazione(dati.beta_5, np.mean(dati.beta_5)),
    deviazione(dati.beta_6, np.mean(dati.beta_6)),
    deviazione(dati.beta_7, np.mean(dati.beta_7)),
    deviazione(dati.beta_8, np.mean(dati.beta_8)),
    deviazione(dati.beta_9, np.mean(dati.beta_9))
])
errori_parte2a = deviazioni_parte2a/np.sqrt(9) #errori sulle medie

print("le medie degli angoli non corretti per la parte 2a sono: {}".format(angoli_parte2a))
print("gli errori sulle medie non corrette per la parte 2a sono: {}".format(errori_parte2a))

#correzione di teta
R = 1.9/100 #raggio delle sfere = 1.9cm
r = 0.08 
B = 1-(4*((R/r)**3))
angoli_parte2a = angoli_parte2a/B
print("le medie degli angoli corretti per la parte 2a sono: {}".format(angoli_parte2a))
errori_parte2a = errori_parte2a/B
print("gli errori sulle medie corrette per la parte 2a sono: {}".format(errori_parte2a))

#grafico2
potenziale = dati.V

plt.errorbar(potenziale, angoli_parte2a, errori_parte2a, fmt='o', ls='none', label=r"$\theta_{(V)}$", color="Salmon")
plt.scatter(potenziale, angoli_parte2a)
#plt.plot(potenziale, angoli_parte2a, color="LightCoral")

#x = np.arange(2000.0, 6000.0, 0.1)
#cost = (np.power(0.019, 2)*4*np.pi*0.00000000000885)/( np.power(0.08, 2)*0.00000725 ) #Ktor = 0.00000725    
#y = cost*np.power(x, 2)
#plt.plot(x, y)

plt.xlim(1900.0, 6050.0)
plt.ylim(-35.0, 40.0)

plt.xlabel(r'$V (Volt)$')
plt.ylabel(r'$\theta (deg)$') 
plt.legend() # aggiungo una legenda
plt.savefig('computed_data/grafico2.png')
plt.show()

#coefficiente di correlazione lineare
x  = dati.V**2
y = angoli_parte2a

r = sum((x-np.mean(x))*(y-np.mean(y)))/np.sqrt(sum((x-np.mean(x))**2)*sum((y-np.mean(y))**2) )
print("coefficiente di correlazione lineare PARTE2a: {}".format(r))

print("-------------parte 2b-------------")
angoli_parte2b = np.array([
    np.mean(dati.theta_1),
    np.mean(dati.theta_2),
    np.mean(dati.theta_3),
    np.mean(dati.theta_4),
    np.mean(dati.theta_5),
    np.mean(dati.theta_6),
    np.mean(dati.theta_7),
    np.mean(dati.theta_8),
    np.mean(dati.theta_9)
])

deviazioni_parte2b = np.array([
    deviazione(dati.theta_1, np.mean(dati.theta_1)),
    deviazione(dati.theta_2, np.mean(dati.theta_2)),
    deviazione(dati.theta_3, np.mean(dati.theta_3)),
    deviazione(dati.theta_4, np.mean(dati.theta_4)),
    deviazione(dati.theta_5, np.mean(dati.theta_5)),
    deviazione(dati.theta_6, np.mean(dati.theta_6)),
    deviazione(dati.theta_7, np.mean(dati.theta_7)),
    deviazione(dati.theta_8, np.mean(dati.theta_8)),
    deviazione(dati.theta_9, np.mean(dati.theta_9))
])
errori_parte2b = deviazioni_parte2b/np.sqrt(9) #errori sulle medie

print("le medie degli angoli non corretti per la parte 2b sono: {}".format(angoli_parte2b))
print("gli errori sulle medie non corrette per la parte 2b sono: {}".format(errori_parte2b))


angoli_parte2b = angoli_parte2b/B
print("le medie degli angoli corretti per la parte 2b sono: {}".format(angoli_parte2b))
errori_parte2b = errori_parte2b/B
print("gli errori sulle medie corrette per la parte 2b sono: {}".format(errori_parte2b))

#grafico3
plt.errorbar(potenziale, angoli_parte2b, errori_parte2b, fmt='o', ls='none', label=r"$\theta_{(V2)}$", color="Khaki")
plt.scatter(potenziale, angoli_parte2b)
#plt.plot(potenziale, angoli_parte2b, color="PaleGoldenrod")

#x = np.arange(2000.0, 6000.0, 0.1)
#cost = (6000*np.power(0.019, 2)*4*np.pi*0.00000000000885)/( np.power(0.08, 2)*0.00000725 ) #Ktor = 0.00000725    
#y = cost*x
#plt.plot(x, y)

plt.xlim(1900.0, 6050.0)
plt.ylim(-35.0, 40.0)

plt.xlabel(r'$V2 (Volt)$')
plt.ylabel(r'$\theta (deg)$') 
plt.legend() # aggiungo una legenda
plt.savefig('computed_data/grafico3.png')
plt.show()

#test della dipendenza lineare
ccl = sum( (potenziale-np.mean(potenziale) )*( angoli_parte2b-np.mean(angoli_parte2b) ) )/np.sqrt(sum(np.power(potenziale-np.mean(potenziale), 2)) * sum(np.power(angoli_parte2b-np.mean(angoli_parte2b), 2)) ) #coefficiente di correlazione lineare
print("il coefficiente di correlazione lineare per la parte 2b è :{}".format(ccl))

print("-------------parte 3-------------")
angoli_parte3 = np.array([
    np.mean(dati.gamma_1),
    np.mean(dati.gamma_2),
    np.mean(dati.gamma_3),
    np.mean(dati.gamma_4),
    np.mean(dati.gamma_5)
])
print("le medie degli angoli per la parte 3 sono: {}".format(angoli_parte3))

deviazioni_parte3 = np.array([
    deviazione(dati.gamma_1, np.mean(dati.gamma_1)),
    deviazione(dati.gamma_2, np.mean(dati.gamma_2)),
    deviazione(dati.gamma_3, np.mean(dati.gamma_3)),
    deviazione(dati.gamma_4, np.mean(dati.gamma_4)),
    deviazione(dati.gamma_5, np.mean(dati.gamma_5))
])
errori_parte3 = deviazioni_parte3/np.sqrt(5) #errori sulle medie
print("gli errori sulle medie per la parte 3 sono: {}".format(errori_parte3))

#grafico4
massa = dati.m

plt.errorbar(massa, angoli_parte3, errori_parte3, fmt='o', ls='none', label=r"$\theta_{(m)}$", color="Orchid")
plt.scatter(massa, angoli_parte3)
#plt.plot(massa, angoli_parte3, color="Plum")

#x = np.arange(0.0, 0.0001, 0.000001)
#cost = 9.81/0.00000725 #Ktor = 0.00000725    
#y = cost*x
#plt.plot(x, y)

plt.xlim(0.0, 0.0001)
plt.ylim(23.0, 150.0)

plt.xlabel(r'$m (kg)$')
plt.ylabel(r'$\theta (deg)$') 
plt.legend() # aggiungo una legenda
plt.savefig('computed_data/grafico4.png')
plt.show()

#interpolazione
x  = dati.m
y = angoli_parte3
s_y = errori_parte3

#calcolo del coefficiente
pesi = 1/np.power(s_y,2)
#print(sum(pesi))
delta = (sum(pesi)*sum(pesi*np.power(x,2)))-(np.power(sum(pesi*x),2)) 
coefficiente = ((sum(pesi)*sum(pesi*x*y))-(sum(pesi*x)*sum(pesi*y)))/delta

print("il coefficiente è: B={0:.3f}".format(coefficiente))

#calcolo l'intercetta A 
intercetta = ((sum(pesi*np.power(x,2))*sum(pesi*y))-(sum(pesi*x)*sum(pesi*x*y)))/delta

print("l'intercetta è: A={} dunque non posso trascurarla".format(intercetta))

#calcolo sigma intercetta
sigma_A = np.sqrt(sum(pesi*np.power(x, 2)))/np.sqrt(delta)
print("l'incertezza su A è: sigma_A={}".format(sigma_A))

#calcolo sigma coefficiente
sigma_B = np.sqrt(sum(pesi))/np.sqrt(delta)
print("l'incertezza su B è: sigma_B={}".format(sigma_B))

#calcolo sigma Ktor con la propagazione degli errori e il valore di Ktor
sigma_Ktor = (9.81*sigma_B)/np.power(coefficiente, 2)
print("incertezza su Ktor: sigma_Ktor={}".format(sigma_Ktor))

Ktor = 9.81/coefficiente
print('Ktor: = {0:.8f}±{1:.8f} '.format(Ktor, sigma_Ktor))

#interpolazione dei dati e retta
plt.errorbar(x, y, s_y, fmt='o', ls='none', label='data')

plt.xlim(left=0)
plt.ylim(bottom=0)

xmin = 0
xmax = max(x)+0.1*(max(x)-min(x))

t = np.linspace(xmin,xmax) # stessa funzione ad alta densità
plt.plot(t,line(t,coefficiente, intercetta),label="y = {0:.2f}x{1:.2f}".format(coefficiente, intercetta), color="darkOrange")
#plt.plot(t,line(t,coefficiente, intercetta))
plt.legend() # aggiungo una legenda
#plt.savefig('computed_data/retta.pgf')
plt.savefig('computed_data/retta.png')
plt.show()


print("-------------calcolo epsilon zero con 1-------------")
#calcolo della costante dielettrica nel vuoto con la parte 1
teta = angoli_parte1
sigma_teta = errori_parte1

r = dati.distanze
sigma_r = 0.001

a = 0.019 #raggio delle sfere in m
sigma_a = 0.001

V = np.array([6000, 6000, 6000, 6000, 6000, 6000])
sigma_V = 100

epsilon_zero_1 = (Ktor*teta*np.power(r, 2))/(4*np.pi*np.power(a, 2)*(V**2))

#prepara calcolo simbolico per generare derivate
_teta, _a, _r, _Ktor, _V = symbols('_teta _a _r _Ktor _V', real=True) #raggio sferette
formula_funzione = (_Ktor*_teta*(_r**2))/(4*pi*(_a**2)*(_V**2))

#genera uno scalare a partire dalla formula simbolica scritta sopra
def genera_derivata(incognita):
    formula_derivata = diff(formula_funzione, incognita)
    arrmagico = np.array([])
    for i in range(len(teta)):
        scalare = formula_derivata.subs([(_teta, teta[i]), (_a, a), (_r, r[i]), (_Ktor, Ktor), (_V, V[i])])
        arrmagico = np.append(arrmagico, [scalare.evalf()])
    return arrmagico

derivata_Ktor = genera_derivata(_Ktor)
derivata_teta = genera_derivata(_teta)
derivata_r = genera_derivata(_r)
derivata_a = genera_derivata(_a)
derivata_V = genera_derivata(_V)

sigma_epsilon_zero_1 = (( np.power(derivata_Ktor, 2)*np.power(sigma_Ktor, 2) ) + ( np.power(derivata_teta, 2)*np.power(sigma_teta, 2) ) + ( np.power(derivata_r, 2)*np.power(sigma_r, 2) ) + ( np.power(derivata_a, 2)*np.power(sigma_a, 2) ) + ( np.power(derivata_V, 2)*np.power(sigma_V, 2) ))
sigma_epsilon_zero_1 = sigma_epsilon_zero_1.astype(float)
sigma_epsilon_zero_1 = np.sqrt(sigma_epsilon_zero_1)

pesi_1 = 1/np.power(sigma_epsilon_zero_1, 2) 

media_pesata_1 = sum(pesi_1*epsilon_zero_1)/sum(pesi_1)
print("la media pesata delle costanti dielettriche con 1 è: {}".format(media_pesata_1))

incertezza_media_1 = np.sqrt(1/sum(pesi_1))
print("l'incertezza sulla media pesata  con 1 è: {}".format(incertezza_media_1))


#calcolo della costante dielettrica nel vuoto con la parte 2a
print("-------------calcolo epsilon zero con 2a-------------")
teta = angoli_parte2a
sigma_teta = errori_parte2a

r = np.array([0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08]) #distanza tra le sfere in m costante
sigma_r = 0.001

a = 0.019 #raggio delle sfere in m
sigma_a = 0.001

V = dati.V
sigma_V = 100

epsilon_zero_2a = (Ktor*teta*np.power(r, 2))/(4*np.pi*np.power(a, 2)*np.power(V, 2))

derivata_Ktor = genera_derivata(_Ktor)
derivata_teta = genera_derivata(_teta)
derivata_r = genera_derivata(_r)
derivata_a = genera_derivata(_a)
derivata_V = genera_derivata(_V)

sigma_epsilon_zero_2a = (( np.power(derivata_Ktor, 2)*np.power(sigma_Ktor, 2) ) + ( np.power(derivata_teta, 2)*np.power(sigma_teta, 2) ) + ( np.power(derivata_r, 2)*np.power(sigma_r, 2) ) + ( np.power(derivata_a, 2)*np.power(sigma_a, 2) ) + ( np.power(derivata_V, 2)*np.power(sigma_V, 2) ))
sigma_epsilon_zero_2a = sigma_epsilon_zero_2a.astype(float)
sigma_epsilon_zero_2a = np.sqrt(sigma_epsilon_zero_2a)

pesi_2a = 1/np.power(sigma_epsilon_zero_2a, 2) 

media_pesata_2a = sum(pesi_2a*epsilon_zero_2a)/sum(pesi_2a)
print("la media pesata delle costanti dielettriche con 2a è: {}".format(media_pesata_2a))

incertezza_media_2a = np.sqrt(1/sum(pesi_2a))
print("l'incertezza sulla media pesata con 2a è: {}".format(incertezza_media_2a))

print("-------------calcolo epsilon zero con 2b-------------")
#calcolo della costante dielettrica nel vuoto con la parte 2b
teta = angoli_parte2b
sigma_teta = errori_parte2b

r = np.array([0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08]) #distanza tra le sfere in m costante
sigma_r = 0.001

a = 0.019 #raggio delle sfere in m
sigma_a = 0.001

V = dati.V
sigma_V = 100

epsilon_zero_2b = (Ktor*teta*np.power(r, 2))/(4*np.pi*np.power(a, 2)*6000*V)

derivata_Ktor = genera_derivata(_Ktor)
derivata_teta = genera_derivata(_teta)
derivata_r = genera_derivata(_r)
derivata_a = genera_derivata(_a)
derivata_V = genera_derivata(_V)

sigma_epsilon_zero_2b = (( np.power(derivata_Ktor, 2)*np.power(sigma_Ktor, 2) ) + ( np.power(derivata_teta, 2)*np.power(sigma_teta, 2) ) + ( np.power(derivata_r, 2)*np.power(sigma_r, 2) ) + ( np.power(derivata_a, 2)*np.power(sigma_a, 2) ) + ( np.power(derivata_V, 2)*np.power(sigma_V, 2) ))
sigma_epsilon_zero_2b = sigma_epsilon_zero_2b.astype(float)
sigma_epsilon_zero_2b = np.sqrt(sigma_epsilon_zero_2b)
print(sigma_epsilon_zero_2b)

pesi_2b = 1/np.power(sigma_epsilon_zero_2b, 2) 

media_pesata_2b = sum(pesi_2b*epsilon_zero_2b)/sum(pesi_2b)
print("la media pesata delle costanti dielettriche per 2b è: {}".format(media_pesata_2b))

incertezza_media_2b = np.sqrt(1/sum(pesi_2b))
print("l'incertezza sulla media pesata per 2b è: {}".format(incertezza_media_2b))

#media pesata delle epsilon zero ottenute coi 3 metodi:
epsilon_zero = np.array([media_pesata_1, media_pesata_2a, media_pesata_2b])
sigma_epsilon_zero = np.array([incertezza_media_1, incertezza_media_2a, incertezza_media_2b])

pesi = 1/np.power(sigma_epsilon_zero, 2)
media_pesata = sum(pesi*epsilon_zero)/sum(pesi)
print("la media pesata delle costanti dielettriche TOTALE è: {}".format(media_pesata))

incertezza_media = np.sqrt(1/sum(pesi))
print("l'incertezza sulla media pesata TOTALE è: {}".format(incertezza_media))