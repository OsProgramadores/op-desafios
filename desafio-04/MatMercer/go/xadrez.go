package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		usoEDesliga()
	}

	tabuleiro := os.Args[1]

	validarTabuleiro(tabuleiro)

	var pecas [7]int
	var buffer = []byte(tabuleiro)

	var idx = 0
	for idx < len(buffer) {
		for i := 0; i < 8; i++ {
			var bytePeca = buffer[idx]

			// ascii table
			var peca = bytePeca - 48
			pecas[peca]++

			idx += 2
		}
	}

	fmt.Println("Peão:", pecas[1], "peça(s)")
	fmt.Println("Bispo:", pecas[2], "peça(s)")
	fmt.Println("Cavalo:", pecas[3], "peça(s)")
	fmt.Println("Torre:", pecas[4], "peça(s)")
	fmt.Println("Rainha:", pecas[5], "peça(s)")
	fmt.Println("Rei:", pecas[6], "peça(s)")
}

func validarTabuleiro(tabuleiro string) {
	if len(tabuleiro) != 127 {
		tabuleiroInvalido()
	}

	for _, char := range tabuleiro {
		if char != '\n' && char != ' ' && (char < 48 || char > 54) {
			tabuleiroInvalido()
		}
	}
}

func tabuleiroInvalido() {
	fmt.Printf("\n\nERRO: Tabuleiro inválido\n\n")
	usoEDesliga()
}

func usoEDesliga() {
	fmt.Println("Uso: xadrez [tabuleiro]")
	fmt.Println("\nNo Linux Bash:")
	fmt.Println("xadrez \"$(printf \"4 3 2 5 6 2 3 4\\n1 1 1 1 1 1 1 1\\n0 0 0 0 0 0 0 0\\n0 0 0 0 0 0 0 0\\n0 0 0 0 0 0 0 0\\n0 0 0 0 0 0 0 0\\n1 1 1 1 1 1 1 1\\n4 3 2 5 6 2 3 4\")\"")
	fmt.Println("\nNo Windows Powershell:")
	fmt.Println("xadrez.exe \"4 3 2 5 6 2 3 4`n1 1 1 1 1 1 1 1`n0 0 0 0 0 0 0 0`n0 0 0 0 0 0 0 0`n0 0 0 0 0 0 0 0`n0 0 0 0 0 0 0 0`n1 1 1 1 1 1 1 1`n4 3 2 5 6 2 3 4\"")
	os.Exit(1)
}
