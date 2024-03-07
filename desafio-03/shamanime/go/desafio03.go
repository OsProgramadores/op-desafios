package main

import (
	"fmt"
	"os"
)

func IsPalindromicNumber(n uint64) bool {
	input := n
	var reversed uint64 = 0
	for n > 0 {
		reversed = reversed*10 + n%10
		n /= 10
	}
	return input == reversed
}

func main() {
	fmt.Println("Este programa mostra os números palíndromos entre dois valores.")
	fmt.Println("Informe apenas números inteiros positivos. O valor final deve ser maior que o inicial.")

	fmt.Println("Digite o número inicial:")
	var first uint64
	fmt.Scanln(&first)

	fmt.Println("Digite o número final:")
	var last uint64
	fmt.Scanln(&last)

	if first > last {
		fmt.Println("O valor final deve ser maior que o inicial.")
		os.Exit(1)
	}

	var results []uint64
	for i := first; i <= last; i++ {
		if IsPalindromicNumber(i) {
			results = append(results, i)
		}
	}
	fmt.Println("Os números palíndromos entre", first, "e", last, "são:", results)
}
