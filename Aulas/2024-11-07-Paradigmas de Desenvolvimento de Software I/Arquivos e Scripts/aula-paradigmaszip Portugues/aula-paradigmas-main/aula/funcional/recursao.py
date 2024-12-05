# Recursão #

# entrada -> funcao -> Saida (propria funcao)


# def fatorial(numero):
#     if numero ==1:
#         return 1
#     else:
#         return numero * fatorial(numero-1)
    
# x = fatorial(4)

# print(x)

# Calcululo de fibronachi

# a sequnencia: 0,1,1,2,3,5,8,13

def fibonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonachi(n - 2) + fibonachi(n - 1 )


n = fibonachi(100)
print(n)