package main

import "fmt"

func isPrimary(number int) bool {
	/*
	  Function: verifies whether a number is primary or not.
	  Input: integer
	  Response: boolean

	  src: https://en.wikipedia.org/wiki/Primality_test
	  function is_prime(n)
	   if n ≤ 3
	      return n > 1
	   else if n mod 2 = 0 or n mod 3 = 0
	      return false
	   let i ← 5
	   while i * i ≤ n
	      if n mod i = 0 or n mod (i + 2) = 0
	          return false
	      i ← i + 6
	   return true
	*/
	if number <= 1 {
		return false
	}
	if number <= 3 {
		return true
	}
	if number%2 == 0 || number%3 == 0 {
		return false
	}

	i := 5
	for j := i * i; j <= number; {
		if number%i == 0 || number%(i+2) == 0 {
			return false
		}
		i += 6
		j = i * i
	}
	return true
}

func main() {
	for i := 0; i <= 10000; i++ {
		if isPrimary(i) == true {
			fmt.Println(i)
		}
	}
}
