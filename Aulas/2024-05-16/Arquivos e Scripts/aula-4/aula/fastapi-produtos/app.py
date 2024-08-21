from fastapi import FastAPI
from models.product import Product

app = FastAPI()

@app.get('/')
def hello_word():
	"""Primeiro end point o classico hello word"""
	return{'hello':'Word!'}


@app.get('/api2/{nome}')
def ola_fulano(nome: str):
	"""Escreva o noome e receba um ola"""

	if not nome:
		pass
	return{'ola':nome}
	
data = [
	Product(id = 1,  name = 'Tenis nke earth', description = 'tenis tenoso ', price = 99.63),
	Product(id = 2,  name = 'Setorianl', description = 'tenis ugiufh ', price = 599.63),
	Product(id = 3,  name = 'senhprvg', description = 'Garrafa de agua ', price = 899.63),
	Product(id = 4,  name = 'senhprvg', description = 'Yeeraaa', price = 1899.63),
]

@app.get('/apix/products')
def get_products():
	"""Retorna todos os produtos"""

	print(data)
	return data
@app.get('/apix/products/{id}')
def get_products_id(id: int):
	"""Retorna um produto por id"""
	for item in data:
		if item.id == id:
			return item
	return {'message':'Item not found'}

