// Desafio 02 | Os Programadores - Imprimir todos os números palindrômicos entre dois números.
package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) < 3 {
		fmt.Println("É preciso informar um número inicial e um número final. e.g.: palindrome 100 5000")
		os.Exit(2)
	}
	min, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println("O primeiro input não é um número")
		os.Exit(2)
	}
	max, err := strconv.Atoi(os.Args[2])
	if err != nil {
		fmt.Println("O segundo input não é um número")
		os.Exit(2)
	}
	for i := min; i < max; i++ {
		if palindrome(i) {
			fmt.Printf("%d é um palindromo\n", i)
		}
	}
}

func palindrome(num int) bool {
	// Cria uma váriavel que irá guardar o número invertido
	var inv int
	// salva o valor do num em uma variável distinta para
	// fazer a comparação posteriormente
	n := num
	for num > 0 {
		// Monta os dígitos do número invertido multiplicando
		// o dígito por 10 e somando com o último dígito do input
		inv = inv*10 + (num % 10)
		num = num / 10
	}
	// se o número invertido for igual ao valor salvo do input
	// então o número é um palíndromo
	if n == inv {
		return true
	}
	return false
}
