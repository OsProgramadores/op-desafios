#include <algorithm>
#include <iostream>
#include <vector>
#include <string>


void imprimeLista (std::vector<unsigned long long> lista);

int main (void)
{
    unsigned long long limite_inferior, limite_superior;
    std::cin >> limite_inferior >> limite_superior;
    std::vector<unsigned long long> palindromos;
    
    //Todos os numeros abaixo de 10 são palindromos.
    if (limite_inferior < 10)
    {
        for (size_t i = limite_inferior; i < (limite_superior < 10? limite_superior:10); i++)
        {
            std::cout << i << " ";
        }
        
    }

    //Para numeros dois ou mais digitos
    if (limite_superior > 10)
    {
        std::string numero, numero_reverso;
        //11 é o menor palindromo com 2 digitos.
        for (unsigned long long i = ((11 > limite_inferior) ? 11:limite_inferior); i < limite_superior; i++)
        {
            numero = std::to_string (i);
            numero_reverso = numero;
            std::reverse(numero_reverso.begin(), numero_reverso.end());
            if (numero == numero_reverso)
                std::cout << i << " ";
        }
        
    }
    
    std::cout << std::endl;
    
    return 0;
}

//Imprime um vector dado como parametro.
void imprimeLista (std::vector<unsigned long long> lista){
    for (size_t i = 0; i < lista.size(); i++)
    {
        std::cout << lista[i] << " ";
    }
    std::cout << std::endl;
}