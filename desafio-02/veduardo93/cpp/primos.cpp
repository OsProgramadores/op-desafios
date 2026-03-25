#include <iostream>

int main() {
    for (int i = 1; i <= 10000; i++) {
        bool primo = true;

        for (int j = 2; j <= i / 2 && primo; j++)
            if (i % j == 0)
                primo = false;
        if (primo)
            std::cout << i << " ";
    }
}