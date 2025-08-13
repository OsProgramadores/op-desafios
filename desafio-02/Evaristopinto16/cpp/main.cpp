#include "iostream"

int VerificandoEprimo(int n) {
    if (n <= 1) {
        return 0;
    }
     if (n <= 3) {
        return 1;
    }
    if (n % 2 == 0 || n % 3 == 0) {
        return 0;
    }
    
   for (int i = 5; i * i <= n; i += 2) {
        if (n % i == 0) {
            return 0;
        }
    }
    
 return 1;
}
void ListarPrimos(int inicio, int fim) {
    for (int i = inicio; i <= fim; i++) {
        if (VerificandoEprimo(i) == 1) {
            std::cout << i << std::endl;
        }
    }
}
int main() {
    int iniciaNumero = 0;
    int finalNumero = 10000;
    ListarPrimos(iniciaNumero, finalNumero);
}
