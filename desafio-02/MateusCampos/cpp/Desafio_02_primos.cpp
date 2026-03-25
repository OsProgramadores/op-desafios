#include <iostream>
using namespace std;

int main()
{
    cout << "\nDesafio-02 apresentar numeros primos de 0 a 10000: "; // introducao do desafio-02
    int num_pri, num, contar; // variaveis usadas
    for (num_pri = 2; num_pri <= 10000; num_pri++) // primeira condicao
    {
        contar = 0; // armazenar os numeros de 2 a 10000 na variavel contar
        for (num = 2; num <= num_pri / 2; num++)  // segunda condicao
            if (num_pri % num == 0) // verifica o resto da divisao da variavel 'num' que eh a metade da variavel 'num_pri' eh igual a zero
                contar = 1; // serao armazenados os valores da segunda condicao
        if (contar == 0) // se os numeros sao iguais a 0, entao, eles sao primos
            cout << "\nNumero primo:" << num_pri; // todos os numeros primos serao impressos
    }
    cout << endl;
    return 0;
}