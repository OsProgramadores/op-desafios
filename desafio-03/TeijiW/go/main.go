package main

import (
	"fmt"
	"strconv"
)

func main() {

	var minInt int
	var maxInt int

	fmt.Println("Min: ")
	fmt.Scan(&minInt)
	fmt.Println("Max: ")
	fmt.Scan(&maxInt)

	fmt.Print("\n \n")

	for i := minInt; i <= maxInt; i++ {
		if numberIsPalindrome(i) {
			fmt.Println(i)
		}
	}
}

func reverse(originalText string) string {
	runeText := []rune(originalText)
	for i, j := 0, len(runeText)-1; i < j; i, j = i+1, j-1 {
		runeText[i], runeText[j] = runeText[j], runeText[i]
	}
	return string(runeText)
}

func numberIsPalindrome(number int) bool {
	text := string(strconv.Itoa(number))
	return text == reverse(text)
}
