# -*- coding: utf-8 -*-
from bcolors import BColors

def solicitarColuna():
    while True:
        try:
            coluna = int(raw_input(u"Digite a coluna [1,7] para inserir uma peça: ".encode('utf-8')))
            if 1 <= coluna <= 7:
                return coluna - 1
            else:
                print BColors.WARNING + "Valor da coluna fora do intervalo!" + BColors.ENDC
        except ValueError:
            print BColors.WARNING+ u"Isso nem sequer é um inteiro!".encode('utf-8') + BColors.ENDC

def solicitarJogadorIniciante():
    while True:
        try:
            jogador = int(raw_input(u"Quem começa, jogador humano (1) ou computador (2)? ".encode('utf-8')))
            if 1 <= jogador <= 2:
                return jogador
            else:
                print BColors.WARNING + "Valor deve ser 1 ou 2!" + BColors.ENDC
        except ValueError:
            print BColors.WARNING + u"Isso nem sequer é um inteiro!".encode('utf-8') + BColors.ENDC