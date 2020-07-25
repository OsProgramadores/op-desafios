#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define INPUT_LIMIT	100		// max input lenght
#define WORDS_FILE	"words.txt"	// name of the file
#define NUM_WORDS	24853		// num of words in file 
#define MAX_LEN		23		// lenght of the largest word + '\0'



char unordened_word_array[NUM_WORDS][MAX_LEN]; // array with words ordened in crescent order, from the small to the bigger one
char word_array[NUM_WORDS][MAX_LEN]; // [num_of_words][len of largest word]
char word_len[NUM_WORDS]; // lenght of each word in word_array; 
int solution[INPUT_LIMIT] = {0}; // store the indexes os word_array for current solution

int last_len_ocurrency[23];	// armazena os indexes da ultima ocorrencia de 
				// uma palavra com determinado tamanho indicado pelo
				// index da variavel last_len_ocurrency

//push a new char into a buffer and return the new lenght
int push(char *buffer, char c){
	int pos = 0; //position in buffer
	while( buffer[pos]!='\0') pos++;
	buffer[pos] = c;
	buffer[pos + 1] = '\0';
	return(pos+1);
}	
// ordena as palavras da menor pra maior, assim espero, kkkk
// de quebra a função gera um array de 23 elementos que informa o index
// da ultima palavra de determinado tamanho 
int sort(char src[][MAX_LEN], char dest[][MAX_LEN]){
	int counter = 0;// contador para o buffer de destino.
	for(int len = 1; len <=  MAX_LEN;len++){ // para todos os tamanhos de palavra de 1 até 23
		for(int s_index = 0 ; s_index < NUM_WORDS; s_index++){ // para todas as palavras do dicionário
			if(strlen(src[s_index]) == len){
				last_len_ocurrency[len] = counter;
			       	strcpy(dest[counter++],src[s_index]);
			}
		}
	}
}
// returns the size of a string without counting spaces ' ' . 
int no_space_strlen(char *buffer){
	int counter = 0;
	int space_counter = 0;
	while(buffer[counter] != 0 ){
		counter++;
		if(buffer[counter] == ' ') space_counter++;
	}
	return(counter - space_counter);
}

// return 0 if a buffer is completely filled with spaces
int blank(char *buffer){	
	for(int i = 0; i < strlen(buffer);i++) 
		if(buffer[i] != ' ') return(-1);
	
	return(0);
}
void print_solution(int max_index){
	printf("");
	for(int i = 0; i <= max_index; i++)
		printf("%s ", word_array[solution[i]]);
	printf("\n");
}
// Test if a word of word_index was already used in solution array
// return 0 if not used and -1 if already used 
int used(int word_index, int solution_max_index){
	for(int i = 0; i <= solution_max_index; i++)
		if(word_index == solution[i]) return(-1);
	return(0);
}

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
/* A função de busca deve criar um buffer e testar cada palavra da words_list
 * se a palavra coincidir e não for maior que o work_buffer(input_buffer), a gente
 * exclui as letras encontradas e chama a mesma função passando como work_buffer 
 * as letras restantes.*
 */
int search(char *input, int solution_index, int first_index){
	char test_word[MAX_LEN];
	char test_input[INPUT_LIMIT];
	strcpy(test_input,input);
	
//	printf("(%s) ",test_input);

	//for(int i = first_index; i < last_len_ocurrency[no_space_strlen(test_input)]; i++){// testa todas as palavras
	for(int i = first_index; i < NUM_WORDS; i++){// testa todas as palavras
//		if(used(i,solution_index) == 0)//dicard used words		
			if(comb(test_input,word_array[i]) == 0) {
				
				//printf("%d %s ",index,word_array[i]);
				solution[solution_index] = i; // current word
				if(blank(test_input) == 0){ //the input is blank 
					print_solution(solution_index);
					//printf(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
				//	return(0); // sucess
				}
				search(test_input,solution_index+1,i+1);
				strcpy(test_input,input);
			}
		}
	solution[solution_index] = 0;
//	printf("<\n");	
	return(-1);
}

int main(int argc,char* argv[]){
	FILE *words_fp;
	char input[INPUT_LIMIT] = {0}; // stores the input from user, without spaces and all uppercase
	char temp[50];
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
	//	printf("%d\n",count);
	}
	fclose(words_fp);
	
	// ordena as palavras da menor pra maior
	sort(unordened_word_array,word_array);


	//aqui a brincadeira começa

//	printf("largest word: %d \n", largest(words_buffer));	
//	printf("%d ",pull_word(temp,words_buffer,24852));
//	pull_word(temp,words_buffer,3);
	//printf(">>%s", word_array[1]);
//	search(input);

	char test[] = "Mare  o";
	//int ret = comb(test,"aero");
	//printf("ret: %d, test[]:%s blank:%d",ret,test,blank("      "));
//	printf("no_space_strlen:%d strlen:%d",no_space_strlen(test),strlen(test));		
//	for(int i = 0 ; i < NUM_WORDS;i++) printf("%s\n",word_array[https://www.google.com/search?client=firefox-b-e&q=unordenedi]);
	return(search(input,0,0));
}
