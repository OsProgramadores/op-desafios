#include "iostream"
bool VerificandoEprimo(int n) {
    if (n <= 1) {
        return false;
    }
     if (n <= 3) {
        return true;
    }
    if (n % 2 == 0 || n % 3 == 0) {
        return false;
    }
    for (int i = 5; i * i <= n; i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
     return true;
}
void ListarPrimos(int inicio, int fim) {
    for (int i = inicio; i <= fim; i++) {
        if (VerificandoEprimo(i)) {
            std::cout << i << std::endl;
        }
    }
}
int main() {
    int iniciaNumero = 0;
    int finalNumero = 10000;
    ListarPrimos(iniciaNumero, finalNumero);
}
