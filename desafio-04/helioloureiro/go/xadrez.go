/***
 * Contabilizar Peças de Xadrez.
O xadrez é um jogo de tabuleiro estratégico, disputado por dois jogadores e que consiste em um tabuleiro com um arranjo de 8 linhas e colunas formando 64 posições diferentes como uma matriz [8 x 8]. Existem 6 diferentes tipos de peças no xadrez e cada tipo possui uma quantidade (destacada por parênteses):

Peão (8)
Bispo (2)
Cavalo (2)
Torre (2)
Rainha (1)
Rei (1)
Um tabuleiro completo possui trinta e duas peças. Cada tipo de peça, segundo a ordem que aparecem, receberão um código (ex.: peão = 1, bispo = 2, …, rei = 6 e o vazio = 0).

Neste desafio, você deverá contabilizar e exibir a quantidade de cada peça em um tabuleiro de xadrez sem usar estruturas condicionais ou de múltipla escolha (sem *if*s, else e switch case).
***/

package main

import (
	"fmt"
	"os"
)

func getPieceByID(pieceID int) string {
	/*
	  Peão (8)
	  Bispo (2)
	  Cavalo (2)
	  Torre (2)
	  Rainha (1)
	  Rei (1)
	*/
	chessID := map[int]string{
		1: "Peão",
		2: "Bispo",
		3: "Cavalo",
		4: "Torre",
		5: "Rainha",
		6: "Rei"}
	if pieceID < 1 {
		return ""
	}
	if pieceID > 6 {
		return ""
	}
	return chessID[pieceID]
}

func initMap() map[string]int {
	pieces := []string{"Peão", "Bispo", "Cavalo", "Torre", "Rainha", "Rei"}
	result := make(map[string]int)
	for _, name := range pieces {
		result[name] = 0
	}
	return result
}

func countingChess(chessTable [][]int) map[string]int {
	result := initMap()
	for row := 0; row < len(chessTable); row++ {
		for col := 0; col < len(chessTable[row]); col++ {
			piece := chessTable[row][col]
			pieceName := getPieceByID(piece)
			if pieceName != "" {
				result[pieceName]++
			}
		}
	}
	return result
}

func checkMap(result1, result2 map[string]int) {
	for key, value := range result1 {
		if result2[key] != value {
			err := fmt.Errorf("Para %s era esperado valor %d mas encontrou %d", key, value, result2[key])
			fmt.Println(err.Error())
			os.Exit(1)
		}
	}
}

func printResult(result map[string]int) {
	for i := 0; i < len(result); i++ {
		pieceName := getPieceByID(i + 1)
		fmt.Printf("%s: %d peça(s)\n", pieceName, result[pieceName])
	}
	fmt.Println()
}

func checkExemplos() {
	/***
	  Exemplo 1
	  Entrada
	  0 0 0 0 0 0 0 0
	  0 0 0 0 0 0 0 0
	  0 0 0 0 0 0 0 0
	  0 0 0 1 1 0 0 0
	  0 0 0 1 1 0 0 0
	  0 0 0 0 0 0 0 0
	  0 0 0 0 0 0 0 0
	  0 0 0 0 0 0 0 0
	  Saída
	  Peão: 4 peça(s)
	  Bispo: 0 peça(s)
	  Cavalo: 0 peça(s)
	  Torre: 0 peça(s)
	  Rainha: 0 peça(s)
	  Rei: 0 peça(s)
	  Exemplo 2
	  Entrada
	  4 3 2 5 6 2 3 4
	  1 1 1 1 1 1 1 1
	  0 0 0 0 0 0 0 0
	  0 0 0 0 0 0 0 0
	  0 0 0 0 0 0 0 0
	  0 0 0 0 0 0 0 0
	  1 1 1 1 1 1 1 1
	  4 3 2 5 6 2 3 4
	  Saída
	  Peão: 16 peça(s)
	  Bispo: 4 peça(s)
	  Cavalo: 4 peça(s)
	  Torre: 4 peça(s)
	  Rainha: 2 peça(s)
	  Rei: 2 peça(s)
	  ***/

	tabuleiro1 := [][]int{
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 1, 1, 0, 0, 0},
		{0, 0, 0, 1, 1, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0}}

	saida1 := map[string]int{
		"Peão":   4,
		"Bispo":  0,
		"Cavalo": 0,
		"Torre":  0,
		"Rainha": 0,
		"Rei":    0}

	result1 := countingChess(tabuleiro1)
	checkMap(result1, saida1)
	fmt.Println("Exemplo 1")
	printResult(result1)

	tabuleiro2 := [][]int{
		{4, 3, 2, 5, 6, 2, 3, 4},
		{1, 1, 1, 1, 1, 1, 1, 1},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{1, 1, 1, 1, 1, 1, 1, 1},
		{4, 3, 2, 5, 6, 2, 3, 4}}
	saida2 := map[string]int{
		"Peão":   16,
		"Bispo":  4,
		"Cavalo": 4,
		"Torre":  4,
		"Rainha": 2,
		"Rei":    2}

	result2 := countingChess(tabuleiro2)
	checkMap(result2, saida2)
	fmt.Println("Exemplo 2")
	printResult(result2)

}

func main() {
	checkExemplos()
}
