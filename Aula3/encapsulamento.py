class ContaBancaria:
	def __init__(self, saldo):
	#pass -> indica que o metodo está vazio
		self.__saldo = saldo
		self.valor = saldo
				
	def depositar(self, valor):
		self.__saldo = self.__saldo + valor

	def consultar_saldo(self):
		return self.__saldo

conta = ContaBancaria(1000)
print("saldo inicial: ", conta.consultar_saldo())
#print(conta.valor)

valor_deposito = (500)
print("Valor depositado: ", valor_deposito)

conta.depositar(valor_deposito)

print("Saldo Total: ", conta.consultar_saldo())

#conta.deposito(500)
#print("Valor depositado: ",conta.deposito)
#print("Saldo Total: ", conta.consultar_saldo())
