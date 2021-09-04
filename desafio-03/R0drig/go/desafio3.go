package main

import "fmt"

//funcao que inverte o numero
func inverte(numero int) (numeroInvertido int) {
	for ; numero > 0; numero = numero / 10 {
		digito := numero % 10
		numeroInvertido = numeroInvertido*10 + digito
	}
	return numeroInvertido

}

func main() {
	for i := 1; i <= 100000; i++ {
		if i == inverte(i) {
			fmt.Println(i)
		}
	}
}
