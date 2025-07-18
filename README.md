Anotações das aulas realizadas

Aula 1 - Construção de uma classe

Projeto criado no Google Colab pelo professor. 
Essas aulas estão sendo feitas no VsCode por mim

class Pessoa: <- Classe 
def __init__(self, nome, idade): <- Método
	    self.nome = nome <- variável, atributo nome da classe pessoa
	    self.idade = idade
p1 = Pessoa('João', 20)
p2 = Pessoa('Maria', 22)	<- instancias
p3 = Pessoa('Carlos', 25)
p4 = Pessoa('Jorge', 27)

print(p1.nome, pq.idade)
print(p2.nome, pq.idade)
print(p3.nome, pq.idade)
print(p4.nome, pq.idade)

*************************************************************************************************

class Circulo: <- class indica ao python que está se criando uma classe
	
	def __init__(self, raio_parametro):
	    self.raio = raio_parametro

	def calcular_area(self):
    	return 3.14 * (self.raio ** 2)

c1 = Circulo(5)
print('Área: ', c1.calcular_area())

**********************************************************************************
Aula 2 - COnstrução de um Modelo Orientado a Objetos usando animais (Nenhum animal foi ferido ou morto durante a aula) - Herança e polimorfismo

Reaproveitameto de codigo ex 1:

class Animal: <- classe animal
	def __init__(self, nome, cor): <- parametro / para o metodo init precisa de um self
		self.nome = nome <- atibuto da classe animal
		self.cor = cor

class Cachorro(Animal): <- herança
	def latir(self): <- metodo latir
		return "Au Au!"

c = Cachorro("Rex", "Preto")

print(c.latir())
print(c.nome, c.cor)


Reaproveitameto de codigo ex 2: Retangulo e Forma

class Forma: <- super classe
	def calcular_area(self):
		pass <- indica que o metodo está vazio

class Retangulo(Forma): <- sub classe, herda a forma, o conceito da forma
	def __init__(self, baseP, alturaP):
		self.base = baseP <- atributo da classe, o "P" é o parametro
		self.altura = alturaP <- variavel = parametro

def calcular_area(self):
	return self.base * self.altura


class Circulo(Forma):
	def __init__(self, raioP):
		self.raio = raioP

	def calcular_area(self):
		return 3.14 * (self.raio ** 2)

ret = Retangulo(5, 3)
print("retangulo: ", ret.calcular_area())

cir = Circulo(4)
print("circulo: ", cir.calcular_area())

Cria-se uma instancia

************************************************************************************

Aula 3

	Encapsulamento e atributos privados

Aprende-se em Ciencia de dados

class ContaBancaria:
	def __init__(self, saldo):
	#pass -> indica que o metodo está vazio
		self.__saldo = saldo <- atributo privado, o saldo é um atributo da classe e um parametro

	def depositar(self, valor):
		self.__saldo = self.__saldo + valor

	def consultar_saldo(self):
		return self.__saldo

conta = ContaBancaria(1000)
conta.depositar(500)
print("saldo: ", conta.consultar_saldo())
print(conta.valor)

conta.depositar(100)
print(conta.consultar _saldo())


Exemplo 02

class Carro:
	def __init__(self, marca, modelo, ano):
		self.__marca = marca
		self.__modelo = modelo
		self.__ano = ano








