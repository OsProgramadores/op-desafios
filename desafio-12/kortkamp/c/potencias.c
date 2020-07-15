#include <stdlib.h>
#include <stdio.h>

#define FILE_NAME "d12.txt"

FILE* pf;
char number[2000]; //
int pcounter = 0;
int sobra = 0; //sobra da divisao por 2
int indice  =0; //potencia de 2
int nsize = 0; //size o working number
int old = 0;


long zero(){
	//return 1 if the number in string formar is equal to 0
	//return 0 otherwise
	//erro em caso da soma de sum seja overflowed to 0
	int counter = 0;
	long sum = 0;
	while(number[counter] != 0){
		sum += number[counter]-'0';
		counter ++;
	}
	return(sum);
}
int main(int argc, char *argv[]){

	if(argc < 2){
	       	printf("Usage: %s filename\n",argv[0]);
		return(0);
	}
	pf = fopen(argv[1], "r");	
	if(pf == NULL){
		printf("Error opening file %s",argv[1] );
		return(1);
	}
	while(nsize = fscanf(pf,"%s",&number) > 0){
		printf("%s ",number);
		indice = 0;
		if(zero() == 0){
			sobra = -1;
			number[0] = '1';
		}
		while((sobra == 0)){
			
			pcounter = 0;
			sobra = 0;
			while(number[pcounter] != 0){
			
				old = number[pcounter] - '0'; //convert to int
				number[pcounter]  = (10*sobra + old) / 2 ;
				sobra = (10*sobra + old) % 2 ;
	
				number[pcounter] +=  '0'; // convert back to ascii
	
				pcounter ++;
			}

			indice++;
		}
		if(zero() == 0){
			printf("true %d\n",indice-1);
		}else printf("false\n");
		sobra = 0;
	}
	
	return(0);
}
