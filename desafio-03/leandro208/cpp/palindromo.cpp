#include <iostream>
#include <string>
#include <vector>
#include <cmath>

bool validar(int* inicio, int* fim){
    bool isPositivo = *inicio >= 1 && *fim >= 1;
    if(isPositivo){
        if(*inicio > *fim){
            int aux = *inicio;
            *inicio = *fim;
            *fim = aux;
        }
        return true;
    }
    return false;
}

int converteParaInteiro(std::vector<int> numeros){
    int tamanho = numeros.size();
    int valor = 0;
    for(int i = 0; i<tamanho; i++){
        valor+=numeros[i]*std::pow(10, tamanho-1-i);
    }
    return valor;
}

void verificaPalindromo(int numero){
   std::vector<int> numeros;
    std::string numeroStr = std::to_string(numero);

    for (char digitoChar : numeroStr) {
        numeros.insert(numeros.begin(), digitoChar - '0');
    }
    int novoValor = converteParaInteiro(numeros);
    
    if(numero==novoValor){
        std::cout<<numero<<std::endl;
    }
}

int main()
{
    int inicio, fim;
    std::cout<<"Digite o Intervalo um numero apos o outro"<<std::endl;
    std::cin>>inicio;
    std::cin>>fim;

    if(validar(&inicio, &fim)){
        for(int i = inicio; i<=fim; i++){
            verificaPalindromo(i);
        }
    }
    return 0;
}

