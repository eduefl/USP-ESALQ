package main

import(
	"fmt"
	"time"
)

func trabalho(nome string, sleep time.Duration)  {
	fmt.Println(nome, "iniciou")
	time.Sleep(sleep*time.Second)
	fmt.Println(nome,"finalizou")
}


func main()  {
	go trabalho("Groutine 1 ",3)	
	go trabalho("Groutine 1 ",3)	
	go trabalho("Groutine 1 ",3)	
	go trabalho("Groutine 2 ",1)	
	go trabalho("Groutine 2 ",1)	
	go trabalho("Groutine 2 ",1)	

	time.Sleep(10 * time.Second)
	fmt.Println("Todos os trabalhos foram finalizados")

}