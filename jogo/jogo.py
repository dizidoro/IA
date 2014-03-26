#!/usr/bin/python
'''
Created on Mar 25, 2014

@author: renan
'''

from tabuleiro import Tabuleiro
from cor import Cor
import game_input

def main():
    tabuleiro = Tabuleiro(6, 7)

    jogador_atual = game_input.solicitarJogadorIniciante()

    while True :
        print "\n", tabuleiro

        coluna = game_input.solicitarColuna()
        tabuleiro.inserirPeca(coluna, jogador_atual)
        
        jogador_atual = Cor.VERMELHO if jogador_atual is Cor.AZUL else Cor.AZUL

if __name__ == '__main__':
    main()