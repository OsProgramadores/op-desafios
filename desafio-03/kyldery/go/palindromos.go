package main

import (
	"fmt"
)

func inverterNumero(n int) (num int) {
	for ; n > 0; n /= 10 {
		num *= 10
		num += n % 10
	}
	return num
}

func verficarPalindromo(n int) bool {
	if n <= 9 {
		return true
	}
	return n == inverterNumero(n)
}

func main() {
	for numero := 1; numero <= 10000; numero++ {
		if verficarPalindromo(numero) {
			fmt.Println(numero)
		}
	}
}
