/*TODO 
 * 1 mesclar as funções comb e fast_comb
 * 2 trabalhar com qualquer tamanho de dicionario
 *
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define INPUT_LIMIT	100		// max input lenght
#define WORDS_FILE	"words.txt"	// name of the file
#define NUM_WORDS	24853		// num of words in file 
#define MAX_LEN		23		// lenght of the largest word + '\0'

long ana_count = 0; // contador global para contabilizar a quantidade de anagramas gerados
char *solution[INPUT_LIMIT] = {0}; // store the indexes os word_array for current solution

// push a new char into a buffer and return the new lenght
int push(char *buffer, char c){
	int pos = 0; //position in buffer
	while( buffer[pos]!='\0') pos++;
	buffer[pos] = c;
	buffer[pos + 1] = '\0';
	return(pos+1);
}	

// return 0 if a buffer is completely filled with spaces
int blank(char *buffer){	
	for(int i = 0; i < strlen(buffer);i++) 
		if(buffer[i] != ' ') return(-1);
	return(0);
}
void print_solution(int max_index){
	
	for(int i = 0; i < max_index; i++)
		printf("%s ", solution[i]);
	printf("%s\n", solution[max_index]);
}
// comb() verify combination
// Return 0 if sub is a subset of set
// in another words, all chars in string sub 
// are too in the string set
// a important note: set is partialy destroyed if successful
// a chars of set that are part of sub are substituted for spaces in set.
int comb(char *set, char *sub){
	char *index;
	char temp[INPUT_LIMIT];
	strcpy(temp,set);
	for(int j = 0 ; j < strlen(sub) ; j++){ // para cada letra da string sub
		if((index = strchr(set,sub[j])) != NULL){
			index[0] = ' ';
		}else{
			strcpy(set,temp);
			return(-1);
		}
	}
	return(0);
}
/* fast_comb, a more fast version of comb *
 *
 */
int fast_comb(char *set, char *sub){
	char *index;
	for(int j = 0 ; j < strlen(sub) ; j++){ // para cada letra da string sub
		if((index = strchr(set,sub[j])) == NULL){
			return(-1);
		}
	}
	return(comb(set,sub));
}

/* Make a new dictionary of valid words 
 * and return the num of words in the new dictionary
 */
int make_new_dict(char *input,char *dest_dict[23],char *src_dict[MAX_LEN], int src_size){
	char temp[INPUT_LIMIT];
	int counter = 0; //conta as ocorrencias de match
	strcpy(temp,input);
	for(int i = 0; i < src_size; i ++){
		if(fast_comb(temp,src_dict[i])==0){
			dest_dict[counter++] = src_dict[i];
			strcpy(temp,input);
		}
	}
	return(counter);
}


/* merge a sentence, removing space and shifting the parts together
 */

int merge(char *buffer){
	int spaces = 0;
	for(int i = 0 ; i < strlen(buffer); i++){
		if(buffer[i+spaces] == ' ') spaces++;
		buffer[i] = buffer[i+spaces];
	}
	return(0);
}


/*
 *
 */
int search(char *prev_dict[MAX_LEN], int prev_dict_size, char *input, int solution_index){
	
	// solution_index : indice da solução a ser preechido caso um anagrama seja encontrado
	// dict_indexes : array with indexes of dictionary with all words used in precious search
	char test_word[MAX_LEN];
	char temp_input[INPUT_LIMIT];
	int dict_size;// size of current dictionary
	// dict é um ponteiro para os ponteiros do novo dicionário a ser criado 
	// essa ideia parece ter sido a melhor estratégia para otimizar o algoritmo
	// pois a cada nova chamada do search() a função cria um novo dicionário sem
	// comprometer muita memória pois não armazena as palavras novamente, apenas os
	// ponteiros para as palavras pre-armazenadas
	char  **dict = NULL;
	dict = (char **)malloc(prev_dict_size * sizeof(char*));
	if(dict == NULL){
		// e agora josé??
		//
		// se não houver memória, aproveite o dicionário anterior
		dict = prev_dict;
		dict_size = prev_dict_size;
	}else dict_size = make_new_dict(input, dict,prev_dict,prev_dict_size);
	
	strcpy(temp_input,input);
	for(int i = 0; i < dict_size; i++){// testa todas as palavras
			if(fast_comb(temp_input,dict[i]) == 0) {
				solution[solution_index] = dict[i]; // current word
				if(blank(temp_input) == 0){ //the input is blank 
					print_solution(solution_index);
					ana_count++;
				//	free(dict);	
				//	return(0);
				}
				merge(temp_input); // elimina os espacos pra ganhar tempo nas operações seguintes
				search((dict+i+1),dict_size-(i+1),temp_input,solution_index+1);
				strcpy(temp_input,input);
			}
		}
	free(dict);	
	solution[solution_index] = 0;
	return(0);
}

int main(int argc,char* argv[]){
	FILE *words_fp;
	int num_words = 0; // quantidade de palavras lidas do arquivo
	char word_array[NUM_WORDS][MAX_LEN]; // [num_of_words][len of largest word]
	char input[INPUT_LIMIT] = {0}; // stores the input from user, without spaces and all uppercase
	//trata os erros de entrada
	if(argc != 2){
	       	fprintf(stderr,"usage: %s \"sentenca de entrada\"\n",argv[0]);
		return(-1);
	}
	if(strlen(argv[1])>INPUT_LIMIT){
		fprintf(stderr,"Erro: entrada maxima %d\n",INPUT_LIMIT);
		return(-1);
	}
	
	//trata a entrada
	for(int i = 0 ; i < strlen(argv[1]);i++){
		if((argv[1][i]>='A')&&(argv[1][i]<='Z')) push(input,argv[1][i]);
		else if((argv[1][i]>='a')&&(argv[1][i]<='z')) push(input,argv[1][i] + 'A' - 'a');
		else if(argv[1][i] == ' ');
		else{
			fprintf(stderr,"Caracteres permitidos: A-Z a-z\n");
			return(-1);
		}
	}	
	//abre o arquivo , carrega o array e fecha
	words_fp = fopen(WORDS_FILE,"rb+");
	if(words_fp == NULL){
		perror("Erro ao abrir o arquivo " WORDS_FILE );
		return(-1);
	}
	int count = 0;
	while(!feof(words_fp)){
		fscanf(words_fp,"%s",word_array[count++]); 
		if(ferror(words_fp)){
			perror("Erro lendo o arquivo " WORDS_FILE);
			return(-1);
		}
		num_words++;
	//	printf("%d\n",count);
	}
	fclose(words_fp);
	num_words--; // é necessário diminuir 1 porque a função acima também conta o EOF.

	//aqui a brincadeira começa
	
	char **dict = NULL;
	dict = (char **)malloc(num_words * sizeof(char*));
	if(dict == NULL){
		fprintf(stderr,"Cara, seu pc não conseguiu alocar %ld Bytes, resolver anagramas é o menor dos seus problemas!", num_words * sizeof(char*));
		return(-1);
	}
	for(int i = 0 ;i < num_words;i++) dict[i] = word_array[i];
	// aqui eu converti o array de words para poiter of poiters para
	// padronizar a chamada da função search. 
	// não consegui trabalhar do jeito que eu queria usando arrays
	search(dict,num_words,input,0);
	return(0);
}
