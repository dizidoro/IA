class Jogada:
	
	def __init__(self, linha, coluna, jogador):
		self.linha = linha
		self.coluna = coluna
		self.jogador = jogador

	def __str__(self):
		return  str(self.linha)+str(self.coluna)+str(self.jogador)