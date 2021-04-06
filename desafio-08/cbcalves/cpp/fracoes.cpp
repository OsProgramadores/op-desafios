#include <iostream>

int main()
{
    char c;
    int dividendo;

    while (std::cin >> dividendo) {
        int inteiro;
        int divisor;
        int div_a = 0;
        int div_b = 0;

        if (std::cin.peek() != '/') {
            if (dividendo)
                std::cout << dividendo << std::endl;
            continue;
        }
        std::cin >> c >> divisor;
        // Divisor sendo 0
        if (divisor == 0) {
            std::cout << "ERR" << std::endl;
            continue;
        }
        inteiro = 0;

        // Se o dividendo for maior ou igual ao divisor, vai ter inteiro
        if (dividendo >= divisor) {
            inteiro = dividendo / divisor;
            dividendo = dividendo % divisor;
        }

        // Achar se existe o MDC (Máximo Divisor Comum)
        div_a = dividendo;
        div_b = divisor;
        while (div_b) {
            int resto = div_a % div_b;
            div_a = div_b;
            div_b = resto;
        }
        // Existindo o MDC vai fazer a redução da fração
        dividendo = dividendo / div_a;
        divisor = divisor / div_a;

        if (inteiro)
            std::cout << inteiro;
        if (inteiro && dividendo)
            std::cout << " ";
        if (divisor > 1)
            std::cout << dividendo << "/" << divisor;
        std::cout << std::endl;
    }

    return 0;
}
