class Carro:


    def __init__(self, marca, modelo,ano):
        self.marca = marca
        self.modelo_do_carro = modelo
        self.ano = ano

    def emitir_som(self):
        print('Vrummmmmmmmmmmmmmmmmmmmmm')


    def exibir_detalhes(self):
        print('--------------------------------------------------------')
        # print(self.marca)
        # print(self.modelo_do_carro)
        # print(self.ano)
        print(f"Carro: {self.marca} {self.modelo_do_carro}, Ano: {self.ano}")
        self.emitir_som()
        # print('--------------------------------------------------------')

carro1 = Carro(marca='toyota', modelo='Corola', ano=2010)
carro3 = Carro(marca='Renault', modelo='Duster', ano=2024)

print(carro1.marca,carro1.modelo_do_carro,carro1.ano)        
print(carro3.marca,carro3.modelo_do_carro,carro3.ano)        

carro1.exibir_detalhes()
carro3.exibir_detalhes()

# carro3.emitir_som()