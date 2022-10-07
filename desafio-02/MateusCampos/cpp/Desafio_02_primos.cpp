#include <iostream>
using namespace std;

int main()
{
    cout << "Desafio-02 apresentar numeros primos de 0 a 10000" << endl; // introducao do desafio-02
    int num_pri, num, total = 10000, divisor; // variaveis a serem usadas
    
    for (num_pri = 2; num_pri <= total; num_pri++) //primeira condicao
    {
        divisor = 0; // armazenar os numeros de 2 a 10000 na variavel 'divisor' 

        for (num = 2; num <= num_pri/2; num++) //segunda condicao
            if (num_pri % num == 0) //verifica o resto da divisao da variavel 'num' que eh a metade da variavel 'num_pri' eh igual a zero
                divisor++; //os numeros sao incrementados dentro dos valores armazenados da primeira condicao

                if (divisor == 0) //se os numeros sao iguais a 0, entao, eles sao primos
                    cout << num_pri << " "; //todos os numeros primos sao impressos
    }
    cout << endl;
    return 0;
}
