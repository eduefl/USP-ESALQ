let produtos = []
let endpoint = 'https://raw.githubusercontent.com/guilhermeonrails/api-frontend/main/produtos.json'
let nodeProduct = document.getElementById('produtos__lista')

buscarProdutosDaAPI()

async function buscarProdutosDaAPI() {
	let res = await fetch(endpoint)
	produtos = await res.json()
	exibirProdutos(produtos)
}

function exibirProdutos(produtos) {
	console.log(produtos)
	console.table(produtos)
	produtos.forEach( produto => {
		nodeProduct.innerHTML +=`
		<li class="produtos__item">
		<div class="produtos__content">
			<img src="${produto.img}" alt="Imagem de celular">
			<div class="produtos__informacoes">
				<h3>${produto.nome}</h3>
				<p>${produto.descricao}</p>
				<h4>R$${produto.valorSemDesconto}<s>R$ ${produto.valorComDesconto}</s></h4>
				<p>${produto.tipoEntrega}</p>
			</div>
		</div>
	</li>

		`	
	})
}