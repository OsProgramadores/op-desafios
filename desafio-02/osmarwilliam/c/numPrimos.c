#include <stdio.h>

int main()
{
    int numero_max = 10000;
    int lista[numero_max]; // para resolver o problema usando o Crivo de Eratóstenes primeiro devemos criar um array com todos os elementos
    for (int i = 0; i < numero_max; i++)
    {
        lista[i] = i + 2; // lista[2..10000]
    }
    printf("%i\n", lista);
    // implementando o Crivo de Eratóstenes
    for (int i = 0; i < numero_max; i++)
        if (lista[i] != 0)
            for (int j = i + lista[i]; j < numero_max; j += lista[i])
            {
                lista[j] = 0; // toda vez que um número for múltiplo irá receber como valor 0
            }
    for (int i = 0; i < numero_max; i++)
        if (lista[i] != 0)
        // no array todo número que não é primo tem o valor de 0, logo iremos excluir esses e imprimir o restante
            printf("%i\n", lista[i]);
    return 0;
}