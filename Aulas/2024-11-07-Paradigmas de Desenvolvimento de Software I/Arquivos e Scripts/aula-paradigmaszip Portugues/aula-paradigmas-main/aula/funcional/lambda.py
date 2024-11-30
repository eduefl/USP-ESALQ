
# funcao lambda e uma funcao anonima (que nao tem nome) 

    #  funcoes que sao escritas em apenas uma linha onde eu posso a partir de imputs maniputas os imputs para obter uma respostta
dobro = lambda  x: x*2
#  dividda em duas partes a parte antes do dois pontos e a parte depois do dois pontos 
    # a parte antes do dois pontos sao os atributos de entrada
    # a parte depois e como vai ser a saida da miha funcao

# print(dobro(4))


valores = [1,2,3,4]

# o que a funcao mao faz ? 
    # Ela recebe uma funcao como primeiro agrumento e uma lista de valores como segundo argumento 
    # e executa essa funcao para cada argumento
valores_dobrados = list(map(lambda  x: x*2,valores))

# print(valores_dobrados)

# Calcular numeros impares
numeros = [1,2,3,4,5,6,7,8,9,10]
# maneira immperativa 

# resultado=[]
# for numero in numeros:
#     if numero % 2 !=0:
#         resultado.append(numero)
# print(resultado)


# Como que a funcao filter funciona? 
    # ela fucnina parecido com o map mas ain inves de interar com cada um dos elementos 
    # ela aplica uma condicao em cada um dos elementos retornando apenas os que satisfazem a condicao

resultado= list(filter(lambda x: x % 2 !=0,numeros))
print(resultado)
