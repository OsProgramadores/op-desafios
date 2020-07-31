#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
14/3
1/2
3/8
237/122
10492/6637
5/25
152/776
917/1008
2/1
120
942/227
197/199
283791739/113312387
13/13
15/0
*/

// shift every element of a string
// shift("a123",2) == "c345"
int shift(char *str, int value,int size){
	int counter = 0;
	while(counter < size) str[counter++] += value;
	return(counter);
}
// Faz uma subtração inteira positiva
// se o resultado for < 0 , retorna -1
// TODO caso negativo retornar a sutração invertida
int subtrair(char *val, char *sub, char *diff){
	int val_len = strlen(val); // lenght of val
	int sub_len = strlen(sub); // lenght of sub
	int val_pos; // position in val
	int sub_pos; // position in pos
	if(sub_len > val_len)return(-1);
	for(int i = 0;i < sub_len;i++)
		if(sub[i] > val[i+(val_len-sub_len)])return(-1);
	
	strcpy(diff,val);
	shift(val,-'0',val_len);shift(sub,-'0',sub_len);shift(diff,-'0',val_len);// converte cada char numerico para o valor correspondente
	for(int i = sub_len-1; i >= 0; i--){
		val_pos = i+(val_len-sub_len);
		sub_pos = i;
		diff[val_pos] = val[val_pos] - sub[sub_pos];
		//printf("%d",diff[val_pos]);
	}
	shift(val,'0',val_len);shift(sub,'0',sub_len);shift(diff,'0',val_len);// desfaz a conversão
	//diff[val_len] = '\0';	
	
	return(0);
}
int divide(char *num, char *den, char *quo, char *resto){
	if(den[0] == '0') return(-1); // divisao por zero
	//
	printf("(%s , %s)\n",num ,den);
	return(0);
}

int main(int argc, char* argv[]){
	
	FILE *fp;
	char line[200] = {0};
	char num[100] = {0};// numerador
	char den[100] = {0};// denominador
	char quo[100];
	char resto[100];
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
		if(sscanf(line,"%[^/]/%s",num,den) == 1){ // apenas um valor na linha
			strcpy(den,"1");
		}
		if(divide(num,den,quo,resto) == -1){
			printf("ERR\n");
		}else{
			// print solution
		}
	}	
	char v1[100] = "192";
	char v2[100] = "192";
	char r[100];
	int signal = subtrair(v1,v2,r);
	printf("\nsub:%d(%s)\n",signal,r);
	return(0);
}
