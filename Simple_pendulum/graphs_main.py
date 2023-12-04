#!/usr/bin/python
# prg. writeFile.py
# 18-03-2014 ByteMan OpenWeb
# Scrittura dati su file

import numpy as np
import pylab as pl

#grafico1
x = np.arange(0.0, 100., 0.1)
cost1 = 2          # Interi tra 0 e 100 con intervallo 0.5
y = cost1*np.sqrt(x)                              # Quadrati dei valori di x


pl.plot(x, y, 'g')                   # Assegnazione x,y e colore
pl.xlabel(r'$l$', fontsize=25)
pl.ylabel('T', fontsize=25)
pl.xlim(0.0, 10.)
pl.grid()
pl.savefig('computed_data/grafico1.png')
pl.show()

#grafico2
x = np.arange(-100.0, 100., 0.1)
cost2 = 0.696          # Interi tra 0 e 100 con intervallo 0.5
y = cost2+(1/2)*(x)                              # Quadrati dei valori di x


pl.plot(x, y, 'g')                   # Assegnazione x,y e colore
pl.xlabel(r'$\ln{l}$', fontsize=25)
pl.ylabel(r'$\ln{T}$', fontsize=25)
pl.xlim(0.0, 10.)
pl.ylim(0.0, 10.)
pl.grid()
pl.savefig('computed_data/grafico2.png')
pl.show()

#grafico3
x = np.arange(-100.0, 100., 0.1)
cost3 = 4.02          # Interi tra 0 e 100 con intervallo 0.5
y = cost3*(x)                              # Quadrati dei valori di x

pl.plot(x, y, 'g')                   # Assegnazione x,y e colore
pl.xlabel(r'l', fontsize=25)
pl.ylabel(r'$T^{2}$', fontsize=25)
pl.xlim(0.0, 10.)
pl.ylim(0.0, 10.0)
pl.grid()
pl.savefig('computed_data/grafico3.png')
pl.show()