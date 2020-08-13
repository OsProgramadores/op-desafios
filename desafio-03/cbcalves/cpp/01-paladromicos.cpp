#include <iostream>

// Versão invertendo o numero
void getPalodromicos(size_t a, size_t b)
{
    size_t palo, atual;
    b++;
    for (; a < b; a++)
    {
        atual = a;
        palo = 0;
        do
        {
            palo = palo * 10 + atual % 10;
            atual = atual / 10;
        } while (atual > 0);
        if (palo == a)
            std::cout << palo << std::endl;
    }
}

int main()
{
    size_t inicio, final;
    std::cin >> inicio >> final;
    if (inicio > final)
        return 0;
    getPalodromicos(inicio, final);
    return 0;
}

