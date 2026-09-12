package main

import (
	"fmt"
	"math"
)

func main() {
	lastNumToVerify := int(math.Sqrt(10_000))
	primes := []int{}
	var divisibleCount int
	for i := 2; i <= lastNumToVerify; i++ {
		for j := 1; j <= i; j++ {
			if i%j == 0 {
				divisibleCount++
			}
		}
		if divisibleCount == 2 {
			primes = append(primes, i)
		}
		divisibleCount = 0
	}

	finalPrimes := primes
	var isPrime bool
	for i := (primes[len(primes)-1] + 1); i <= 10_000; i++ {
		isPrime = true
		for _, p := range primes {
			if i%p == 0 {
				isPrime = false
			}
		}
		if isPrime {
			finalPrimes = append(finalPrimes, i)
		}
	}

	for _, i := range finalPrimes {
		fmt.Println(i)
	}
}
