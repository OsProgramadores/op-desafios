#include <iostream>
#include <vector>

void getXadrez(const std::vector<int> &xadrez, const std::string &peca, int numero)
{
    int i = 0, k = 0;
    for (; k < 64; k++)
        while (k < 64 && xadrez[k] == numero) // Loops realizam condicionais para entrar ou continuar
        {
            i++;
            k++;
        }
    std::cout << peca <<": " << i << " peça(s)" << std::endl;
}

int main()
{
    std::vector<int> xadrez(64);

    for (auto &i : xadrez)
        std::cin >> i;

    getXadrez(xadrez, "Peão", 1);
    getXadrez(xadrez, "Bispo", 2);
    getXadrez(xadrez, "Cavalo", 3);
    getXadrez(xadrez, "Torre", 4);
    getXadrez(xadrez, "Rainha", 5);
    getXadrez(xadrez, "Rei", 6);
    return 0;
}

