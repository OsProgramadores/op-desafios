#include <stdio.h>
#include <math.h>

int main()
{
    char numero[5];
    char inverso[5];
    for (int i = 1; i <= 3010; i++) {
        sprintf(numero, "%d", i);
        sprintf(inverso, "%d", i);
        strrev(inverso);

        if (strcmp(numero, inverso) == 0) {
            printf("%d\n", i);
        }
    }

    return 0;
}