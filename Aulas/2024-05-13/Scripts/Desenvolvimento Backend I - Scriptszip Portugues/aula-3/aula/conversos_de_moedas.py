taxa_euro = 5.85
c_Valor = input('Digite o valor em R$')
c_Valor = c_Valor.replace(',', '.', 1)
if not (c_Valor.replace('.', '', 1).isdigit()):
    print("Valor monetario invalido!")    
else:
    nValConv = float(c_Valor)/ taxa_euro
    print("Valor convertido : ","{:.2f}".format(nValConv))    
    print(f"Valor convertido : {nValConv:.2f}")    
