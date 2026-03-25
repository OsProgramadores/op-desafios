package main

import (
	"fmt"
)

func main() {
	var primeNumbers []int
	for i := 1; i <= 10000; i++ {
		if isPrime(i) {
			primeNumbers = append(primeNumbers, i)
		}
	}
	fmt.Println(primeNumbers)
}

func isPrime(number int) bool {
	for i := 2; i < number; i++ {
		if number%i == 0 {
			return false
		}
	}
	return true
}
