#include<bits/stdc++.h>
#define endl '\n'
#define _ ios_base::sync_with_stdio(0); cin.tie(0);
#define MAX 10000
using namespace std;

// Mostra todos os primos entre 1 e 10000, usando o crivo de eratóstenes
int main() {_
    // Inicialmente todos são
    vector<int> x(MAX+1, 1);
    for (int i = 2; i*i <= MAX; i++) {
        // Se i é primo, então todos os múltiplos de i que são maiores do que i
        // não serão primos
        if (x[i]) {
            for (int j = i*i; j <= MAX; j += i) {
                x[j] = 0;
            }
        }
    }
    cout << 2 << endl;
    for (int i = 3; i <= MAX; i++) {
        if (x[i]) {
            cout << i << endl;
        }
    }
    return 0;
}