# -*- coding: utf-8 -*-
'''
Created on Mar 25, 2014

@author: renan
'''
from jogador import Jogador
from jogada import Jogada
from bcolors import BColors

# import numpy as np
# from diagonal import Diagonal


class Tabuleiro:
    '''
    5,0 5,1 5,2 5,3 5,4 5,5 5,6
    4,0 4,1 4,2 4,3 4,4 4,5 4,6
    3,0 3,1 3,2 3,3 3,4 3,5 3,6
    2,0 2,1 2,2 2,3 2,4 2,5 2,6
    1,0 1,1 1,2 1,3 1,4 1,5 1,6
    0,0 0,1 0,2 0,3 0,4 0,5 0,6

    '''

    principal = {
      (0,0) : None,
      (1,0) : None, (0,1) : None,
      (2,0) : None, (1,1) : None, (0,2) : None,
      (3,0) : 0, (2,1) : 0, (1,2) : 0, (0,3) : 0,
      (4,0) : 1, (3,1) : 1, (2,2) : 1, (1,3) : 1, (0,4) : 1,
      (5,0) : 2, (4,1) : 2, (3,2) : 2, (2,3) : 2, (1,4) : 2, (0,5) : 2,
      (5,1) : 3, (4,2) : 3, (3,3) : 3, (2,4) : 3, (1,5) : 3, (0,6) : 3,
      (5,2) : 4, (4,3) : 4, (3,4) : 4, (2,5) : 4, (1,6) : 4,
      (5,3) : 5, (4,4) : 5, (3,5) : 5, (2,6) : 5,
      (5,4) : None, (4,5) : None, (3,6) : None,
      (5,5) : None,(4,6) : None,
      (5,6) : None
    }

    secundaria = {
      (5,0) : None,
      (4,0) : None, (5,1) : None,
      (3,0) : None, (4,1) : None, (5,2) : None,
      (2,0) : 6, (3,1) : 6, (4,2) : 6, (5,3) : 6,
      (1,0) : 7, (2,1) : 7, (3,2) : 7, (4,3) : 7, (5,4) : 7,
      (0,0) : 8, (1,1) : 8, (2,2) : 8, (3,3) : 8, (4,4) : 8, (5,5) : 8,
      (0,1) : 9, (1,2) : 9, (2,3) : 9, (3,4) : 9, (4,5) : 9, (5,6) : 9,
      (0,2) : 10, (1,3) : 10, (2,4) : 10, (3,5) : 10, (4,6) : 10,
      (0,3) : 11, (1,4) : 11, (2,5) : 11, (3,6) : 11,
      (0,4) : None, (1,5) : None, (2,6) : None,
      (0,5) : None, (1,6) : None,
      (0,6) : None
    }

    def __init__(self, linhas, colunas, celulas = None):
        if celulas is None:
            self.celulas = [[Jogador.VAZIO for _ in range(colunas)] for _ in range(linhas)]
        else:
            self.celulas = celulas
        
    def inserirPeca(self, coluna, jogador):
        for indice, linha in enumerate(self.celulas): 
            if linha[coluna] is Jogador.VAZIO:
                linha[coluna] = jogador
                return indice
            
    def verificarVitoria(self, jogada):
        # print jogada
        # verificar linha
        if Tabuleiro.listaTem4Conectados(self.celulas[jogada.linha], jogada.jogador):
            return True
        
        # verificar coluna
        coluna = [linha[jogada.coluna] for linha in self.celulas]
        if Tabuleiro.listaTem4Conectados(coluna, jogada.jogador):
            return True

        #verificar diagonais
        diagonais = self.obterDiagonais()
        indice_diagonal_principal = Tabuleiro.principal[(jogada.linha, jogada.coluna)]
        indice_diagonal_secundaria = Tabuleiro.secundaria[(jogada.linha , jogada.coluna)]

        diagonal_principal = []
        if indice_diagonal_principal is not None:
            diagonal_principal = diagonais[indice_diagonal_principal]

        diagonal_secundaria = []
        if indice_diagonal_secundaria is not None:          
            diagonal_secundaria = diagonais[indice_diagonal_secundaria]

        return Tabuleiro.listaTem4Conectados(diagonal_principal, jogada.jogador) or Tabuleiro.listaTem4Conectados(diagonal_secundaria, jogada.jogador)
    
    @staticmethod
    def listaTem4Conectados(lista, jogador):
        contador_iguais = 0
        for celula in lista:
            if celula is jogador:
                contador_iguais += 1
                if contador_iguais is 4:
                    return True
            else:
                contador_iguais = 0

        return False

    def utilidade(self, jogada):
        utilidade = 0;

        #verificar linha
        for linha in self.celulas:
            utilidade += Tabuleiro.utilidade_da_linha(linha, Jogador.COMPUTADOR, Jogador.HUMANO)
            utilidade -= Tabuleiro.utilidade_da_linha(linha, Jogador.HUMANO, Jogador.COMPUTADOR)
        
        # verificar coluna
        for i in range(7):
            coluna = [linha[i] for linha in self.celulas]
            utilidade += Tabuleiro.utilidade_da_coluna(coluna, Jogador.COMPUTADOR, Jogador.HUMANO)
            utilidade -= Tabuleiro.utilidade_da_coluna(coluna, Jogador.HUMANO, Jogador.COMPUTADOR)

        # verificar diagonais
        diagonais = self.obterDiagonais()

        utilidade += Tabuleiro.utilidade_de_4_celulas(diagonais[0],0, Jogador.COMPUTADOR, Jogador.HUMANO)
        utilidade -= Tabuleiro.utilidade_de_4_celulas(diagonais[0],0, Jogador.HUMANO, Jogador.COMPUTADOR)

        utilidade += Tabuleiro.utilidade_da_diagonal_de_5(diagonais[1], Jogador.COMPUTADOR, Jogador.HUMANO)
        utilidade -= Tabuleiro.utilidade_da_diagonal_de_5(diagonais[1], Jogador.HUMANO, Jogador.COMPUTADOR)

        utilidade += Tabuleiro.utilidade_da_diagonal_de_6(diagonais[2], Jogador.COMPUTADOR, Jogador.HUMANO)
        utilidade -= Tabuleiro.utilidade_da_diagonal_de_6(diagonais[2], Jogador.HUMANO, Jogador.COMPUTADOR)

        utilidade += Tabuleiro.utilidade_da_diagonal_de_6(diagonais[3], Jogador.COMPUTADOR, Jogador.HUMANO)
        utilidade -= Tabuleiro.utilidade_da_diagonal_de_6(diagonais[3], Jogador.HUMANO, Jogador.COMPUTADOR)

        utilidade += Tabuleiro.utilidade_da_diagonal_de_5(diagonais[4], Jogador.COMPUTADOR, Jogador.HUMANO)
        utilidade -= Tabuleiro.utilidade_da_diagonal_de_5(diagonais[4], Jogador.HUMANO, Jogador.COMPUTADOR)

        utilidade += Tabuleiro.utilidade_de_4_celulas(diagonais[5],0, Jogador.COMPUTADOR, Jogador.HUMANO)
        utilidade -= Tabuleiro.utilidade_de_4_celulas(diagonais[5],0, Jogador.HUMANO, Jogador.COMPUTADOR)

        utilidade += Tabuleiro.utilidade_de_4_celulas(diagonais[6],0, Jogador.COMPUTADOR, Jogador.HUMANO)
        utilidade -= Tabuleiro.utilidade_de_4_celulas(diagonais[6],0, Jogador.HUMANO, Jogador.COMPUTADOR)

        utilidade += Tabuleiro.utilidade_da_diagonal_de_5(diagonais[7], Jogador.COMPUTADOR, Jogador.HUMANO)
        utilidade -= Tabuleiro.utilidade_da_diagonal_de_5(diagonais[7], Jogador.HUMANO, Jogador.COMPUTADOR)

        utilidade += Tabuleiro.utilidade_da_diagonal_de_6(diagonais[8], Jogador.COMPUTADOR, Jogador.HUMANO)
        utilidade -= Tabuleiro.utilidade_da_diagonal_de_6(diagonais[8], Jogador.HUMANO, Jogador.COMPUTADOR)

        utilidade += Tabuleiro.utilidade_da_diagonal_de_6(diagonais[9], Jogador.COMPUTADOR, Jogador.HUMANO)
        utilidade -= Tabuleiro.utilidade_da_diagonal_de_6(diagonais[9], Jogador.HUMANO, Jogador.COMPUTADOR)

        utilidade += Tabuleiro.utilidade_da_diagonal_de_5(diagonais[10], Jogador.COMPUTADOR, Jogador.HUMANO)
        utilidade -= Tabuleiro.utilidade_da_diagonal_de_5(diagonais[10], Jogador.HUMANO, Jogador.COMPUTADOR)

        utilidade += Tabuleiro.utilidade_de_4_celulas(diagonais[11],0, Jogador.COMPUTADOR, Jogador.HUMANO)
        utilidade -= Tabuleiro.utilidade_de_4_celulas(diagonais[11],0, Jogador.HUMANO, Jogador.COMPUTADOR)

        return utilidade

    @staticmethod
    def utilidade_da_linha(lista, jogador, oponente):
        utilidade = 0
        
        utilidade += Tabuleiro.utilidade_de_4_celulas(lista, 0, jogador, oponente)
        utilidade += Tabuleiro.utilidade_de_4_celulas(lista, 1, jogador, oponente)
        utilidade += Tabuleiro.utilidade_de_4_celulas(lista, 2, jogador, oponente)
        utilidade += Tabuleiro.utilidade_de_4_celulas(lista, 3, jogador, oponente)

        return utilidade

    @staticmethod
    def utilidade_da_coluna(lista, jogador, oponente):
        utilidade = 0

        #slice manual
        utilidade += Tabuleiro.utilidade_de_4_celulas(lista, 0, jogador, oponente)
        utilidade += Tabuleiro.utilidade_de_4_celulas(lista, 1, jogador, oponente)
        utilidade += Tabuleiro.utilidade_de_4_celulas(lista, 2, jogador, oponente)
        
        return utilidade

    @staticmethod
    def utilidade_da_diagonal_de_6(lista, jogador, oponente):
        utilidade = 0

        utilidade += Tabuleiro.utilidade_de_4_celulas(lista, 0, jogador, oponente)
        utilidade += Tabuleiro.utilidade_de_4_celulas(lista, 1, jogador, oponente)
        utilidade += Tabuleiro.utilidade_de_4_celulas(lista, 2, jogador, oponente)
        
        return utilidade

    @staticmethod
    def utilidade_da_diagonal_de_5(lista, jogador, oponente):
        utilidade = 0
        
        utilidade += Tabuleiro.utilidade_de_4_celulas(lista, 0, jogador, oponente)
        utilidade += Tabuleiro.utilidade_de_4_celulas(lista, 1, jogador, oponente)
        
        return utilidade

    @staticmethod
    def utilidade_de_4_celulas(lista, comeco, jogador, oponente):
        contador_jogador = 0
        
        if lista[comeco] is jogador:
            contador_jogador += 1
        elif lista[comeco] is oponente:
            return 0

        if lista[comeco + 1] is jogador:
            contador_jogador += 1
        elif [comeco + 1] is oponente:
            return 0

        if lista[comeco + 2] is jogador:
            contador_jogador += 1
        elif lista[comeco +2] is oponente:
            return 0

        if lista[comeco + 3] is jogador:
            contador_jogador += 1
        elif lista[comeco + 3] is oponente:
            return 0

        if contador_jogador is 2:
            return 1
        elif contador_jogador is 3:
            return 10
        elif contador_jogador is 4:
            return 100
        else:
            return 0

    def obterDiagonais(self):
        diagonais = [
            [self.celulas[3][0], self.celulas[2][1], self.celulas[1][2], self.celulas[0][3]],
            [self.celulas[4][0], self.celulas[3][1], self.celulas[2][2], self.celulas[1][3], self.celulas[0][4]],
            [self.celulas[5][0], self.celulas[4][1], self.celulas[3][2], self.celulas[2][3], self.celulas[1][4], self.celulas[0][5]],
            [self.celulas[5][1], self.celulas[4][2], self.celulas[3][3], self.celulas[2][4], self.celulas[1][5], self.celulas[0][6]],
            [self.celulas[5][2], self.celulas[4][3], self.celulas[3][4], self.celulas[2][5], self.celulas[1][6]],
            [self.celulas[5][3], self.celulas[4][4], self.celulas[3][5], self.celulas[2][6]],
    
            [self.celulas[2][0], self.celulas[3][1], self.celulas[4][2], self.celulas[5][3]],
            [self.celulas[1][0], self.celulas[2][1], self.celulas[3][2], self.celulas[4][3], self.celulas[5][4]],
            [self.celulas[0][0], self.celulas[1][1], self.celulas[2][2], self.celulas[3][3], self.celulas[4][4], self.celulas[5][5]],
            [self.celulas[0][1], self.celulas[1][2], self.celulas[2][3], self.celulas[3][4], self.celulas[4][5], self.celulas[5][6]],
            [self.celulas[0][2], self.celulas[1][3], self.celulas[2][4], self.celulas[3][5], self.celulas[4][6]],
            [self.celulas[0][3], self.celulas[1][4], self.celulas[2][5], self.celulas[3][6]],
        ]
        return diagonais

    def __str__(self):
        string_tabuleiro = ""
        string_tabuleiro += "\n  1 2 3 4 5 6 7" + "\n"
        for indice, linha in enumerate(self.celulas):
            linha_str = ""
            for celula in linha:
                if celula is Jogador.COMPUTADOR:
                    linha_str += BColors.RED + u"●".encode('utf-8') + BColors.ENDC + " "
                elif celula is Jogador.HUMANO:
                    linha_str += BColors.BLUE + u"●".encode('utf-8') + BColors.ENDC + " "
                else:
                        linha_str += u"◦".encode('utf-8') + " "
            string_tabuleiro = "  "+ linha_str + "\n" + string_tabuleiro
        return string_tabuleiro
