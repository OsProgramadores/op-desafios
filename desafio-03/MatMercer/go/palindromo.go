package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	start, _ := strconv.ParseUint(os.Args[1], 10, 64)
	end, _ := strconv.ParseUint(os.Args[2], 10, 64)

	for i := start; i < end; i++ {
		if isPalindrome(i) {
			fmt.Printf("%d ", i)
		}
	}
}

func isPalindrome(num uint64) bool {
	strNum := strconv.FormatUint(num, 10)
	algCount := len(strNum)

	if algCount == 1 {
		return true
	}

	var middleSize int
	middleSize = algCount / 2

	for i := 0; i < middleSize; i++ {
		if strNum[i] != strNum[algCount-1-i] {
			return false
		}
	}

	return true
}
