'''
Created on Mar 25, 2014

@author: renan
'''

from tabuleiro import Tabuleiro
from cor import Cor

tabuleiro = Tabuleiro(6, 7)

jogador = Cor.AZUL
while(True):
    coluna = int(raw_input("Digite a coluna para inserir uma peca"))
    tabuleiro.inserirPeca(coluna, jogador)
    if (jogador==Cor.AZUL):
        jogador = Cor.VERMELHO
    else:
        jogador = Cor.AZUL
        
    print tabuleiro