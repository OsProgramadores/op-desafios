	#include <stdio.h>
	#define LIMITE 10000 //quantidade de números para testar
	int main(){
		int i=2;
		int div=2;
		int total=0;
		bool isPrimo;
		printf("Lista de números primos:\n");
		while(i<=LIMITE){
			isPrimo=true;
			while(div<i){
				if(i%div==0)
					isPrimo=false;
				div++;
			}
			if(isPrimo){
				printf("%d\n",i);
				total++;
			}
			i++;
			div=2;
		}
		printf("\nTotal de números primos: %d",total);
		return 0;
	}
