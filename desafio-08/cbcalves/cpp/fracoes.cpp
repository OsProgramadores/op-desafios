#include <iostream>

int main()
{
    std::string entrada;
    size_t inteiro, dividendo, divisor, tmp, max = SIZE_MAX, min = 2;
    while (std::cin >> entrada)
    {
        if ((tmp = entrada.find("/")) == std::string::npos) // Se não tem / é um numero inteiro
        {
            std::cout << entrada << std::endl;
            continue;
        }
        dividendo = std::stoul(entrada.substr(0, tmp));
        divisor = std::stoul(entrada.substr(tmp + 1));

        if (divisor == 0) // Divisor sendo 0
        {
            std::cout << "ERR" << std::endl;
            continue;
        }
        inteiro = 0;

        if (dividendo > divisor) // Se o dividendo for maior que o divisor, vai ter inteiro
        {
            if ((tmp = dividendo % divisor) > 0) // tem inteiro
            {
                if ((dividendo % tmp) == 0 && (divisor % tmp) == 0) // tenta reduzir a fração
                {
                    dividendo = dividendo / tmp;
                    divisor = divisor / tmp;
                }
                inteiro = dividendo / divisor;
                dividendo = dividendo % divisor;
            }
        }
        else
        {
            if ((divisor % dividendo) == 0) // tenta reduzir a fração
            {
                inteiro = 0;
                divisor = divisor / dividendo;
                dividendo = 1;
            }
        }

        max = std::min(divisor, dividendo);
        min = 2;
        tmp = 2;
        while (min <= max)
        {
            if ((divisor % max) == 0 && (dividendo % max) == 0)
            {
                tmp = max;
                break;
            }
            if (tmp < min && (divisor % min) == 0 && (dividendo % min) == 0)
                tmp = min;
            max--;
            min++;
        }
        if ((divisor % tmp) == 0 && (dividendo % tmp) == 0)
        {
            divisor = divisor / tmp;
            dividendo = dividendo / tmp;
        }
        entrada = "";
        if (inteiro > 0)
            entrada += std::to_string(inteiro) + " ";
        entrada += std::to_string(dividendo);
        if (divisor > 1)
            entrada += "/" + std::to_string(divisor);
        std::cout << entrada << std::endl;
    }
    return 0;
}
