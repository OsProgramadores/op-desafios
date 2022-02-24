package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Uso: xadrez [tabuleiro]")
		fmt.Println("Tabuleiro exemplo:")
		fmt.Println("4 3 2 5 6 2 3 4\n1 1 1 1 1 1 1 1\n0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0\n1 1 1 1 1 1 1 1\n4 3 2 5 6 2 3 4")
		fmt.Println("As new lines devem ser passadas, por exemplo, pelo bash:")
		fmt.Println("$ xadrez \"4 3 2 5 6 2 3 4\\n1 1 1 1 1 1 1 1\\n0 0 0 0 0 0 0 0\\n0 0 0 0 0 0 0 0\\n0 0 0 0 0 0 0 0\\n0 0 0 0 0 0 0 0\\n1 1 1 1 1 1 1 1\\n4 3 2 5 6 2 3 4\"")
		os.Exit(1)
	}

	var pecas [7]int
	var buffer = []byte(os.Args[1])

	var idx = 0
	for idx < len(buffer) {
		for i := 0; i < 8; i++ {
			var bytePeca = buffer[idx]
			idx++

			// ascii table
			var peca = bytePeca - 48
			pecas[peca]++

			idx++
		}
		idx++
	}

	fmt.Println("Peão:", pecas[1], "peça(s)")
	fmt.Println("Bispo:", pecas[2], "peça(s)")
	fmt.Println("Cavalo:", pecas[3], "peça(s)")
	fmt.Println("Torre:", pecas[4], "peça(s)")
	fmt.Println("Rainha:", pecas[5], "peça(s)")
	fmt.Println("Rei:", pecas[6], "peça(s)")
}
