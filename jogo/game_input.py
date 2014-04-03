# -*- coding: utf-8 -*-
def solicitarColuna():
    while True:
        try:
            coluna = int(raw_input(u"Digite a coluna [1,7] para inserir uma peça: ".encode('utf-8')))
            if 1 <= coluna <= 7:
                return coluna - 1
            else:
                print "Valor da coluna fora do intervalo!"
        except ValueError:
            print u"Isso nem sequer é um inteiro!".encode('utf-8')

def solicitarJogadorIniciante():
    while True:
        try:
            jogador = int(raw_input(u"Quem começa, jogador humano (1) ou computador (2)? ".encode('utf-8')))
            if 1 <= jogador <= 2:
                return jogador
            else:
                print "Valor deve ser 1 ou 2!"
        except ValueError:
            print u"Isso nem sequer é um inteiro!".encode('utf-8')