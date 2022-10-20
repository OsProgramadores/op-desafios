#include <iostream>
using namespace std;

//Verficacao de numeros palindromicos em classe
class Palindromos
{
private: //O acesso as veriaveis ficaram restritas para que nao seja mudada a extensao da verificacao
    int Numero_inicial; // integer para o numero inicial.
    unsigned long long int Numero_final; //unsigned long long int (2^64 - 1)

public: 
    void getFaixa() //opcao para usuario escolher a faixa de numeros para verificar quais sao palindromicos
    {
        cout << "Escolha a faixa de numeros para verificar a ocorrencia de numeros palindromicos" << endl;
        cout << "\nEntre com o numero inicial: ";
        cin >> Numero_inicial;
        cout << "\nEntre com o numero final: ";
        cin >> Numero_final;
    }
    void Palindromo() //funcao para imprimir a faixa escolhida pelo usuario
    {// todas as variaveis utilizadas no loop devem ser unsigned long long int
        unsigned long long int numero; 
        cout << "\nNumeros palindromos na faixa de " << Numero_inicial << " a " << Numero_final << " sao: " << endl;
        for (numero = Numero_inicial; numero <= Numero_final; numero++) //loop para pesquisar os numeros palindromicos
        {
            unsigned long long int resto, inverso = 0; 
            unsigned long long int palind = numero;
            while (palind) //funcao em loop para inversao dos numeros e verificacao de numeros palindromicos
            {
                resto = palind % 10; // resto obtem o ultimo elemento dos numeros verificados, por exemplo, o numero 23, resto = 23%10 = 3
                inverso = (inverso * 10) + resto; // o resto eh adicionado, por exemplo, o numero 23, inverso(0) = (inverso(0) * 10) + resto(3) = 3
                palind = palind / 10; //numero eh divido por 10, por exemplo, palind = palind(23) / 10 = 2
            } //entao, repetivos = inverso = (inverso(3) * 10) + (2 % 10) = 32
            if (inverso == numero) //comparacao dos numeros palindromicos
            {
                cout << numero << " "; //impressao dos numeros palindromicos
            }
        }
    }
};

int main()
{
    Palindromos Capicua;
    //a funcao getFaixa imprime a faixa determinada pelo usario
    Capicua.getFaixa(); 
    //a funcao pesquisa quais os numeros palindromicos e imprime os que foram encontrados
    Capicua.Palindromo();

    return 0;
}