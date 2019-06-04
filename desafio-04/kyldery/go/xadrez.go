package main

import (
	"fmt"
)

func main() {
	tabuleiro := [8][8]int{
		{4, 3, 2, 5, 6, 2, 3, 4},
		{1, 1, 1, 0, 0, 1, 1, 1},
		{0, 0, 0, 1, 1, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 1, 1, 0, 0, 0},
		{1, 1, 1, 0, 0, 1, 1, 1},
		{4, 3, 2, 5, 6, 2, 3, 4},
	}
	
	nomeDasPecas := [6]string{
		"Peão",
		"Bispo",
		"Cavalo",
		"Torre",
		"Rainha",
		"Rei",
	}
	
	var totalDeCadaPeca [7]int
	
	for _, fileira := range tabuleiro {
		for _, casa := range fileira {
			totalDeCadaPeca[casa] += 1
		}
	}
	
	for i, total := range totalDeCadaPeca[1:] {
		fmt.Printf("%s: %d peça(s)\n", nomeDasPecas[i], total)
	}
}
