#include <iostream>

#define LIMITE_MUDABASE 30 //zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz

bool limite(std::string, int);
std::string mudabase(std::string &, int, int);

int main()
{
    int base_in, base_out, aux;
    std::string entrada;
    while (std::cin >> base_in >> base_out >> entrada)
    {
        std::cout << mudabase(entrada, base_in, base_out) << std::endl;
    }
    return 0;
}

bool limite(std::string entrada, int base_in)
{
    entrada = mudabase(entrada, base_in, 62);
    if (entrada == "???")
        return true;
    return false;
}

std::string mudabase(std::string &entrada, int base_in, int base_out)
{
    std::string bases = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    std::string saida;
    size_t numero = 0, resto = 0;
    int aux;
    // O limite é dado pela criatividade de completar a string bases, não tem limite no calculo,
    // exceto pelo limite de memória para o tipo string. Para esse desafio foi 62.
    // Existe impossibilidade matemática em fazer base 1 e base 0.
    // zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
    if (base_in > bases.length() || base_out > bases.length() || base_out < 2 || base_in < 2)
        return "???";

    // Não é necessário mas o resultado vai ser 0 mesmo.
    if (entrada == "0")
        return entrada;

    if (base_out < 62 && limite(entrada, base_in))
        return "???";

    saida = "";

    while (entrada != "" && saida != "???")
    {
        resto = 0;
        for (auto &i : entrada)
        {
            aux = bases.find(i);
            // Se não achar o simbolo ou o numero for maior que a base, da erro.
            if (aux == std::string::npos || aux >= base_in)
                return "???";
            numero = (resto * base_in) + aux;
            resto = numero % base_out;
            i = bases[(numero / base_out)];
        }
        saida = bases[resto] + saida;
        while (entrada[0] == '0') // retira o 0 à esquerda.
            entrada = entrada.substr(1);
    }
    if (base_out == 62)
    {
        if (saida.length() > LIMITE_MUDABASE)
            saida = "???";
    }
    return saida;
}
