from  functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]

# map, filter, reduce 

# o que o reduce faz? 
    # ele vai somar a partir de uma funcao lambda valores e agregar no output  ate entregar os dados somados

# filtrar os numeros pares

numeros_pares = list(filter(lambda x:  x%2 ==0,  numeros))

numeros_pares_dobrados = list(map(lambda x:  x*2,numeros_pares ))

soma_numeros_pares_dobrados =reduce(lambda x,y: x+y, numeros_pares_dobrados)

print(numeros_pares)

print(numeros_pares_dobrados)

print(soma_numeros_pares_dobrados)