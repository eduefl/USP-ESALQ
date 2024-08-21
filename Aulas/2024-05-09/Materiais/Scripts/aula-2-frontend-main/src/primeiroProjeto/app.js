let botao = document.querySelector('button')

botao.addEventListener('click',somaum)

function somaum(){
	let elementoH3 =document.querySelector('h3')
	let valor =parseInt(elementoH3.textContent)
	let r = parseInt(Math.random()*256)
	let g = parseInt(Math.random()*256)
	let b = parseInt(Math.random()*256)
	
	valor ++
	elementoH3.textContent = valor
	
	elementoH3.style.color =`rgb(${r},${g},${b})`
}