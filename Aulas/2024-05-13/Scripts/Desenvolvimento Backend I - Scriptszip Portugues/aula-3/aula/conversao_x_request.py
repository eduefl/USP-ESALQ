import requests

print('carregando taxas')
response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
data = response.json()
taxa_dolar  = data['USDBRL']['bid']
taxa_euro   = data['EURBRL']['bid']
taxa_btc    = data['BTCBRL']['bid']

n_val_taxa_dolar    =  float(taxa_dolar)
n_val_taxa_euro     =   float(taxa_euro)
n_val_taxa_btc      =    float(taxa_btc)


print(f'taxa do Dolar   é R$ {n_val_taxa_dolar:.2f}')
print(f'taxa do Euro    é R$ {n_val_taxa_euro:.2f}')
print(f'taxa do BitCoin é R$ {n_val_taxa_btc:.2f}')


c_valor = input('Digite o valor em R$')
c_valor = c_valor.replace(',', '.', 1)
if not (c_valor.replace('.', '', 1).isdigit()):
    print("Valor monetario invalido!")    
else:
    n_valt_tiped = float(c_valor) 

    n_val_conv_usd = n_valt_tiped/ n_val_taxa_dolar
    n_val_conv_eur = n_valt_tiped/ n_val_taxa_euro 
    n_val_conv_btc = n_valt_tiped/ n_val_taxa_btc  
    
    print(f"Valor convertido em USD: {n_val_conv_usd:.2f}")    
    print(f"Valor convertido em EUR: {n_val_conv_eur:.2f}")    
    print(f"Valor convertido em BTC: {n_val_conv_btc:.8f}")    
    
