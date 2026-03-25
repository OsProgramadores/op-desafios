#include <iostream>

constexpr int MAX{ 10000 };

int TestePrimo(int n) {
    for (auto i{ 2 }; i < n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    for (auto i{ 0 }; i < MAX; i++) {
        if (i > 1) {
            if (TestePrimo(i)) {
                std::cout << i << '\n';
            }
        }
    }
}