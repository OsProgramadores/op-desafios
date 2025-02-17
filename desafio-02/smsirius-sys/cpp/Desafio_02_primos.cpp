#include <iostream>

int main() {
    int limite = 10000;

    std::cout << "Números primos entre 1 e " << limite << ":\n";

    for (int num = 2; num <= limite; num++) {
        bool ehPrimo = true;

        for (int divisor = 2; divisor * divisor <= num; divisor++) {
            if (num % divisor == 0) {
                ehPrimo = false;
                break;
            }
        }

        if (ehPrimo) {
            std::cout << num << " ";
        }
    }

    std::cout << std::endl;
    return 0;
}
