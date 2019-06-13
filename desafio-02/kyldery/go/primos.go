package main

import (
	"fmt"
)

func gerarNumerosPrimos(max int) []bool {
	primos := make([]bool, max+1)

	for i := 2; i*i <= max; i++ {
		if primos[i] == false {
			for j := i * 2; j <= max; j += i {
				primos[j] = true
			}
		}
	}
	return primos
}

func main() {
	numerosPrimos := gerarNumerosPrimos(10000)

	for i := 2; i < len(numerosPrimos); i++ {
		if numerosPrimos[i] == false {
			fmt.Printf("%d\n", i)
		}
	}
}
