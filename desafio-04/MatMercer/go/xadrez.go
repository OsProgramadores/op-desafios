package main

import (
	"fmt"
	"io/ioutil"
	"math/rand"
	"os"
	"time"
)

func main() {
	if len(os.Args) != 2 {
		usoEDesliga()
	}

	if "gerar-tabuleiro" == os.Args[1] {
		tabuleiroExemplo()
	} else if "gerar-tabuleiro-gigante" == os.Args[1] {
		tabuleiroGigante()
	}

	var buffer = abrirTabuleiro()

	validarTabuleiro(buffer)
	contarPecas(buffer)
}

func tabuleiroExemplo() {
	fmt.Print("4 3 2 5 6 2 3 4\n1 1 1 1 1 1 1 1\n0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0\n1 1 1 1 1 1 1 1\n4 3 2 5 6 2 3 4")
	os.Exit(0)
}

func tabuleiroGigante() {
	const tamanho = 32
	rand.Seed(time.Now().UnixNano())

	for i := 0; i < tamanho; i++ {
		for j := 0; j < tamanho; j++ {
			fmt.Print(rand.Intn(7))
			if j < tamanho-1 {
				fmt.Print(" ")
			}
		}
		if i < tamanho-1 {
			fmt.Print("\n")
		}
	}

	os.Exit(0)
}

func validarTabuleiro(tabuleiro []byte) {
	for _, char := range tabuleiro {
		if char != '\n' && char != '\r' && char != ' ' && (char < 48 || char > 54) {
			tabuleiroInvalido()
		}
	}
}

func tabuleiroInvalido() {
	fmt.Printf("\n\nERRO: Tabuleiro inválido\n\n")
	usoEDesliga()
}

func abrirTabuleiro() []byte {
	arquivo := os.Args[1]
	buffer, err := ioutil.ReadFile(arquivo)

	if err != nil {
		fmt.Printf("Falha ao abrir o arquivo \"%s\": %s\n", arquivo, err)
		os.Exit(2)
	}

	return buffer
}

func contarPecas(buffer []byte) {
	var pecas [7]int

	var idx = 0
	for idx < len(buffer) {
		var bytePeca = buffer[idx]

		// ascii table
		// transforma um char na distância do número 0 que esse char está, excluindo ' ', '\r' e '\n'
		var peca = bytePeca % '0' % ' ' % '\r' % '\n'
		pecas[peca]++

		idx++
	}

	fmt.Println("Peão:", pecas[1], "peça(s)")
	fmt.Println("Bispo:", pecas[2], "peça(s)")
	fmt.Println("Cavalo:", pecas[3], "peça(s)")
	fmt.Println("Torre:", pecas[4], "peça(s)")
	fmt.Println("Rainha:", pecas[5], "peça(s)")
	fmt.Println("Rei:", pecas[6], "peça(s)")
}

func usoEDesliga() {
	fmt.Println("Uso: xadrez [nome_arquivo]")
	fmt.Println("\nVoce pode gerar o tabuleiro e salvar ele:")
	fmt.Println("xadrez gerar-tabuleiro")
	fmt.Println("\nO programa também aceita tabuleiros de qualquer tamanho:")
	fmt.Println("xadrez gerar-tabuleiro-gigante")
	os.Exit(1)
}
