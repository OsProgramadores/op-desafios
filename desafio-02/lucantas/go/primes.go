// Os Programadores - Desafio 2

// ### Faltando:
// - Melhora do algoritmo
// - Melhora na inicialização da array de booleanos com valor true
// ou contornar essa parte do algoritmo de outra forma
package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	log.Println(os.Args)
	if len(os.Args) < 2 {
		fmt.Println("Faltando argumentos, digite o número máximo a ser testado")
		os.Exit(2)
	}
	max, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println("Erro, o argumento não é um número:", err)
		os.Exit(2)
	}
	primeDetector(max)
}

func primeDetector(n int) {
	// Cria uma array de booleanos com o tamanho de n
	ab := make([]bool, n)
	// Tornando os valores da array como true
	for i := 0; i < n; i++ {
		ab[i] = true
	}
	// Varre sobre cada número para que os seus múltiplos sejam marcados
	// como compostos
	for num := 2; num*num <= n; num++ {
		// se o index num da array de booleans ab for true, é um número primo
		if ab[num] {
			for i := num * 2; i < n; i += num {
				ab[i] = false
			}
		}
	}
	// Varre a array de booleanos e exibe os números primos na saída
	for i := 2; i < n; i++ {
		if ab[i] == true {
			log.Printf("O número %d é primo:", i)
		}
	}
}
