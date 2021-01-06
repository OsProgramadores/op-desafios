package main

import "fmt"

func showPrimes(x, y int) {
	for i := x; i < y; i++ {
		quantityOfDivisors := 0
		for j := 1; j <= i; j++ {
			if i%j == 0 {
				quantityOfDivisors++
			}
		}
		if quantityOfDivisors == 2 {
			fmt.Println(i)
		}
	}
}

func main() {
	showPrimes(1, 1000)
}
