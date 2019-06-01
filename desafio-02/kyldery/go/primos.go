package main

import (
	"fmt"
)

func verificarNumeroPrimo(numero int) bool {
	numeroDeDivisores := 0

	for i := 1; i <= numero; i++ {
		if numeroDeDivisores > 2 {
			return false
		} else if resto := numero % i; resto == 0 {
			numeroDeDivisores++
		}

	}
	return numeroDeDivisores == 2
}

func main() {
	for numero := 1; numero <= 10000; numero++ {
		if verificarNumeroPrimo(numero) {
			fmt.Println(numero)
		}
	}
}
