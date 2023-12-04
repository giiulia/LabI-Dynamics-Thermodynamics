import numpy as np
from matplotlib import pyplot as plt
import dati
import math
from strumenti_utili_v4 import *

def grafici_intervalli(altezza, n, intervalli, colore):
    lista_t = []
    for i in intervalli:
        lista_t.append(np.mean(i))
    t = np.array(lista_t)
    print("in media gli intervalli per {} sono : {}".format(altezza, t))

    y = np.log10(t)

    lista_s_t = []
    for i in intervalli:
        lista_s_t.append(deviazione(i, np.mean(i))/np.sqrt(len(i)))
    s_t = np.array(lista_s_t)
    print("gli errori sui tempi sono : {}\n".format(s_t))

    s_y = s_t*np.log10(np.e)/t
    print("gli errori sulle y sono : {}\n".format(s_y))

    #disegno il grafico dei punti
    plt.errorbar(n, y, s_y, fmt='o', ls='none', label=altezza, color=colore)
    plt.scatter(n, y)
    plt.plot(n, y, color= colore)

    plt.xlim(0.0, 9.0)
    plt.ylim(-1.0, 1.0)


    plt.xlabel('numero rimbalzo', fontsize = 12)
    plt.ylabel('log($\Delta t$)', fontsize = 12) 
    
    plt.legend() # aggiungo una legenda

def calcolo_ev(altezza, x, intervalli, colore):
    lista_intervalli = []
    for i in intervalli:
        lista_intervalli.append(np.mean(i))
    y = np.array(lista_intervalli)
    #print("le y: {}".format(y))
    y = np.log10(y)

    lista_s_intervalli = []
    for i in intervalli:
        lista_s_intervalli.append(deviazione(i, np.mean(i))/np.sqrt(len(i)))
    s_y = np.array(lista_s_intervalli)
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

    #disegno la retta 
    plt.xlim(0.0, 9.0)
    plt.ylim(-1.0, 1.0)

    plt.xlabel('numero rimbalzo', fontsize = 12)
    plt.ylabel('log($\Delta t$)', fontsize = 12) 

    xmin = 0
    xmax = 11

    t = np.linspace(xmin,xmax) # stessa funzione ad alta densità
    plt.plot(t,line(t,coefficiente, intercetta),label=r"$y = {0:.2f}x{1:.2f}$".format(coefficiente, intercetta), color="CadetBlue")
    plt.scatter(x, y, color=colore)

    plt.legend() # aggiungo una legenda

    #calcolo ev e sigma ev
    ev = np.power(10, coefficiente)
    sigma_ev = np.power(10, coefficiente)*np.log(10)*sigma_B
    print('il coefficiente di restituzione per altezza di {}: ev = {}±{}\n\n'.format(altezza, ev, sigma_ev))

    ris = [ev, sigma_ev]
    return ris

def francesca(nome, altezze, intervalli, n):
    print("-"*10)
    print(nome)

    colors = ["FireBrick", "Gold", "MediumSlateBlue", "ForestGreen", "Orange"]
    i = 0
    for j in intervalli: #chiamo grafici_intervalli 4 o 5 volte a seconda della pallina
        grafici_intervalli(altezze[i], n, j, colors[i])
        i = i+1
    #grafici_intervalli(altezze[1], n, intervalli_h2, "Gold")
    #grafici_intervalli(altezze[2], n, intervalli_h3, "MediumSlateBlue")
    #grafici_intervalli(altezze[3], n, intervalli_h4, "ForestGreen")
    #grafici_intervalli(altezze[4], n, intervalli_h5, "Orange")

    #plt.savefig('computed_data/retta.pgf')
    plt.savefig('computed_data/graficoLog_{}.png'.format(nome)) #salvo tutti i grafici appena creati in una sola immagine
    plt.show()

    coefficienti = []

    i = 0
    for j in intervalli:
        coefficienti.append(calcolo_ev(altezze[i], n, j, colors[i]))
        i = i+1
    plt.savefig('computed_data/graficoLog_interpolato_{}.png'.format(nome))
    plt.show()
    #print(coefficienti)
    #ev_55 = calcolo_ev(55, n, intervalli_h2)
    #ev_45 = calcolo_ev(45, n, intervalli_h3)
    #ev_35 = calcolo_ev(35, n, intervalli_h4)
    #ev_25 = calcolo_ev(25, n, intervalli_h5)
    
    pesi = []
    ev = []
    for i in range(intervalli.shape[0]):
        ev.append(coefficienti[i][0])
        pesi.append(coefficienti[i][1])
    ev_magico = np.array(ev)
    pesi_magici = np.array(pesi)
    pesi_magici = np.power(1/pesi_magici, 2)

    media_pesata = sum(pesi_magici*ev_magico)/sum(pesi_magici)
    print("la media pesata dei coefficienti di restituzione è: {0:.4f}".format(media_pesata))

    incertezza_media = np.sqrt(1/sum(pesi_magici))
    print("l'incertezza sulla media pesata è: {0:.4f}".format(incertezza_media))

n1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
h1 = ["8cm", "10cm", "15cm", "18cm", "30cm"]
francesca("pallina1", h1, dati.pallina1_intervalli, n1)
n2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
h2 = ["65cm", "55cm", "45cm", "35cm", "25cm"]
francesca("pallina2", h2, dati.pallina2_intervalli, n2)
n3 = np.array([1, 2, 3, 4])
h3 = ["65cm", "55cm", "45cm", "35cm", "25cm"]
francesca("pallina3", h3, dati.pallina3_intervalli, n3)
n4 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
h4 = ["80cm", "90cm", "100cm", "110cm"]
francesca("pallina4", h4, dati.pallina4_intervalli, n4)