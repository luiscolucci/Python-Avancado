class Circulo: 
	
    def __init__(self, raio_parametro):
        self.raio = raio_parametro

    def calcular_area(self):
        return 3.14 * (self.raio ** 2)

c1 = Circulo(5)
print('Área: ', c1.calcular_area())