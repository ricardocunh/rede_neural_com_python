# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 07:46:41 2020

@author: Ricardo Cunha
"""

import numpy as np

 # Criando uma lista de entradas
entradas = np.array([1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

# criar uma função de soma (entrada e peso)
def soma(e, p):
    # dot -> produto escalar (calculo de algebra) essa funçao é muito mais rápido que um for
    return e.dot(p)
        
s = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

r = stepFunction(s)



