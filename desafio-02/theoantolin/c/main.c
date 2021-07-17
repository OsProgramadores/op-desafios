#include <stdio.h>
#include <stdlib.h>

int main() {

int num, x, resultado;
char naoprimo = ' ';

    for(num = 2; num <= 10000; num++) {
        resultado = 0;

        for(x = 1; x <= num; x++)

        if((num % x) == 0)
            resultado++;

        if(resultado > 2)
            printf("%c", naoprimo);
        else
            printf("%d PRIMO ", num);

    }
return 0;
}
