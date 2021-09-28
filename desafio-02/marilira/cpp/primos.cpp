#include <bits/stdc++.h>
using namespace std;
int ePrimo(int n){
	int divisores = 0;
	for(int valor = 1; valor <= n; valor++) if(n%valor == 0) divisores++;
	if(divisores == 2) cout << n << '\n';	
}
int main(){
	for(int i=1; i<=10000; i++) ePrimo(i);
	return 0;
}
