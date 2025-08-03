#include "iostream"
#include "vector"
using namespace std;
int VerificandoEprimo(int n) {
    if (n <= 1) return 0;     
    if (n <= 3) return 1;    
    if (n % 2 == 0 || n % 3 == 0) return 0;  
 for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return 0;  }}
    return 1; }
 void ListarPrimos(int inicio, int fim){
for (int i = inicio; i <= fim; i++)
    {
if(VerificandoEprimo(i) == 1){
                cout<<i;}
    }}
int main(){
    int iniciaNumero, finalNumero;
    iniciaNumero = 0;
    finalNumero = 1000;
    ListarPrimos(iniciaNumero, finalNumero);

}
