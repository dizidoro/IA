# -*- coding: utf-8 -*-
'''
Created on Mar 25, 2014

@author: renan
'''
from jogador import Jogador
from jogada import Jogada
import numpy as np


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
        self.celulas = [[Jogador.VAZIO for _ in range(colunas)] for _ in range(linhas)]
        
    def inserirPeca(self, coluna, jogador):
        for indice, linha in enumerate(self.celulas): 
            if linha[coluna] is Jogador.VAZIO:
                linha[coluna] = jogador
                return indice
            
    def verificarVitoria(self, jogada):
        # verificar linha
        if Tabuleiro.listaTem4Conectados(self.celulas[jogada.linha], jogada.jogador):
            return True
        
        # verificar coluna
        coluna = []
        for linha in self.celulas:
            coluna.append(linha[jogada.coluna])
        if Tabuleiro.listaTem4Conectados(coluna, jogada.jogador):
            return True

        # verificar diagonais
        diagonais = self.obterDiagonais()
        diagonal_principal = diagonais[jogada.linha + jogada.coluna]
        diagona_secundaria = diagonais[len(diagonais) / 2 + jogada.linha + jogada.coluna]
        return Tabuleiro.listaTem4Conectados(diagonal_principal, jogada.jogador) or Tabuleiro.listaTem4Conectados(diagona_secundaria, jogada.jogador)
    
    @staticmethod
    def listaTem4Conectados(lista, jogador):
        contador_iguais = 0
        for celula in lista:
            if celula is jogador:
                contador_iguais += 1
            else:
                contador_iguais = 0

            if contador_iguais >= 4:
                return True

        return False
    
    def utilidade(self, jogada):
        fator_vitoria = 100
        fator_3_de_quatro = 10

        utilidade = 0;
        vitoria = self.verificarVitoria(jogada)
        if vitoria:
            if jogada.jogador is Jogador.HUMANO:
                utilidade -= fator_vitoria
            else
                utilidade += fator_vitoria

        utilidade -= self.numeroDeTresDasQuatro(Jogador.HUMANO) * fator_3_de_quatro
        utilidade += self.numeroDeTresDasQuatro(Jogador.COMPUTADOR) * fator_3_de_quatro

        return utilidade


    def numeroDeTresDasQuatro(self, jogador):
        # verificar linha
        numero_de_tres = 0
        for linha in self.celulas:
            numero_de_tres += Tabuleiro.numeroDeTresDasQuatroDaLista(linha, jogador)
        
        # verificar coluna
        for i in range(7):
            coluna = []
            for linha in self.celulas:
                coluna.append(linha[i])
            numero_de_tres += Tabuleiro.numeroDeTresDasQuatroDaLista(coluna, jogador)

        # verificar diagonais
        diagonais = self.obterDiagonais()
        for diagonal in diagonais:
            numero_de_tres += Tabuleiro.numeroDeTresDasQuatroDaLista(diagonal, jogador)

        return numero_de_tres

    @staticmethod
    def numeroDeTresDasQuatroDaLista(lista, jogador):
        numero_de_tres = 0
        contador = 0
        passou_por_zero = False
        for celula in lista:
            if celula == jogador:
                contador +=1
                if contador == 3:
                    numero_de_tres +=1
                    contador = 1
                    passou_por_zero = False
            elif celula == 0:
                if passou_por_zero:
                    contador = 0
                    passou_por_zero = False
                else:
                    passou_por_zero = True
            else:
                contador = 0

        return numero_de_tres

    def obterDiagonais(self):
        a = np.array(self.celulas)
        diags = [a[::-1, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]
        diags.extend(a.diagonal(i) for i in range(a.shape[1] - 1, -a.shape[0], -1))
        diagonais = [n.tolist() for n in diags]
        return diagonais

    def __str__(self):
        string_tabuleiro = ""
        for linha in self.celulas:
            string_tabuleiro = str(linha) + "\n" + string_tabuleiro
        return string_tabuleiro
