# -*- coding: utf-8 -*-
'''
Created on Mar 25, 2014

@author: renan
'''
from cor import Cor


class Tabuleiro:
    '''
    5,0 5,1 5,2 5,3 5,4 5,5 5,6
    4,0 4,1 4,2 4,3 4,4 4,5 4,6
    3,0 3,1 3,2 3,3 3,4 3,5 3,6
    2,0 2,1 2,2 2,3 2,4 2,5 2,6
    1,0 1,1 1,2 1,3 1,4 1,5 1,6
    0,0 0,1 0,2 0,3 0,4 0,5 0,6

    '''
    
    celulas = []

    def __init__(self, linhas, colunas):
        self.celulas = [[Cor.BRANCO for _ in range(colunas)] for _ in range(linhas)]
        
    def inserirPeca(self, coluna, jogador):
        for linha in self.celulas:
            if linha[coluna] is Cor.BRANCO:
                linha[coluna] = jogador
                break
            
    def verificarVitoria(self, jogador):
        return False
    
    def verificarListaDeCelulas(self, lista, cor_do_jogador):
        contador_iguais = 0
        for cor_da_celula in lista:
            if cor_da_celula is cor_do_jogador:
                contador_iguais += 1
            else:
                contador_iguais = 0
        return contador_iguais >= 4
            
    def __str__(self):
        string_tabuleiro = ""
        for linha in self.celulas:
            string_tabuleiro = str(linha) + "\n" + string_tabuleiro
        return string_tabuleiro