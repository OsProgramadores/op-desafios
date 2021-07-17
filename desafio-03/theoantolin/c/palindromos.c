#include <stdio.h>
#include <stdlib.h>

int main () {

int num, invertido, aux;

	printf("A lista a seguir contem os numeros palindromicos entre 1 e 100000:\n");

	for(num = 1; num <= 100000; num++) {

		// Declara��o da vari�vel invertido com o valor zero. Essa vari�vel ser� utilizada no c�lculo de cada n�mero junto de uma v�riavel auxiliar (aux).
		invertido = 0;

		// Como devemos verifcar os valores dos n�meros que s�o pal�ndromos, devemos preservar a vari�vel num[] e utilizar a vari�vel aux nos c�lculos.
		aux = num;

		/* C�lculo do n�mero invertido */
		while (aux > 0) {
			invertido = (invertido * 10) + (aux % 10);
			aux = aux / 10;
		}

		// N�meros pal�ndr�micos entre 1 e 100000.
		if (num == invertido) {
			printf("%d\t", num);
		}
	}
return 0;
}
