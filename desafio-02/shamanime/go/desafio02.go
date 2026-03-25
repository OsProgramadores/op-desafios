package main

import (
	"fmt"
	"math"
)

func IsPrime(value int) bool {
	sqrt := math.Sqrt(float64(value))
	for i := 2; i <= int(math.Floor(sqrt)); i++ {
		if value%i == 0 {
			return false
		}
	}
	return value > 1
}

func main() {
	for i := 0; i <= 10000; i++ {
		if IsPrime(i) {
			fmt.Println(i)
		}
	}
}
