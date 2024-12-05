from abc import ABC, abstractmethod

class FormaGeometrica(ABC): #para classes abstratas eu tenho que injetar a dependencia ABC
    
    @abstractmethod #Para definir metodos abstratos eu tenho que definir o decorator abstractmethod
    def calcular_area(self):
        raise NotImplementedError('Esse metodo deve ser implementado obrigatoriamente ')
    

class Circulo(FormaGeometrica):  #Passando como parametro eu informa que essa classe depende da outra a do parametro 
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = 3.14 * self.raio ** 2
        return area
    
class Retangulo (FormaGeometrica):
    def __init__(self, largura, autura):
        self.largura = largura
        self.autura = autura
        
    def calcular_area(self):
        return self.largura * self.autura




# circulo = Circulo(10)
# circulo2 = Circulo(2)
# circulo3 = Circulo(0.6559)

# print(circulo.raio)
# print(circulo.calcular_area())


# print(circulo2.raio)
# print(circulo2.calcular_area())

# print(circulo3.raio)
# print(circulo3.calcular_area())

# Retangulo1 = Retangulo(largura=10, autura= 5)

# print(Retangulo1.autura, Retangulo1.largura)
# print(Retangulo1.calcular_area())



# Composicao

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
        self.ligado = False

    def ligar_motor(self):
        self.ligado = True
        print ('Veiculo ligado')

class Carro:
    def __init__(self, marca,modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
    
    def exibir_detalhes(self):
        print(f"carro {self.marca} {self.modelo}")

    def mostrar_potencia_motor(self):
        print(f"Motode de potencia: {self.motor.potencia} Cavalos")

    


motor1 = Motor(potencia=200)

motor1.ligar_motor()
print(motor1.ligado)

carro1 = Carro(marca="Honda",modelo="Civic",motor=motor1)

carro1.exibir_detalhes()
carro1.mostrar_potencia_motor()