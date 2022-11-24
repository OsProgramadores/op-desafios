#include <vector>
#include <iostream>

class Palindromo {
public:
    unsigned long long int num_inicial;
    unsigned long long int num_final;

    void exibeInfo() {
        std::cout << "Informe os numeros limites para achar os palindromos" << '\n';
        std::cout << "Obs: Apenas numeros inteiros e positivos" << '\n';
        std::cout << "Inserir o numero limite inicial" << '\n';
        std::cin >> num_inicial;
        std::cout << "Inserir o numero limite final" << '\n';
        std::cin >> num_final;
    }

    bool isPalindromo(unsigned long long int num) {
        unsigned long long int test_palindromo = 0, aux = num, resto;
        while (num > 0) {
            resto = num % 10;
            test_palindromo = (test_palindromo * 10) + resto;
            num = num / 10;
        }
        return aux == test_palindromo;
    }

    void exibePalindromo() {
        std::vector<unsigned long long int> palindromo;
        for (auto i{ num_inicial }; i < num_final; i++) {
            if (isPalindromo(i)) {
                palindromo.push_back(i);
            }
        }

        std::cout << "Numero que sao palindromos entre " << num_inicial << " a " << num_final << " :" << '\n';
        for (auto j : palindromo) {
            std::cout << j << ' ';
        }
        std::cout << '\n';
    }
};

int main() {
    Palindromo palindromo;
    palindromo.exibeInfo();
    palindromo.exibePalindromo();
}