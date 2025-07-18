class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João', 20)
p2 = Pessoa('Maria', 22)	
p3 = Pessoa('Carlos', 25)
p4 = Pessoa('Ana', 23)
p5 = Pessoa('Jorge', 27)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
print(p5.nome, p5.idade)