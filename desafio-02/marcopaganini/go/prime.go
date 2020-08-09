// Silly go program to display all primes between 2 and a given number.
//
// This is a very simple program that displays all primes between 2
// and a given number. Exercises:
//
// - Find bugs
// - Optimize the algorithm.
// - Use all processors in the system.
// - Change the program to allow truly gigantic numbers.
// - What happens today if we just pass a number that is too large?
// - How much memory do we need for really large numbers?
//
// Written as an example by Marco Paganini <paganini@paganini.net>,
// in literally 10 minutes. This is probably buggy and unoptimized.

package main

import (
	"fmt"
	"math"
	"os"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Use: prime max_number")
		os.Exit(2)
	}
	maxNum, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Printf("Error: max_number must be a number (got %q)\n", os.Args[1])
		os.Exit(2)
	}

	sieve := make([]bool, maxNum)

	halfway := int(math.Ceil(math.Sqrt(float64(maxNum))))

	// Fill-in the sieve and print lower half primes.
	for n := 2; n <= maxNum; n++ {
		if !sieve[n-1] {
			fmt.Println(n, "is prime")
		}
		// Fill remaining if under square root of number
		if n <= halfway {
			for idx := (n - 1); idx < maxNum; idx += n {
				sieve[idx] = true
			}
		}
	}
}
