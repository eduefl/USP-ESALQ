
# o que uma funcao pura e uma funcao que retorna um valor 
    # ela nao tem efeito colateral
    # sempre produz os mesmos resultados sem ter efeitos colaterais


def soma(a,b):
    return a+b

# print(soma(3,4))
# print(soma(3,4))

# a funcao de alta ordem recebe como input uma outra funcao 
def aplicar_duas_vezes(func,valor):
    # output = func(valor)
    # output = func(output)    
    return func(func(valor))

def soma1(x):
    return x+1

def dividir_por_dois(x):
    return x/2

def elevar_ao_quadrado(x):
    return x**2

# print(soma1(6))

# print(aplicar_duas_vezes(soma1,8))


# print(aplicar_duas_vezes(elevar_ao_quadrado,6))


numeros = [1,2,3,4,5,6]

def aplicar_transformacao(funcao,lista):
    return [funcao(x) for x  in lista] #List comprehension
    # e o equivalente funcional a 
    # lista_trasformada = []
    # for item in lista:
    #     lista_trasformada.append(funcao(x))
    # return lista_trasformada
        

numeros_quadrado = aplicar_transformacao(elevar_ao_quadrado, numeros)

numeros_quadrado_divido_por_dois = aplicar_transformacao(dividir_por_dois,numeros_quadrado)
numeros_quadrado_divido_por_doisx = aplicar_transformacao(dividir_por_dois,aplicar_transformacao(elevar_ao_quadrado, numeros)) #a mesma coisa mas aninhado 

print(numeros_quadrado)

print(numeros_quadrado_divido_por_dois)

print(numeros_quadrado_divido_por_doisx)
