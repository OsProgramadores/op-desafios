package main

import (
	"fmt"
	"testing"
)

func TestIsPrime(t *testing.T) {
	type testCase struct {
		upTo           int
		expectedPrimes int
	}
	tests := []testCase{
		{0, 0},
		{2, 1},
		{10, 4},
		{10000, 1229},
	}

	for _, test := range tests {
		primes := 0
		for i := 0; i <= test.upTo; i++ {
			if IsPrime(i) {
				primes++
			}
		}

		if primes != test.expectedPrimes {
			t.Errorf("Test Failed: %v -> expected: %v actual: %v\n",
				test.upTo, test.expectedPrimes, primes)
		} else {
			fmt.Printf("Test Passed: %v -> expected: %v actual: %v\n",
				test.upTo, test.expectedPrimes, primes)
		}
	}
}
