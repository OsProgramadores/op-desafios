#include <iostream>
#include <string>

// Versão comparando string
void getPalodromicos(size_t a, size_t b)
{
    std::string numero;
    int i, size;
    b++;
    for (; a < b; a++)
    {
        numero = std::to_string(a);
        size = numero.size() / 2 + 1;
        for (i = 0; i < size; i++)
        {
            if (numero[i] != numero[numero.size() - i - 1])
                break;
        }
        if (i == size)
            std::cout << a << std::endl;
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
