
# limite = 100
# soma = 0
# numero = 1 

# enquando a soma for menor do que o limite continue somando 

# while soma < limite:
#     soma+=numero
#     numero+=1
#     print(' soma ' + str(soma))
#     print(' numero ' + str(numero))
# print(' total ' + str(soma))


# encontrar io primeiro numeor divisivel por 7 em um intercalo
# 1-->99
# for numero in range(1,100):
#     if numero % 7 == 0:
#         print(numero)



# VErificar se todos os itens de uma lista sao positivos 

numeros = [1,2,33,5,8,9]

todos_positivos = True

for numero in numeros:
    # print(numero)
    if numero<0:
        todos_positivos = False
        break
if todos_positivos:
    print("todos os numeros sao positivos")
else:
    print("existe um numero negativo ")
