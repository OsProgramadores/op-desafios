#include <vector>
#include <iostream>

class Palindromo {
public:
    unsigned long long int num_inicial;
    unsigned long long int num_final;

    void exibeInfo() {
        std::cout << "Informe os numeros limites para achar os palindromos" << '\n';
        std::cout << "Inserir o numero limite inicial" << '\n';
        std::cin >> num_inicial;
        std::cout << "Inserir o numero limite final" << '\n';
        std::cin >> num_final;
        if (num_final < num_inicial) {
            std::cerr << "Erro: Execute o programa novamente\n";
            std::cerr << "Informe um numero maior que o limite inicial para o limite final\n";
            std::exit(0);
        }
        else if (num_final >= static_cast<unsigned long long int>(-1) ||
            num_inicial >= static_cast<unsigned long long int>(-1)) {
            std::cerr << "Erro: Execute o programa novamente\n";
            std::cerr << "Insira apenas numeros inteiros e positivos\n";
            std::exit(0);
        }
        else if (num_inicial == num_final) {
            std::cerr << "Erro: Execute o programa novamente\n";
            std::cerr << "Insira numeros diferentes\n";
            std::exit(0);
        }
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
    return 0;
}