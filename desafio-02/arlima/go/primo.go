package main

import (
	"fmt"
	"math"
)

// geraprimos é uma função para geração de um array que identifica se um
// número, menor que n, é primo ou não.
// Referência: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
func geraPrimos(n int64) []bool {
	var (
		i, j int64
	)

	flag1 := make([]bool, n)
	for i = 0; i < n; i++ {
		flag1[i] = true
	}

	flag1[0] = false
	flag1[1] = false

	for i = 2; i < int64(math.Sqrt(float64(n)))+1; i++ {
		if flag1[i] {
			for j = i * i; j < n; j += i {
				flag1[j] = false
			}
		}
	}
	return flag1
}

func main() {
	primo := geraPrimos(10001)
	for i := 1; i <= 10000; i++ {
		if primo[i] {
			fmt.Println(i)
		}
	}
}
