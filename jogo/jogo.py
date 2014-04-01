#!/usr/bin/python
'''
Created on Mar 25, 2014

@author: renan
'''

from tabuleiro import Tabuleiro
from jogador import Jogador
from jogada import Jogada
import game_input

def main():
    tabuleiro = Tabuleiro(6, 7)

    jogador_atual = game_input.solicitarJogadorIniciante()
    jogo_nao_acabou = True
    print "\n", tabuleiro
    while jogo_nao_acabou:
        print "Vez do jogador", jogador_atual

        coluna = game_input.solicitarColuna()
        linha = tabuleiro.inserirPeca(coluna, jogador_atual)
        
        jogada = Jogada(linha, coluna, jogador_atual)
        jogada_vitoriosa = tabuleiro.verificarVitoria(jogada)

        print "linha, coluna: ", str(linha) + "," + str(coluna)
        print "\n", tabuleiro

        if jogada_vitoriosa:
            print "Parabens jogador",jogador_atual,"voce ganhou!"
            jogo_nao_acabou = False

        jogador_atual = Jogador.HUMANO if jogador_atual is Jogador.COMPUTADOR else Jogador.COMPUTADOR

if __name__ == '__main__':
    main()