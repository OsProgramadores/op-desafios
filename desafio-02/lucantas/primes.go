// Os Programadores - Desafio 2
package main

import (
	"fmt"
	"math/big"
)

func main() {
	// iteira sobre inteiros entre 2 e 10000
	for i := 2; i < 10000; i++ {
		// Testa o número com a função ProbablyPrime do pacote math/big
		// da biblioteca padrão
		if big.NewInt(int64(i)).ProbablyPrime(0) {
			// Número primo encontrado
			fmt.Println("É primo:", i)
		}
	}
}
