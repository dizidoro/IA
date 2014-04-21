#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on Mar 25, 2014

@author: renan
'''

from tabuleiro import Tabuleiro
from jogador import Jogador
from jogada import Jogada
from nodo import Nodo
import game_input
import copy
import time

def main():
    numero_de_jogadas = 0

    tabuleiro = Tabuleiro(6, 7)

    jogador_atual = game_input.solicitarJogadorIniciante()
    jogo_nao_acabou = True
    print "\n", tabuleiro
    while jogo_nao_acabou:
        print "Vez do jogador", jogador_atual

        if jogador_atual is Jogador.COMPUTADOR:
            start = time.time()
            jogada = Nodo(copy.deepcopy(tabuleiro)).jogar();
            end = time.time()
            print "tempo: ", end - start
            tabuleiro.inserirPeca(jogada.coluna, jogador_atual)
        else:
            coluna = game_input.solicitarColuna()
            linha = tabuleiro.inserirPeca(coluna, jogador_atual)
            jogada = Jogada(linha, coluna, jogador_atual)
        
        numero_de_jogadas += 1
        jogada_vitoriosa = tabuleiro.verificarVitoria(jogada)

        Nodo.tamanho_colunas[jogada.coluna] +=1

        # print "linha: ",  str(jogada.linha + 1) 
        print "coluna: ", str(jogada.coluna + 1)

        print "\n", tabuleiro

        if jogada_vitoriosa:
            if jogador_atual is Jogador.COMPUTADOR:
                print "Perdeu playboy!!"
            else: 
                print "Voce ganhou, mas isso nao acaba aqui. Te pego na saida"
            jogo_nao_acabou = False
        else:
            if numero_de_jogadas is 42:
                print "Empate!"
                jogo_nao_acabou = False

        jogador_atual = Jogador.HUMANO if jogador_atual is Jogador.COMPUTADOR else Jogador.COMPUTADOR

# def main():
#     for i in range(7):
#         tabuleiro = Tabuleiro(6, 7)

#         jogador_atual = Jogador.HUMANO
#         coluna = i
#         tabuleiro.inserirPeca(coluna, jogador_atual)

#         jogador_atual = Jogador.COMPUTADOR
#         start = time.time()
#         jogada = Nodo(copy.deepcopy(tabuleiro)).jogar()
#         end = time.time()
#         print "nivel 1 - tempo para coluna ",coluna, " : ", end - start
#         tabuleiro.inserirPeca(jogada.coluna, jogador_atual)

        # jogador_atual = Jogador.HUMANO
        # coluna = 2
        # tabuleiro.inserirPeca(coluna, jogador_atual)

        # jogador_atual = Jogador.COMPUTADOR
        # start = time.time()
        # jogada = Nodo(copy.deepcopy(tabuleiro)).jogar()
        # end = time.time()
        # print "nivel 2 - tempo para coluna ",coluna, " : ", end - start
        # tabuleiro.inserirPeca(jogada.coluna, jogador_atual)

        # for k in range(7):
            # jogador_atual = Jogador.HUMANO
            # coluna = k
            # tabuleiro.inserirPeca(coluna, jogador_atual)

            # jogador_atual = Jogador.COMPUTADOR
            # start = time.time()
            # jogada = Nodo(copy.deepcopy(tabuleiro)).jogar()
            # end = time.time()
            # print "nivel 2 - tempo para coluna ",coluna, " : ", end - start
            # tabuleiro.inserirPeca(jogada.coluna, jogador_atual)
            



# def main():
#     tabuleiro = Tabuleiro(6, 7)
#     nodo = Nodo(copy.deepcopy(tabuleiro));
#     nodo.jogar()


if __name__ == '__main__':
    main()