Aula 1 - Construção de uma classe

Projeto criado no Google Colab pelo professor. 
Essas aulas estão sendo feitas no VsCode por mim

class Pessoa: <- Classe 
def __init__(self, nome, idade): <- Método
	    self.nome = nome <- variável, atributo nome da classe pessoa
	    self.idade = idade
P1 = Pessoa(“João”, 20)
P2 = Pessoa(“Maria”, 22)	<- instancias
P3 = Pessoa(“Carlos”, 25)
P4 = Pessoa(“Jorge”, 27)

print(p1.nome, pq.idade)
print(p2.nome, pq.idade)
print(p3.nome, pq.idade)
print(p4.nome, pq.idade)

*************************************************************************************************

class Circulo: <- class indica ao python que está se criando uma classe
	def __init__(self, raio_parametro):
	    Self.raio = raio_parametro

def calcular_area(self):
    Return 3.14 * (self.raio ** 2)

C1 = Circulo(5)
print(“área: “c1.calcular_area())
