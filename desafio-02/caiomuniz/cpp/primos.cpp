#include <iostream>
#include <cmath>
#include <vector>



bool ePrimo (int num);

int main(int argc, char const *argv[])
{
    std::vector<int> primos;
    for (size_t i = 0; i < 10000; i++)
    {
        if (ePrimo(i))
            primos.push_back(i);
        
    }
    
    for (size_t i = 0; i < primos.size(); i++)
    {
        std::cout << primos[i] << " ";
    }
    std:: cout << std::endl;

    return 0;
}

bool ePrimo (int num)
{
    if (num == 2) return true;
    if (num < 2) return false;
    for (size_t i = 2; i <= (unsigned int)sqrt(num); i++)
    {
        if (num % i == 0)
            return false;
    }
    return true;
}