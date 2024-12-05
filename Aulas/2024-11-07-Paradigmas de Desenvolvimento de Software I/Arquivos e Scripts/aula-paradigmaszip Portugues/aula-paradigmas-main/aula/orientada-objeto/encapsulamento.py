class ContaBancaria:

    def __init__(self, titular, saldo_inicial = 0):
        self.titular =titular
        # quando eu quero que um aributo seja privado coloco __ na frente do nome 
        self.__saldo = saldo_inicial  
    
    def get_saldo(self):
        return self.__saldo
    
    def depositar_dinheiro(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor de deposito deve ser positivo')
        
        

    def sacar_dinheiro(self, valor):
        if valor < 0:
            print('O valor de saque deve ser positivo')
        elif valor > self.__saldo:
            print('Limite insuficientepara operacao')
        else:
            self.__saldo -= valor

conta_a = ContaBancaria(titular='Jao' , saldo_inicial= 200)

conta_b = ContaBancaria(titular='Xandao' , saldo_inicial= 40000)

print(conta_a.get_saldo())
conta_a.depositar_dinheiro(300)
print(conta_a.get_saldo())
conta_a.sacar_dinheiro(1000)
print(conta_a.get_saldo())
conta_a.sacar_dinheiro(-200)
print(conta_a.get_saldo())
conta_a.depositar_dinheiro(-300)
print(conta_a.get_saldo())
conta_a.sacar_dinheiro(200)
print(conta_a.get_saldo())
