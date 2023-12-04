# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:48:29 2021

@author: giuly

funzioni utili per misurazioni e creazione di relazioni
mettere questo file nella stessa cartella del proprio programma,
poi scrivere al suo interno
from strumenti_utili_v1 import *
"""
import numpy as np
from matplotlib import pyplot as plt


"""deviazione standard
Parametri
a: <array magico numpy> - i dati
m: scalare - la media
Restituisce
scalare
"""
def deviazione(a, m):
        t = a-m
        t**=2
        sc = np.sum(t)/(t.size-1)
        dev = np.sqrt(sc)
        return dev


"""gaus
Parametri
x: <array magico numpy> - i dati
m: scalare - la media
s: scalare - la deviazione
Restituisce
<array magico>
"""
def gaus(x,m,s):
    h = 1.0/(s*np.sqrt(2))
    z = x-m
    return np.exp(-np.power(h*z, 2.)) *h / np.sqrt(np.pi)

"""retta
Parametri
x: <array magico numpy> - i dati
m: scalare - coefficiente angolare
q: scalare - l'intercetta'
Restituisce
<array magico>
"""
def line(x,m,q=0):
 y = m*x+q
 return y

"""chi quadro
Parametri
v: <array magico numpy> - i dati
m: scalare - la media
s: scalare - la deviazione
Restituisce
scalare
"""
def chi_sq(v, media, dev):
    incr_list = [0,0,0,0] #lista incrementale
    E = np.array([0.16, 0.34, 0.34, 0.16]) #array delle probabilità di una gaussiana

    for i in range(len(v)):
        if(v[i]<=(media-dev)):
            incr_list[0] = incr_list[0]+1
        elif((v[i]>(media-dev)) and (v[i]<=media)):
            incr_list[1] = incr_list[1]+1
        elif((v[i]>media) and (v[i]<(media+dev))):
            incr_list[2] = incr_list[2]+1
        else:
            incr_list[3] = incr_list[3]+1

    O = np.array(incr_list) #array con il numero delle misure osservate per ogni intervallo
    print(O)
    E *= len(v) #array dei valori attesi per O
    print(E)

    chi_sq = sum(np.power((O-E), 2.0)/E)
    return chi_sq



"""crea una tabella .tex importabile tramite il comando
   \input{nomefile.tex}
Parametri
dati: array magico o lista - i dati
colonne: intero - il numero di colonne che deve avere la tabella
percorso: stringa - dove salvare il file. esepio: computed_data/tabella1.tex
template: stringa, opzionale - una stringa contenente il codice latex della tabella che
                               si vuole utilizzare. deve contenere un %d e un %s, che saranno
                               sostituiti con il numero di colonne e con i dati formattati.
                               Alternativamente, è possibile passare il nome di un template ,tra 
                               quelli definiti nella funzione. se non si passa nulla, il template
                               "semplice" verrà utilizzato
Restituisce
nulla
"""
def crea_tabella(dati, colonne, percorso, template="semplice"):
    #template per tabelle centrate, anche se molto lunghe che escono dal margine
    #richiede questo header \usepackage{graphicx}
    #https://tex.stackexchange.com/a/360788
    if(template=="centrata"):
        template = r"""
        \begin{figure}[!h]
            \makebox[1 \textwidth][c]{
                \begin{tabular}{*{%d}{c}}
                    \hline
                    \hline
                        %s
                    \hline
                    \hline
                \end{tabular}
            } 
        \end{figure}
        """
    #template per tabella semplice, utile se si vuole scrivere tutto il codice che circonda la tabella
    #dentro al documento latex
    if(template=="semplice"):
        template = r"""
        \begin{tabular}{*{%d}{c}}
            \hline
            \hline
                %s
            \hline
            \hline
        \end{tabular}
        """
    #formatta i dati
    content = ""
    for i in range(0, len(dati)):
        #se i è un multiplo di colonne, inserisci l'acapo
        if((i+1)%(colonne) == 0):
            content += r"""{} \\
            \hline
            """.format(dati[i])
        #altrimenti metti l'elemento nella stessa riga
        else:
            content += "{} & ".format(dati[i])
            if(i == len(dati)-1):
                content += r"\\"
    #crea il file
    fileOutput = template % (colonne, content)
    f = open(percorso, "w")
    f.write(fileOutput)
    f.close()




