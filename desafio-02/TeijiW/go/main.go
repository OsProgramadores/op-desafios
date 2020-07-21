package main

import (
	"fmt"
)

func main() {
	var primeNumbers []int
	for i := 0; i < 10000; i++ {
		if isPrime(i) {
			primeNumbers = append(primeNumbers, i)
		}
	}
	fmt.Println(primeNumbers)
}

func isPrime(number int) bool {
	var count int = 0
	for i := 1; i <= number; i++ {
		if number%i == 0 {
			count++
		}
	}
	return count <= 2
}
