import sys
from tabuleiro import Tabuleiro
from jogador import Jogador
from jogada import Jogada
import copy
import time

class Nodo:

    MAX = sys.maxint
    MIN = - sys.maxint
    NIVEL_MAX = 9
    N_JOGADAS = 0
    tamanho_colunas = [0,0,0,0,0,0,0]

    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro

    def jogar(self):
        maior_utilidade = Nodo.MIN
        melhor_jogada = Jogada(0, 0, 1)
        nivel = 1
        # [0,1,2,3,4,5,6]
        # sort by next play utility
        # for i in range(7):
        #     tabuleiro = Tabuleiro(0, 0, [list(linha) for linha in self.tabuleiro.celulas])

        # if Nodo.N_JOGADAS is 8:
        #     Nodo.NIVEL_MAX = 11
        # elif Nodo.N_JOGADAS is 9:
        #     Nodo.NIVEL_MAX = 14
        # elif Nodo.N_JOGADAS >= 10:
        #     Nodo.NIVEL_MAX = 20
        Nodo.NIVEL_MAX = 9 + Nodo.tamanho_colunas.count(7) * 3

        for i in [3,2,4,1,5,0,6]:
            # tabuleiro = copy.deepcopy(self.tabuleiro)
            if Nodo.tamanho_colunas[i] is 7:
                continue

            tabuleiro = Tabuleiro(0,0,[list(linha) for linha in self.tabuleiro.celulas])
            linha = tabuleiro.inserirPeca(i, Jogador.COMPUTADOR)
            if linha is None:
                continue
            nodo = Nodo(tabuleiro)
            jogada = Jogada(linha, i, Jogador.COMPUTADOR)
            utilidade = nodo.visitar(nivel, Nodo.MIN, Nodo.MAX, jogada)
            if utilidade > maior_utilidade:
                melhor_jogada = jogada
                maior_utilidade = utilidade

        return melhor_jogada


    def visitar(self, nivel, alpha, beta, jogada):
        if nivel == Nodo.NIVEL_MAX or self.tabuleiro.verificarVitoria(jogada):
            return self.tabuleiro.utilidade(jogada)
        
        jogador = Jogador.HUMANO if jogada.jogador is Jogador.COMPUTADOR else Jogador.COMPUTADOR

        for i in [3,2,4,1,5,0,6]:
            # tabuleiro = copy.deepcopy(self.tabuleiro)
            tabuleiro = Tabuleiro(0,0,[list(linha) for linha in self.tabuleiro.celulas])
            linha = tabuleiro.inserirPeca(i, jogador)
            if linha is None:
                continue
            nodo = Nodo(tabuleiro)
            jogada = Jogada(linha, i, jogador)
            utilidade = nodo.visitar(nivel+1, alpha, beta, jogada)
            if jogador is Jogador.COMPUTADOR:
                if utilidade > alpha:
                    alpha = utilidade
            else:
                if utilidade < beta:
                    beta = utilidade

            if alpha >= beta:
                if jogador is Jogador.COMPUTADOR:
                    return alpha
                else:
                    return beta


        if jogador is Jogador.COMPUTADOR:
            return alpha
        else:
            return beta




