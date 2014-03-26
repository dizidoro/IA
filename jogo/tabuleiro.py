# -*- coding: utf-8 -*-
'''
Created on Mar 25, 2014

@author: renan
'''
from cor import Cor
from jogada import Jogada


class Tabuleiro:
    '''
    5,0 5,1 5,2 5,3 5,4 5,5 5,6
    4,0 4,1 4,2 4,3 4,4 4,5 4,6
    3,0 3,1 3,2 3,3 3,4 3,5 3,6
    2,0 2,1 2,2 2,3 2,4 2,5 2,6
    1,0 1,1 1,2 1,3 1,4 1,5 1,6
    0,0 0,1 0,2 0,3 0,4 0,5 0,6

    '''

    def __init__(self, linhas, colunas):
        self.celulas = [[Cor.BRANCO for _ in range(colunas)] for _ in range(linhas)]
        
    def inserirPeca(self, coluna, jogador):
        for indice, linha in enumerate(self.celulas): 
            if linha[coluna] is Cor.BRANCO:
                linha[coluna] = jogador
                return indice
            
    def verificarVitoria(self, jogada):
        #verificar linha
        if self.listaTem4Conectados(self.celulas[jogada.linha], jogada.jogador):
            return True
        #for linha in self.celulas
        #verificar coluna

        #verificar diagonais
        return False
    
    def listaTem4Conectados(self, lista, jogador):
        contador_iguais = 0
        for celula in lista:
            if celula is jogador:
                contador_iguais += 1
            else:
                contador_iguais = 0

            if contador_iguais >=4:
                return True

        return False
            
    def diagonais():
        a = np.array(self.celulas)
        diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
        diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))
        diagonais = [n.tolist() for n in diags]
        return diagonais

    def __str__(self):
        string_tabuleiro = ""
        for linha in self.celulas:
            string_tabuleiro = str(linha) + "\n" + string_tabuleiro
        return string_tabuleiro
