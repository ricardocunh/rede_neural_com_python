# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 07:46:41 2020

@author: Ricardo Cunha
"""
 # Criando uma lista de entradas
entradas = [-1, 7, 5]
pesos = [0.8, 0.1, 0]

# criar uma função de soma (entrada e peso)
def soma(e, p):
    s = 0
    for i in range(3):
        #print(entradas[i])
        #print(pesos[i])
        
        # realizando a soma e a multiplicação
        s += e[i] * p[i]
    return s
        
s = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

r = stepFunction(s)



