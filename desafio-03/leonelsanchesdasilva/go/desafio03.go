package main

import (
	"fmt"
	"strconv"
)

func Reverse(s string) (result string) {
	for _, v := range s {
		result = string(v) + result
	}
	return
}

func main() {
	for i := 1; i <= 3010; i++ {
		if strconv.Itoa(i) == Reverse(strconv.Itoa(i)) {
			fmt.Println(i)
		}
	}
}
