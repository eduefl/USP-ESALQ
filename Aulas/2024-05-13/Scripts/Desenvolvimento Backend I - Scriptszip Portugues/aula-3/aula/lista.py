# Indice 0 1 2 3 4 
numeros = [1,4,3,3,5]

print('lista de numeros ',numeros)
print('lista de numeros ',numeros[0])
print('lista de numeros ',numeros[-1])
print('-----------Separator-----------')

numeros.append(6)

print('lista de numeros ',numeros)

print('lista de numeros ',numeros[0])
print('lista de numeros ',numeros[-1])
print('-----------Separator-----------')

numeros.remove(4)
print('lista de numeros ',numeros)
print('-----------Separator-----------')

numeros = [1,4,3,3,5]
print('lista de numeros ',numeros)

numeros.pop(4)
print('lista de numeros ',numeros)
print('lista de numeros ',numeros[0])
print('lista de numeros ',numeros[-1])
print('-----------Separator-----------')

numeros = [1,2,3,4,5]
i = 0
for numero in numeros:
	print(numero)

print('-----------Separator-----------')

# exemplo de For
for numero in numeros:
	print(numeros[i]*2)
	i+=1
print('-----------Separator-----------')

# exemplo de IF 
n_search = 2
if n_search in numeros:
	print(str(n_search)+ ' Esta na lista')
else:
	print(str(n_search)+' nao Esta na lista')
print('-----------Separator-----------')
	
# exemplo de IF Elseif (elif)
n_search = 6
if n_search > len(numeros):
	print("o tamanho do array e menor que "+str(n_search))
elif n_search == len(numeros):
	print("o tamanho do array e Igual a "+str(n_search))
else:
		print("o tamanho do array e maior que "+str(n_search))

