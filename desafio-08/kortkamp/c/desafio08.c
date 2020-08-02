#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LIMIT 100
#define MAX_NUM_SIZE 100
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
// Faz uma subtração inteira positiva de strings numericas de tamanho arbitrário
// se o resultado for < 0 , retorna -1 else retorna 0
// TODO permitir p uso da mesma string em val e diff  val -= sub 
int subtrair(char *val, char *sub, char *diff){
//	printf("v[0]:%d v[1]:%d val[2]:%d val:%s,size: %d sub:%s\n",val[0], val[1],val[2], val,strlen(val) , sub);
	int val_len = strlen(val); // lenght of val
	int sub_len = strlen(sub); // lenght of sub
//	printf("lens %d %d\n ", val_len,sub_len);
	int val_pos = 0; // position in val
	int sub_pos = 0; // position in pos
	int empresta = 0; // valor a ser emprestado da próxima casa decimal
	if(sub_len > val_len){
		subtrair(sub,val,diff);
		return(-1);
	}
	strcpy(diff,val);
//	printf("1 val[val_pos]:%d , sub[sub_pos]:%d empresta:%d\n",val[val_pos],sub[sub_pos],empresta);
//	shift(val,-'0',val_len);shift(sub,-'0',sub_len);shift(diff,-'0',val_len);// converte cada char numerico para o valor correspondente
//	printf("2 val[val_pos]:%d , sub[sub_pos]:%d empresta:%d\n",val[val_pos],sub[sub_pos],empresta);
	for(int i = sub_len-1; i >= 0; i--){
		val_pos = i+(val_len-sub_len);
		sub_pos = i;
		sub[sub_pos] += empresta;

	//	printf("3 val[%d]:%d , sub[%d]:%d empresta:%d\n",val_pos,val[val_pos],sub_pos,sub[sub_pos],empresta);
		if(val[val_pos] < sub[sub_pos]) {// o digito de sub é maior que o de val
			val[val_pos] += 10; // empresta 1 do próximo
			empresta = 1;
		}else empresta = 0;
		
	//	printf("val[val_pos]:%d , sub[sub_pos]:%d empresta:%d\n",val[val_pos],sub[sub_pos],empresta);
	//	exit(0);
		diff[val_pos] = val[val_pos] - sub[sub_pos];
		if(empresta == 1) {
			val[val_pos] -= 10; 
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
int divide(char *num, char *den, char *quo, char *resto){
	char temp_num[MAX_NUM_SIZE];
	char temp_diff[MAX_NUM_SIZE];
	int result = 0;
	int sub_counter = 0;
	if(den[0] == '0') return(-1); // divisao por zero
	//
	int num_len = strlen(num);
	int den_len = strlen(den);
	int num_pos = den_len;
	if(den_len > num_len){
		strcpy(quo,"0");
		strcpy(resto,num);
		return(0);
	}
	/* vai pegando os pedaços do numerador de tamnhos igual ao denominador*/
	
	strncpy(temp_num,num,den_len);
	printf("size:%d\n", strlen(temp_num));
	while(num_pos <= num_len ){
		printf("1 while %s / %s\n",temp_num,den);
		while(result != -1){
			result = subtrair(temp_num,den,temp_diff);
			printf("temp_num:%s sub_counter:%d result:%d\n", temp_num, sub_counter,result);	
			strcpy(temp_num,temp_diff);
			sub_counter ++;
		}
		sprintf(quo,"%s%d",quo,sub_counter);// contat o resultado parcial ao quociente
		sprintf(temp_num,"%s%c",temp_num,num[num_pos]);// pega mais um dígito do numerador
		num_pos++;
	}
	printf("%s / %s = %s  sobra %s\n",num ,den,quo,resto);
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
	char v1[100] = "654";
	char v2[100] = "89777";
	char r[100];
	int signal = subtrair(v1,v2,r);
//	printf("\nsub:%d(%s)\n",signal,r);
	return(0);
}
