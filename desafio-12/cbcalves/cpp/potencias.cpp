#include <cmath>
#include <iostream>

int main()
{
    std::string entrada;
    size_t potencia = 0, resto = 0, numero;
    bool dedois = true;
    while (std::cin >> entrada)
    {
        potencia = 0;
        resto = 0;
        dedois = true;
        std::cout << entrada << " ";
        while (entrada != "1")
        {
            if (entrada.length() < 19) //acelerar o processo faltando pouco.
            {
                //solução matemática para saber a potencia de 2: 2^x = y -> log(y) / log(2) = x
                numero = log(std::stoul(entrada)) / log(2);
                //como é um tipo sem casas decimais, faço a conta para saber se é potencia de um numero natural
                dedois = (pow(2, numero) == std::stoul(entrada));
                potencia += numero;
                break;
            }
            for (auto &i : entrada)
            {
                numero = (resto * 10) + (i - '0');
                resto = numero % 2;
                i = (numero / 2) + '0';
            }
            if (resto > 0) // não pode ter resto de divisão
            {
                dedois = false;
                break;
            }
            if (entrada[0] == '0') // retira o 0 à esquerda
                entrada = entrada.substr(1);
            potencia++;
        }

        if (dedois)
            std::cout << "true " << potencia << std::endl;
        else
            std::cout << "false" << std::endl;
    }
    return 0;
}
