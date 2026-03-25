package main

import (
	"fmt"
)

func main() {
	piecesCount := map[int]int{}
	piecesNames := map[string]int{
		"Peão":   1,
		"Bispo":  2,
		"Cavalo": 3,
		"Torre":  4,
		"Rainha": 5,
		"Rei":    6,
	}
	pieces := [8][8]int{
		{4, 3, 2, 5, 6, 2, 3, 4},
		{1, 1, 1, 0, 0, 1, 1, 1},
		{0, 0, 0, 1, 1, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 1, 1, 0, 0, 0},
		{1, 1, 1, 0, 0, 1, 1, 1},
		{4, 3, 2, 5, 6, 2, 3, 4},
	}

	for _, row := range pieces {
		for _, col := range row {
			piecesCount[col]++
		}
	}

	for key, value := range piecesNames {
		fmt.Printf("%v: %v Peça(s)\n", key, piecesCount[value])
	}
}
