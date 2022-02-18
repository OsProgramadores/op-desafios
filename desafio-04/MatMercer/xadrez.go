package main

import (
	"fmt"
	"os"
)

func main() {
	var pecas [7]int

	var b = make([]byte, 1)

	for b[0] != 10 {
		for i := 0; i < 8; i++ {
			os.Stdin.Read(b)

			// ascii table
			var peca = b[0] - 48
			pecas[peca]++

			os.Stdin.Read(b)
		}
		os.Stdin.Read(b)
	}

	fmt.Println("Peão:", pecas[1], "peça(s)")
	fmt.Println("Bispo:", pecas[2], "peça(s)")
	fmt.Println("Cavalo:", pecas[3], "peça(s)")
	fmt.Println("Torre:", pecas[4], "peça(s)")
	fmt.Println("Rainha:", pecas[5], "peça(s)")
	fmt.Println("Rei:", pecas[6], "peça(s)")
}
