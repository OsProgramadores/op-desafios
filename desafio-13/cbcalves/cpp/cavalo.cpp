#include <iomanip>
#include <iostream>

class Cavalo
{
private:
    int tabuleiro; // tamanho do tabuleiro default:8 x 8
    // tabluleiro
    int **xadrez;
    // movimentos possíveis a partir da posição atual do cavalo (se ele estiver no meio do tabuleiro)
    // depois faz-se a avaliação se estiver perto das bordas
    const int xPulo[8] = {2, 1, -1, -2, -2, -1, 1, 2};
    const int yPulo[8] = {1, 2, 2, 1, -1, -2, -2, -1};
    unsigned int init_x, init_y;
    void destruir()
    {
        if (xadrez)
        {
            for (int i = 0; i < tabuleiro; i++)
            {
                if (xadrez[i])
                    delete[] xadrez[i];
            }
            delete[] xadrez;
        }
    }
    bool passeio(unsigned int x, unsigned int y, int passos)
    {
        unsigned int prox_x = 0, prox_y = 0;
        if (passos == tabuleiro * tabuleiro) // chegou no último passo, tabuleiro completo
            return true;

        for (int i = 0; i < 8; i++) // irá testar recursivamente todos os movimentos possíveis, brute force
        {
            prox_x = x + xPulo[i];
            prox_y = y + yPulo[i];
            if (prox_x < tabuleiro && prox_y < tabuleiro && xadrez[prox_x][prox_y] == -1)
            {
                xadrez[prox_x][prox_y] = passos;
                if (passeio(prox_x, prox_y, passos + 1) == true)
                    return true;
                else
                    xadrez[prox_x][prox_y] = -1; // falhou, retorna o movimento e testa o proximo
            }
        }
        return false;
    }

public:
    Cavalo(unsigned int x = 0, unsigned int y = 0, int size = 8) : tabuleiro(size), xadrez(nullptr), init_x(x), init_y(y)
    {
        xadrez = new int *[tabuleiro];
        if (!xadrez)
            return;
        for (int x = 0; x < tabuleiro; x++) // prepara o tabuleiro
        {
            xadrez[x] = nullptr;
            xadrez[x] = new int[tabuleiro];
            if (!xadrez[x])
            {
                destruir();
                return;
            }
            for (int y = 0; y < tabuleiro; y++)
                xadrez[x][y] = -1;
        }
        if (init_x < tabuleiro && init_y < tabuleiro)
            xadrez[init_x][init_y] = 0; // posição inicial outra
        else
            xadrez[(init_x = 0)][(init_y = 0)] = 0; // posição inicial a1 = x[0] e y[0]
    }
    ~Cavalo() { destruir(); }
    bool passeio()
    {
        if (xadrez)
            return passeio(init_x, init_y, 1);
        return false;
    }
    void mostrar()
    {
        char letras[] = "abcdefgh";
        if (!xadrez)
            return;
        char passos[tabuleiro * tabuleiro][3];
        for (int x = tabuleiro - 1; x > -1; x--) // mostrar o tabuleiro e guardar a ordem dos passos
        {                                        // o problema não pede o tabuleiro mas eu achei interessante ver ele
            for (int y = 0; y < tabuleiro; y++)
            {
                std::cout << std::setw(3) << (xadrez[y][x] + 1) << " ";
                passos[xadrez[x][y]][0] = letras[x];
                passos[xadrez[x][y]][1] = '1' + y;
                passos[xadrez[x][y]][2] = 0;
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
        for (auto s : passos) // mostrar os passos
            std::cout << std::setw(3) << s << std::endl;
    }
};

int main(int argc, char *argv[])
{
    unsigned int init_x = 0, init_y = 0;

    if (argc > 1) // mudança da posição inicial, existem posições que vão levar muito tempo
    {
        init_x = argv[1][0] - 'a';
        init_y = argv[1][1] - '1';
        if (!(init_x < 8 && init_y < 8))
            init_x = init_y = 0;
    }

    Cavalo cavalo(init_x, init_y); // não vou mudar o tamanho do tabuleiro apesar da classe feita aceitar

    if (cavalo.passeio() == false)
        std::cout << "Não foi possível encontrar solução";
    else
        cavalo.mostrar();

    return 0;
}
