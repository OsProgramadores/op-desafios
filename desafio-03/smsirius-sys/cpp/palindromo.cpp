#include <iostream>

using namespace std;

int main() {

    int limiteInferior, limiteSuperior;

    cout << "Digite o número inicial: ";
    cin >> limiteInferior;
    cout << "Digite o número final: ";
    cin >> limiteSuperior;

    cout << "Números palindrômicos entre " << limiteInferior << " e " << limiteSuperior << " são:" << endl;

    for (int i = limiteInferior; i <= limiteSuperior; ++i) {
        int num = i;
        int original = num;
        int reverso = 0;

        // Inverte o número
        while (num > 0) {
            reverso = reverso * 10 + (num % 10);
            num /= 10;
        }


        if (original == reverso) {
            cout << i << " ";
        }
    }

    return 0;
}
