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

// clear zeroes in left of a value
// e remove a caspa do cristiano ronaldo
int clear_zero(char *val){
	while(val[0] == '0') strcpy(val,val+1);
	if(val[0] == '\0') strcpy(val,"0"); 	// mantém ao menos 1 zero 
	return(0);
}

// shift every element of a string
// shift("a123",2) == "c345"
int shift(char *str, int value,int size){
	//printf("shift:%s value:%d size:%d\n",str,value,size);
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
	
//	printf("subtrair val:%s,size: %d sub:%s size:%d\n", val,strlen(val) , sub,strlen(sub));
	int val_len = strlen(val); // lenght of val
	int sub_len = strlen(sub); // lenght of sub
//	printf("lens %d %d\n ", val_len,sub_len);
	int val_pos = 0; // position in val
	int sub_pos = 0; // position in pos
	int empresta = 0; // valor a ser emprestado da próxima casa decimali
	int emprestou = 0;
	if(sub_len > val_len){
		subtrair(sub,val,diff);
		return(-1);
	}
	strcpy(diff,val);
	
//printf("sub:%s.\n",sub);	
	shift(val,-'0',val_len);shift(sub,-'0',sub_len);shift(diff,-'0',val_len);// converte cada char numerico para o valor correspondente
//for(int i = 0; i < sub_len; i++) printf("%d",sub[i]);printf("\n");
	for(int i = sub_len-1; i >= 0; i--){
		val_pos = i+(val_len-sub_len);
		sub_pos = i;
		sub[sub_pos] += empresta;// emprestou 1 para o anterior
		emprestou = empresta;
//		printf("	3 val[%d]:%d , sub[%d]:%d empresta:%d\n",val_pos,val[val_pos],sub_pos,sub[sub_pos],empresta);
		if(val[val_pos] < sub[sub_pos]) {// o digito de sub é maior que o de val
			val[val_pos] += 10; // empresta 1 do próximo
			empresta = 1;
		}else empresta = 0;
		
	//	printf("	val[val_pos]:%d , sub[sub_pos]:%d empresta:%d\n",val[val_pos],sub[sub_pos],empresta);
	//	exit(0);
		diff[val_pos] = val[val_pos] - sub[sub_pos];
		sub[sub_pos] -= emprestou;		
		if(empresta == 1) {
			val[val_pos] -= 10; 
		}
	}

//for(int i = 0; i < sub_len; i++) printf("%d",sub[i]);printf("\n");
	if(empresta == 1){
//	printf("empresta\n");
		for(int i = (val_len - sub_len- 1); i >= 0 ; i--){
			if(diff[i] == 0){
				diff[i] = 9;
				//empresta = 1;
			}else if(diff[i] >=  empresta) {
				diff[i] --;
				empresta = 0;
			}	
		}			

	}
	
//for(int i = 0; i < sub_len; i++) printf("%d",sub[i]);printf("\n");
	shift(val,'0',val_len);shift(sub,'0',sub_len);shift(diff,'0',val_len);// desfaz a conversão
	//printf("sub:%s.\n",sub);	
	if(empresta == 1){
		subtrair(sub,val,diff);
		return(-1);	
	}
	return(0);
}
// Faz uma divisão de inteiros de tamanho arbitrário
int divide(char *num, char *den, char *quo, char *resto){
//	printf("divide %s,%s\n",num,den);
	char temp_num[MAX_NUM_SIZE];
	char temp_diff[MAX_NUM_SIZE];
	int result = 0;
	int sub_counter = 0;
	if(den[0] == '0') return(-1); // divisao por zero
	//
	int num_len = strlen(num);
	int den_len = strlen(den);
	int num_pos = den_len;
	
	quo[0] = '\0';	
	if(den_len > num_len){
		strcpy(quo,"0");
		strcpy(resto,num);
		return(0);

//		printf("%s / %s = %s  sobra %s\n",num ,den,quo,resto);
	}
	/* vai pegando os pedaços do numerador de tamanhos igual ao denominador*/
	strncpy(temp_num,num,den_len);
	temp_num[den_len] = '\0';	
//	printf("size temp_num:%d size_den:%d\n", strlen(temp_num),den_len);
//	printf("1 while\n");
	strcpy(resto,num);	
	while(num_pos <= num_len ){
//		printf("	2 while\n");
		sub_counter = 0;
		while(result != -1){
			result = subtrair(temp_num,den,temp_diff);
		//	printf("		result:%d\n",result);
//			printf(".		temp_num:%s t_diff:%s sub_counter:%d result:%d\n", temp_num,temp_diff, sub_counter,result);
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
//	printf("%s / %s = %s  sobra %s\n",num ,den,quo,resto);
	return(0);
}

int main(int argc, char* argv[]){
	
	FILE *fp;
	char line[200] = {0};
	char num[100] = {0};// numerador
	char den[100] = {0};// denominador
	char quo[100];
	char resto[100];
	char val[] = "00130";
	/*for(int i = 0; i < 100000; i++){// validação das funções
		long int v1 = rand();
		long int v2 = rand();
		long int vq = v1/v2;
		long int vr = v1%v2;
		sprintf(num,"%ld",v1);
		sprintf(den,"%ld",v2);
		divide(num,den,quo,resto);
		if(vq != atol(quo)){
			printf("Erro q (%d) %ld/%ld = %ld,%ld <> %s/%s = %s,%s\n",i,v1,v2,vq,vr,num,den,quo,resto);
		
		}
		if(vr != atol(resto)) {
			printf("Erro r (%d) %ld/%ld = %ld,%ld <> %s/%s = %s,%s\n",i,v1,v2,vq,vr,num,den,quo,resto);
		}
	}*/
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
			clear_zero(quo);
			clear_zero(resto);
			if(quo[0] != '0')// se o primeiro algarismo for zero não imprima
				printf("%s ",quo);
			if(resto[0] != '0')
				printf("%s/%s",resto,den);
			printf("\n");
		}
	}	
	char v1[100] = "654";
	char v2[100] = "89777";
	char r[100];
	int signal = subtrair(v1,v2,r);
//	printf("\nsub:%d(%s)\n",signal,r);
	return(0);
}
