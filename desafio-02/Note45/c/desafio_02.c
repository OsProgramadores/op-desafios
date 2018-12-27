#include <stdio.h>

	int main() {
		int cont = 0, i, a;

		for(i = 1; i <= 10000; i++) {
			for(a = 1; a <= i; a++){
				if(i % a == 0){
					cont++;
				}
			}
			if(cont == 2) {
				printf("%d ", i);
			}
			cont = 0;
		}

		return 0;
	}