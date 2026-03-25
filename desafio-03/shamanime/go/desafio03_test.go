package main

import (
	"fmt"
	"testing"
)

func TestIsPalindromicNumber(t *testing.T) {
	type testCase struct {
		number         uint64
		expectedResult bool
	}
	tests := []testCase{
		{1, true},
		{10, false},
		{101, true},
		{12345, false},
		{12321, true},
	}

	for _, test := range tests {
		result := IsPalindromicNumber(test.number)

		if result != test.expectedResult {
			t.Errorf("Test Failed: %v -> expected: %v actual: %v\n",
				test.number, test.expectedResult, result)
		} else {
			fmt.Printf("Test Passed: %v -> expected: %v actual: %v\n",
				test.number, test.expectedResult, result)
		}
	}
}
