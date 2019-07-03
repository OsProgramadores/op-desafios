//Ṕrograma para verificar se um número é palíndromo, e caso seja imprimir esse número
#include <stdio.h>
 
int main(){
	int num,cont,inv_num,resto;
 		for (num = 0; num < 10000; num++){
 		scanf("%d",&num);
 		cont = num;
 		inv_num = 0;
	
		while(cont != 0){
    			resto = cont % 10;
    			inv_num = (inv_num * 10) + resto;
    			cont = cont / 10;
 	}
 		if(num == inv_num)
    			printf("%d\n",num);
	}
}
