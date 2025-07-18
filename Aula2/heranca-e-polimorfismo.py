class Animal:
	def __init__(self, nome, e, cor): 
		self.nome = nome
		self.cor = cor
		self.e = e
		

class Cachorro(Animal):
	def latir(self):
		return "Au Au!"

c = Cachorro("Olá, sou o Rex", "e", "sou Preto")

print(c.latir())
print(c.nome, c.e, c.cor)