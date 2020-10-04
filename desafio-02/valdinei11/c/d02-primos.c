#include <stdio.h>
// Autor: Valdinei Ferreira
// Link Repl.It: https://repl.it/GrG9/latest

int main() {
    int num, x, divs;

    // Estrutura FOR para verificar de NUM em NUM
    for(num=2;num<10000;num++) {
        divs = 0;

        // Laço WHILE para verificar enquanto houver outro divisor além de 1 e o próprio número
        for (x=2; x<num; x++) {
            if (num%x == 0) {
            	divs = 1;
                break; // BREAK quando encontrar um divisor, já que 1 e o próprio número não estarão incluídos no intervalo
        	}
        }

        if (!divs) // Se não houver divisor, printar na tela
        	printf("%i\n", num);
    }

    return(0);
}
