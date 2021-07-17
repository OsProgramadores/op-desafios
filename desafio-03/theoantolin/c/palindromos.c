#include <stdio.h>
#include <stdlib.h>

int main () {

int num, invertido, aux;

	printf("A lista a seguir contem os numeros palindromicos entre 1 e 100000:\n");

	for(num = 1; num <= 100000; num++) {

		// Declaração da variável invertido com o valor zero. Essa variável será utilizada no cálculo de cada número junto de uma váriavel auxiliar (aux).
		invertido = 0;

		// Como devemos verifcar os valores dos números que são palíndromos, devemos preservar a variável num[] e utilizar a variável aux nos cálculos.
		aux = num;

		/* Cálculo do número invertido */
		while (aux > 0) {
			invertido = (invertido * 10) + (aux % 10);
			aux = aux / 10;
		}

		// Números palíndrômicos entre 1 e 100000.
		if (num == invertido) {
			printf("%d\t", num);
		}
	}
return 0;
}
