#include <stdio.h>
	int palindromo( int a);

	int main() {
		int inicio, fim, i;

			while(1) {
				printf("Digite um intervalo de números positivos: ");
				scanf("%d %d", & inicio, & fim);

				//checar se os números são positivos
				if( inicio >= 0 && fim >= 0) {
					//colocando o menor número como começo do intervalo
					if( inicio < fim) {
						for( i = inicio + 1; i <= fim; i++){
							if(palindromo(i)) {
								printf(" %d ", i);
							}
						}
					//se o usuário digitar primeiro o fim do intervalo
					}else{
						for( i = fim + 1; i <= inicio; i++){
							if(palindromo(i)) {
								printf(" %d ", i);
							}
						}
					}
					break;
				//se o número for negativo
				}else{
					printf("Número(s) invalido(s)!\n\n");
				}
			}

		printf("\n");
		return 0;
	}

	//fũnççao para determinar se o número é palíndromo
	int palindromo( int a){
		int invertido = 0, resto, x;

		x = a;

		while( x != 0) {
			resto = x % 10;
			invertido = (invertido * 10) + resto;
			x = x / 10;
		}

		if(invertido == a){
			return 1;
		}
		return 0;

	}