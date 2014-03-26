# -*- coding: utf-8 -*-
'''
Created on Mar 25, 2014

@author: renan
'''
from cor import Cor

class Tabuleiro:
    
    celulas = []

    def __init__(self, linhas, colunas):
        self.celulas = [[Cor.BRANCO for _ in range(colunas)] for _ in range(linhas)]
        
    def inserirPeca(self, coluna, jogador):
        for linha in self.celulas:
            if linha[coluna]==Cor.BRANCO:
                linha[coluna]=jogador
                return
            
    def verificarVitoria(self, jogador):
        return False
    
    def verificarCondicaoVitoria(self, lista, jogador):
        contador_iguais = 0
        for celula in lista:
            if (celula==jogador):
                contador_iguais += 1
            else:
                contador_iguais = 0
        return contador_iguais >= 4
            
    def __str__(self):
        string_tabuleiro = ""
        for linha in self.celulas:
            string_tabuleiro = str(linha) + "\n" + string_tabuleiro
        return string_tabuleiro