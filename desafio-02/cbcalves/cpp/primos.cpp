#include <iostream>
#include <vector>

int main()
{
    std::vector<size_t> primos(4);
    size_t j = 0;
    primos[0] = 2;
    primos[1] = 3;
    primos[2] = 5;
    primos[3] = 7;
    // O passo é de 2 em 2 para testar apenas números impares
    for (size_t i = 11; i < 10000; i += 2)
    {
        // Ganho de velocidade.
        if ((i % 5) == 0 || (i % 3) == 0)
            continue;
        for (j = 3; j < primos.size(); j++)
        {
            // Se não for primo o resto é zero.
            if ((i % primos[j]) == 0)
                break;
            // Se o resultado for menor que o divisor, quer dizer que
            // não tem um primo que multiplicando por outro primo menor 
            // de o número, ele é primo, não vou até o fim da array.
            if ((i / primos[j]) < primos[j])
            {
                j = primos.size();
                break;
            }
        }
        if (j == primos.size())
            primos.push_back(i);
    }
    for (auto &i : primos)
        std::cout << i << "\n";
    std::cout << std::endl;
    return 0;
}

