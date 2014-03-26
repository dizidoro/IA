# -*- coding: utf-8 -*-
def solicitarColuna():
    while True:
        try:
            coluna = int(raw_input(u"Digite a coluna (intervalo [0,6]) para inserir uma peça: ".encode('utf-8')))
            if 0 <= coluna <= 6:
                return coluna
            else:
                print "Valor da coluna fora do intervalo!"
        except ValueError:
            print u"Isso nem sequer é um inteiro!".encode('utf-8')

def solicitarJogadorIniciante():
    while True:
        try:
            jogador = int(raw_input(u"Quem começa, jogador 1 ou 2? ".encode('utf-8')))
            if 1 <= jogador <= 2:
                return jogador
            else:
                print "Valor deve ser 1 ou 2!"
        except ValueError:
            print u"Isso nem sequer é um inteiro!".encode('utf-8')