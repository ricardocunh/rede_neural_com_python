# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 07:37:26 2020

@author: Ricardo Cunha
"""
import numpy as np

# criando as entradas, primeira entrada, segunda, terceira e quarta
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([0, 0, 0,1])

# Exemplo utilizando o OR
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([0, 1, 1,1])

#exemplo utilizando o SHOR
entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidas = np.array([0, 1, 1,0])

# como estamos trabalhando com array, deve ser 0.0 se não retorna erros
pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.1

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            # abs é para não ficar com o valor negativo
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            # atualizações no peso
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Peso atualizado: '+ str(pesos[j]))
        print('Total de erros: ' + str(erroTotal))
treinar()
print('Rede neural treinada')
print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(entradas[2]))
print(calculaSaida(entradas[3]))
