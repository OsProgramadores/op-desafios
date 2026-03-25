#include <cmath>
#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>

bool testPotencia2(std::string n) {
    _Float64x testa;
    std::stringstream num{ n };
    num >> testa;
    if (testa == 0) {
        return false;
    }
    while (testa > 0) {
        testa = testa / 2;
        if (static_cast<int64_t>(testa) % 2 != 0 && testa != 1) {
            return false;
        }
    }
    return true;
}

int main(int argc, char const* argv[]) {
    std::string numArq;
    std::ifstream potenciaArq(argv[1]);
    std::vector<std::string> numeros;

    if (!potenciaArq.is_open()) {
        std::cout << "Erro ao abrir o arquivo" << '\n';
        return 1;
    }

    while (potenciaArq >> numArq) {
        numeros.push_back(numArq);
    }

    for (auto j : numeros) {
        _Float64x expoenteDe2;
        if (testPotencia2(j)) {
            expoenteDe2 = logf64x(std::stold(j)) / log(2);
            std::cout << j << " true " << expoenteDe2 << '\n';
        }
        else {
            std::cout << j << " false" << '\n';
        }
    }

    return 0;
}