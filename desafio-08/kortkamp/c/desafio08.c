/* Solução para o Desafio 08 em https://osprogramadores.com
 * Ao invés de facilitar e coisas e trabalhar convertendo as
 * strings para long ints, decidi implementar funções para
 * trabalhar com strings numéricas de qualquer tamanho.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TRUE -1
#define FALSE 0
#define MAX_NUM_SIZE 100

// Verefica se uma string numérica é igual a zero
// bool: Se igual a zero retorna -1, se não retorna 0
int zero(char *num){
	int pos = 0;
	while(num[pos] != '\0'){
		if(num[pos] != '0') return(FALSE);
		pos++;
	}
	return(TRUE);
}

// clear zeroes in left of a value
// e remove a caspa do cristiano ronaldo
int clear_zero(char *val){
	while(val[0] == '0') strcpy(val,val+1);
	if(val[0] == '\0') strcpy(val,"0"); 	// mantém ao menos 1 zero 
	return(0);
}

// shift every element of a string
// shift("a123",2,size) == "c345"
// usada para converter strings em arrays de inteiros
int shift(char *str, int value,int size){
	int counter = 0;
	while(counter < size) str[counter++] += value;
	return(counter);
}

// Faz uma subtração inteira positiva de strings numericas de tamanho arbitrário
// se o resultado for < 0 , retorna -1 else retorna 0
// TODO permitir o uso da mesma string em val e diff  val -= sub 
// falha de segmentação quando chamado com subtrair("123","12",var)
// a função previsa ser muito otimizada, está horrorosa.
int subtrair(char *val, char *sub, char *diff){
	clear_zero(val);
	clear_zero(sub);
	
	int val_len = strlen(val); // lenght of val
	int sub_len = strlen(sub); // lenght of sub
	int val_pos = 0; // position in val
	int sub_pos = 0; // position in pos
	int empresta = 0; // valor a ser emprestado da próxima casa decimali
	int emprestou = 0;
	if(sub_len > val_len){
		subtrair(sub,val,diff);
		return(-1);
	}
	strcpy(diff,val);
	shift(val,-'0',val_len);shift(sub,-'0',sub_len);shift(diff,-'0',val_len);// converte cada char numerico para o valor correspondente
	for(int i = sub_len-1; i >= 0; i--){
		val_pos = i+(val_len-sub_len);
		sub_pos = i;
		sub[sub_pos] += empresta;// emprestou 1 para o anterior
		emprestou = empresta;
		if(val[val_pos] < sub[sub_pos]) {// o digito de sub é maior que o de val
			val[val_pos] += 10; // empresta 1 do próximo
			empresta = 1;
		}else empresta = 0;
		diff[val_pos] = val[val_pos] - sub[sub_pos];
		sub[sub_pos] -= emprestou;		
		if(empresta == 1) {
			val[val_pos] -= 10; 
		}
	}
	if(empresta == 1){
		for(int i = (val_len - sub_len- 1); i >= 0 ; i--){
			if(diff[i] == 0){
				diff[i] = 9;
			}else if(diff[i] >=  empresta) {
				diff[i] --;
				empresta = 0;
			}	
		}			

	}
	shift(val,'0',val_len);shift(sub,'0',sub_len);shift(diff,'0',val_len);// desfaz a conversão
	if(empresta == 1){
		subtrair(sub,val,diff);
		return(-1);	
	}
	return(0);
}

// Faz uma divisão de inteiros de tamanho arbitrário
// precisa ser imensamente otimizada
int divide(char *num, char *den, char *quo, char *resto){
	char temp_num[MAX_NUM_SIZE];
	char temp_diff[MAX_NUM_SIZE];
	int result = 0;
	int sub_counter = 0;
	if(den[0] == '0') return(-1); // divisao por zero
	int num_len = strlen(num);
	int den_len = strlen(den);
	int num_pos = den_len;
	
	quo[0] = '\0';	
	if(den_len > num_len){
		strcpy(quo,"0");
		strcpy(resto,num);
		return(0);

	}
	/* vai pegando os pedaços do numerador de tamanhos igual ao denominador*/
	strncpy(temp_num,num,den_len);
	temp_num[den_len] = '\0';	
	strcpy(resto,num);	
	while(num_pos <= num_len ){
		sub_counter = 0;
		while(result != -1){
			result = subtrair(temp_num,den,temp_diff);
			if(result != -1){	
				strcpy(temp_num,temp_diff);
				strcpy(resto,temp_num);
				sub_counter ++;
			}
			strcpy(resto,temp_num);
		}
		result = 0;
		sprintf(quo,"%s%d",quo,sub_counter);// contat o resultado parcial ao quociente
		sprintf(temp_num,"%s%c",temp_num,num[num_pos]);// pega mais um dígito do numerador
		num_pos++;
	}
	clear_zero(quo);
	clear_zero(resto);
	return(0);
}

// Retorna o MDC de dois números 
// usando o algoritmo de Euclides
int mdc(char *val1 , char *val2, char *mdc_val){
	char temp1[MAX_NUM_SIZE];
	char temp2[MAX_NUM_SIZE];
	char quo[MAX_NUM_SIZE];

	strcpy(temp1,val1);
	strcpy(temp2,val2);

	while(zero(temp2) == FALSE){
		divide(temp1,temp2,quo,mdc_val);
		strcpy(temp1,temp2);
		strcpy(temp2,mdc_val);
	}
	strcpy(mdc_val,temp1);
}

int main(int argc, char* argv[]){
	
	FILE *fp;
	char line[MAX_NUM_SIZE *2 + 1] = {0};// buffer de linha lida do arquivo
	char num[MAX_NUM_SIZE];// numerador
	char den[MAX_NUM_SIZE];// denominador
	char quo[MAX_NUM_SIZE];// quociente da divisão
	char resto[MAX_NUM_SIZE];// resto da divisão
	char val1[MAX_NUM_SIZE];
	char val2[MAX_NUM_SIZE];
	char mdc_val[MAX_NUM_SIZE];// armazena o mdc

	if(argc != 2){
		fprintf(stderr, "Usage: %s filename", argv[0]);
		return(-1);
	}
	fp = fopen(argv[1], "r");
	if(fp == NULL){
		perror("Error opening file");
		return(-1);
	}	
	while(fscanf(fp, "%s", line) != EOF){
		if(ferror(fp)){
			perror("Error reading file");
			return(-1);	
		}
		if(sscanf(line,"%[^/]/%s",num,den) == 1){ // leu apenas um valor na linha
			strcpy(den,"1");
		}
		mdc(num,den,mdc_val);
		divide(num,mdc_val,val1,resto);
		divide(den,mdc_val,val2,resto);
		strcpy(num,val1);
		strcpy(den,val2);
		
		if(divide(num,den,quo,resto) == -1){
			printf("ERR\n");
		}else{
			// print solution
			clear_zero(quo);
			clear_zero(resto);
			
			if(quo[0] != '0')// se o primeiro algarismo for zero não imprima
				printf("%s ",quo);
			if(resto[0] != '0')// se o numerador for zero , não imprima
				printf("%s/%s",resto,den);
			printf("\n");
		}
	}	
	return(0);
}
