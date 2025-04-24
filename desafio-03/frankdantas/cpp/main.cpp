#include <iostream>
#include <cstdint>
#include <limits>


void clearInput(){
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}
int main(){

    //Mostrar numeros primos
    std::cout << "Numeros palindromos" << std::endl;

    uint64_t startNumber;
    uint64_t endNumber;

    std::cout << "Enter with first number: ";
    std::cin >> startNumber;
    while(!std::cin.good()){
        clearInput();
        std::cout << "Enter with a valid first number: ";
        std::cin >> startNumber;
    }

    std::cout << "Enter with second number: ";
    std::cin >> endNumber;
    while(!std::cin.good()){
        clearInput();
        std::cout << "Enter with a valid second number: ";
        std::cin >> endNumber;
    }

    int amountPalindromes = 0;

    if(startNumber > endNumber){
        std::swap(startNumber, endNumber);
    }

    for(auto i = startNumber; i <= endNumber; ++i){
        int inverseNumber = 0;
        int currentNumber = i;
        //std::cout << "Checking number " << currentNumber << std::endl;
        while(currentNumber > 0){
            inverseNumber = (inverseNumber * 10) + (currentNumber % 10);
            currentNumber /= 10;
        }

        //std::cout << "Inverse of number: " << i << " is " << inverseNumber << std::endl;

        if(inverseNumber == i){
            std::cout << (amountPalindromes == 0 ? "": ", ") << inverseNumber;
            //std::cout << currentNumber << std::endl;

            ++amountPalindromes;
        }
    }

    std::cout << std::endl;

    std::cout << "Amount of palindromes: " << amountPalindromes << std::endl;


    return 0;
}