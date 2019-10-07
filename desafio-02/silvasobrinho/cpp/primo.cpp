#include <iostream>

using namespace std;

int main() {
    int cont = 0;

    for(int i = 2; i <= 10000;i++) {
        for(int j = i/2; j > 1; j--) { 
            if(i % j == 0 ) {
                cont++;
            }
        }
        if (cont == 0) {
            cout << i << endl;
        }
        cont = 0;
    }

    return 0;
}