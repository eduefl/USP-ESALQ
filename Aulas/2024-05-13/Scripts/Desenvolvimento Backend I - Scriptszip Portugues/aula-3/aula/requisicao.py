import requests

response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
data = response.json()
taxa_dolar = data['USDBRL']['bid']
n_val_taxa_dolar = float(taxa_dolar)
print(f'A atxa do dolar e R$ {n_val_taxa_dolar:.2f}')
