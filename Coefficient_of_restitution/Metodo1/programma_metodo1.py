import numpy as np
from matplotlib import pyplot as plt
import dati
import math
from strumenti_utili_v3 import *

#distribuzione dei dati
def grafico_punti(nome_dataset, dataset_h0, dataset_h1):
    print("-"*10)
    print(nome_dataset)

    lista_H0 = []
    for i in dataset_h0:
        lista_H0.append(np.mean(i))
    H0 = np.array(lista_H0)
    print("in media le altezze h0 sono : {}".format(H0))

    lista_H1 = []
    for i in dataset_h1:
        lista_H1.append(np.mean(i))
    H1 = np.array(lista_H1)
    print("in media le altezze h1 sono : {}".format(H1))

    lista_s_H1 = []
    for i in dataset_h1:
        lista_s_H1.append(deviazione(i, np.mean(i))/np.sqrt(len(i)))
    s_H1 = np.array(lista_s_H1)
    print("gli errori sulle h1 sono : {}".format(s_H1))

    #disegno il grafico dei punti
    #plt.errorbar(H0, H1, s_H1, fmt='o', ls='none', label='h1', color= "DarkSlateBlue")
    plt.scatter(H0, H1, label='h1', color= "DarkSlateBlue")
    #plt.plot(H0, H1, color= "CornflowerBlue")

    plt.xlim(0.0, 120.0)
    plt.ylim(0.0, 90.0)


    plt.xlabel('h0 (cm)')
    plt.ylabel('h1 (cm)') 

    plt.legend() # aggiungo una legenda
    #plt.savefig('computed_data/retta.pgf')
    plt.savefig('computed_data/punti_{}.png'.format(nome_dataset))
    plt.show()

#interpolazione dati
def retta_interpolata(nome_dataset, dataset_h0, dataset_h1):
    print("-"*10)
    print(nome_dataset)
    
    lista_H0 = []
    for i in dataset_h0:
        lista_H0.append(np.mean(i))
    x = np.array(lista_H0)
    print("le x: {}".format(x))

    lista_H1 = []
    for i in dataset_h1:
        lista_H1.append(np.mean(i))
    y = np.array(lista_H1)
    print("le y: {}".format(y))

    lista_s_H1 = []
    for i in dataset_h1:
        lista_s_H1.append(deviazione(i, np.mean(i))/np.sqrt(len(i)))
    s_y = np.array(lista_s_H1)
    print("le s_y: {}".format(s_y))

    #calcolo il coefficiente B
    pesi = 1/np.power(s_y, 2)
    delta = (sum(pesi*np.power(x, 2))*sum(pesi))-np.power(sum(pesi*x),2) 
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

    #calcolo sigma ev con la propagazione degli errori e il valore di ev
    sigma_ev = sigma_B/(2*np.sqrt(coefficiente))
    print("incertezza su ev: sigma_ev={}".format(sigma_ev))

    ev = np.sqrt(coefficiente)
    print('il coefficiente di restituzione: ev = {0:.3f}±{1:.3f} '.format(ev, sigma_ev))


    #disegno la retta 
    plt.errorbar(x, y, s_y, fmt='o', ls='none', label='h1', color="OliveDrab")

    plt.xlim(left=0)
    plt.ylim(bottom=0)
    
    plt.xlabel('h0 (cm)')
    plt.ylabel('h1 (cm)') 

    xmin = 0
    xmax = max(x)+0.1*(max(x)-min(x))

    t = np.linspace(xmin,xmax) # stessa funzione ad alta densità
    plt.plot(t,line(t,coefficiente, intercetta),label=r"$y = {0:.2f}x+{1:.2f}$".format(coefficiente, intercetta), color="darkOrange")
    plt.plot(t,line(t,coefficiente, intercetta))
    plt.legend() # aggiungo una legenda
    #plt.savefig('computed_data/retta.pgf')
    plt.savefig('computed_data/interpolazione_{}.png'.format(nome_dataset))
    plt.show()

#test del chi quadro
def chi_sq(nome_dataset, dataset_h0, dataset_h1):
    print("-"*10)
    print(nome_dataset)
    
    lista_H0 = []
    for i in dataset_h0:
        lista_H0.append(np.mean(i))
    x = np.array(lista_H0)

    lista_H1 = []
    for i in dataset_h1:
        lista_H1.append(np.mean(i))
    y = np.array(lista_H1)

    lista_s_H1 = []
    for i in dataset_h1:
        lista_s_H1.append(deviazione(i, np.mean(i)))
    s_y = np.array(lista_s_H1)

    #calcolo il coefficiente B
    pesi = 1/np.power(s_y, 2)
    delta = (sum(pesi*np.power(x, 2))*sum(pesi))-np.power(sum(pesi*x),2) 
    coefficiente = ((sum(pesi)*sum(pesi*x*y))-(sum(pesi*x)*sum(pesi*y)))/delta

    #calcolo l'intercetta A 
    intercetta = ((sum(pesi*np.power(x,2))*sum(pesi*y))-(sum(pesi*x)*sum(pesi*x*y)))/delta

    #calcolo il chi quadro
    chi_quadro = sum(np.power(((y-intercetta-coefficiente*x)/s_y), 2))
    print("il chi quadro risulta: {0:.3f}".format(chi_quadro))

    #chi ridotto
    dof = x.size-2 #degrees of freedom
    chi_ridotto = chi_quadro/dof
    print("il chi quadro ridotto risulta: {0:.3f}, controllare la probabilità relativa a {1:.3f} gradi di libertà".format(chi_ridotto, dof))


#mostro i punti
grafico_punti("pallina1", dati.pallina1_H0, dati.pallina1_H1)
grafico_punti("pallina2", dati.pallina2_H0, dati.pallina2_H1)
grafico_punti("pallina3", dati.pallina3_H0, dati.pallina3_H1)
grafico_punti("pallina4", dati.pallina4_H0, dati.pallina4_H1)

#seleziono i dati per l'interpolazione
pallina1_H0 = np.delete(dati.pallina1_H0, [3, 4, 5], axis=0)
pallina1_H1 = np.delete(dati.pallina1_H1, [3, 4, 5], axis=0)
#pallina2_H0 = np.delete(dati.pallina2_H0, [2,3])
#pallina2_H1 = np.delete(dati.pallina2_H1, [2,3])
pallina3_H0 = np.delete(dati.pallina3_H0, [0, 1], axis=0)
pallina3_H1 = np.delete(dati.pallina3_H1, [0, 1], axis=0)
#pallina4_H0 = np.delete(dati.pallina4_H0, [7,8], axis=0)
#pallina4_H1 = np.delete(dati.pallina4_H1, [7,8], axis=0)

#mostro le rette interpolate
retta_interpolata("pallina1", dati.pallina1_H0, dati.pallina1_H1)
#retta_interpolata("pallina2", pallina2_H0, pallina2_H1)
retta_interpolata("pallina3", dati.pallina3_H0, dati.pallina3_H1)
retta_interpolata("pallina4", dati.pallina4_H0, dati.pallina4_H1)

#test del chi quadro
chi_sq("pallina1", dati.pallina1_H0, dati.pallina1_H1)
#chi_sq("pallina2", dati.pallina2_H0, dati.pallina2_H1)
chi_sq("pallina3", dati.pallina3_H0, dati.pallina3_H1)
chi_sq("pallina4", dati.pallina4_H0, dati.pallina4_H1)
