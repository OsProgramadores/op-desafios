/***
Números palindrômicos.
Um palíndromo é uma palavra ou expressão que pode ser lida da esquerda para a direita ou da direita para a esquerda mantendo o mesmo significado. Um exemplo de palíndromo é a palavra “reviver”.

Neste desafio, a idéia é imprimir todos os números palindrômicos entre dois outros números. Tal como as palavras, os números palindrômicos mantém o mesmo valor se lidos de trás para a frente.

Exemplo 1: Dado o número inicial 1 e número final 20, o resultado seria: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11.

Exemplo 2: Dado o numero inicial 3000 e número final 3010, o resultado seria: 3003.

Para o desafio, assuma:

Apenas inteiros positivos podem ser usados como limites.
Números de um algarismo são palíndromos por definição.
Máximo número: (1 << 64) - 1 (máximo unsigned int de 64 bits).
Bônus: Se o desafio parece fácil demais, implemente um novo tipo de dados para calcular pra qualquer número com precisão arbitrária (limite: 100000 algarismos por número). O uso de bibliotecas matemáticas de precisão arbitrária não será considerado como uma solução válida.
***/

package main

import (
	"fmt"
	"os"
	"strconv"
)

func invertInteger(number int) int {
	numberString := fmt.Sprintf("%d", number)
	var invertedString string
	for i := len(numberString) - 1; i >= 0; i-- {
		temp := fmt.Sprintf("%s%s", invertedString, string(numberString[i]))
		invertedString = temp
	}
	numberInteger, err := strconv.Atoi(invertedString)
	if err != nil {
		fmt.Println(err.Error())
		os.Exit(1)
	}
	return numberInteger
}

// CheckPalindrome : verifies if the integer is the same whether read backwards
func CheckPalindrome(startIndex, endIndex int) []int {
	var results []int
	for index := startIndex; index <= endIndex; index++ {
		inverted := invertInteger(index)
		if inverted == index {
			fmt.Printf("Number %d is palindrome\n", index)
			results = append(results, index)
		}
	}
	return results
}

func checkResults(expectedValues, currentValues []int) {
	if len(expectedValues) != len(currentValues) {
		err := fmt.Errorf("Result sizes mismatches. expected=%v current=%v", expectedValues, currentValues)
		fmt.Println(err.Error())
		os.Exit(1)
	}

	for i, value := range expectedValues {
		if value != currentValues[i] {
			err := fmt.Errorf("Expected %d but found %d", value, currentValues[i])
			fmt.Println(err.Error())
			os.Exit(1)
		}
	}
}

func main() {
	//Exemplo 1: Dado o número inicial 1 e número final 20, o resultado seria: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11.
	palindromes := CheckPalindrome(1, 20)
	expectedResult := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 11}
	checkResults(expectedResult, palindromes)

	//Exemplo 2: Dado o numero inicial 3000 e número final 3010, o resultado seria: 3003.

	palindromes = CheckPalindrome(3000, 3010)
	expectedResult = []int{3003}
	checkResults(expectedResult, palindromes)
}
