#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define INPUT_LIMIT	100		// max input lenght
#define WORDS_FILE	"words.txt"	// name of the file
#define NUM_WORDS	24853		// num of words in file 
#define MAX_LEN		23		// lenght of the largest word + '\0'

long ana_count = 0;

char unordened_word_array[NUM_WORDS][MAX_LEN]; // array with words ordened in crescent order, from the small to the bigger one
char word_array[NUM_WORDS][MAX_LEN]; // [num_of_words][len of largest word]
char valid_words_array[NUM_WORDS][MAX_LEN]; // armazena todas as palavras cujos caracteres estejam contidos no input, acho que essa vai ser a sacada!!!!!!
char word_len[NUM_WORDS]; // lenght of each word in word_array; 
int valid_words;
char *solution[INPUT_LIMIT] = {0}; // store the indexes os word_array for current solution

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
	
	for(int i = 0; i < max_index; i++)
		printf("%s ", solution[i]);
	
	printf("%s\n", solution[max_index]);
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
/* fast_comb a more fast version of comb *
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


/* Seleciona apenas as palavras cujos caracteres estejam presentes na sentença
 * assim podemos restringir muito a nossa pesquisa
 */
int select_valid(char *input,char dest_bufferi[][MAX_LEN],char src_buffer[][MAX_LEN], int src_size){
	char temp[INPUT_LIMIT];
	int counter = 0; //conta as ocorrencias de match
	strcpy(temp,input);
	for(int i = 0; i < src_size; i ++){
		if(comb(temp,word_array[i])==0){
			strcpy(valid_words_array[counter++],word_array[i]);
			strcpy(temp,input);
		}
	}
	return(counter);
}

/* Make a new dictionary of valid words 
 *
 *
 */
int make_new_dict(char *input,char *dest_dict[23],char *src_dict[MAX_LEN], int src_size){
	char temp[INPUT_LIMIT];
	int counter = 0; //conta as ocorrencias de match
	strcpy(temp,input);
	for(int i = 0; i < src_size; i ++){
		if(fast_comb(temp,src_dict[i])==0){
			//strcpy(valid_words_array[counter++],word_array[i]);
			dest_dict[counter++] = src_dict[i];
		//	printf("%s   %ld  >> %ld \n",src_dict[i], src_dict[i],dest_dict[counter-1]);
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
}



/* A função de busca deve criar um buffer e testar cada palavra da words_list
 * se a palavra coincidir e não for maior que o work_buffer(input_buffer), a gente
 * exclui as letras encontradas e chama a mesma função passando como work_buffer 
 * as letras restantes.*
 */
int search(char *prev_dict[MAX_LEN], int prev_dict_size, char *input, int solution_index, int first_index){
	
	// solution_index : indice da solução a ser preechido caso um anagrama seja encontrado
	// first_index : primeiro índice do word_buffer a ser procurado.
	// dict_indexes : array with indexes of dictionary with all words used in precious search
	//for(int i = 0 ; i < prev_dict_size;i++) printf("%s\n",prev_dict[i]);
	char test_word[MAX_LEN];
	char test_input[INPUT_LIMIT];
	int dict_size;// size of current dictionary
	char  **dict = NULL;
	
	dict = (char **)malloc(prev_dict_size * sizeof(char*));
	strcpy(test_input,input);
	dict_size = make_new_dict(test_input, dict,prev_dict,prev_dict_size);
//	printf("dict for %s: ",input);
//	for(int i = 0 ; i < dict_size;i++) printf("%s ",dict[i]);
//	printf("\n");
//	return(0); // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
//	char current_buffer[][MAX_LEN];	
//	current_buffer = malloc(word_buffer_size*MAX_LEN);
		
//	printf("(%s) ",test_input);

	//for(int i = first_index; i < last_len_ocurrency[no_space_strlen(test_input)]; i++){// testa todas as palavras
	for(int i = 0; i < dict_size; i++){// testa todas as palavras
			if(fast_comb(test_input,dict[i]) == 0) {
				
				//printf("%d %s ",index,word_array[i]);
				solution[solution_index] = dict[i]; // current word
				if(blank(test_input) == 0){ //the input is blank 
					print_solution(solution_index);
					ana_count++;
					//	printf(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n");
				//	return(0); // sucess
				}
				merge(test_input);
				search((dict+i+1),dict_size-(i+1),test_input,solution_index+1,i+1);
				strcpy(test_input,input);
			}
		}
//	printf("<<\n");
	free(dict);	
	solution[solution_index] = 0;
//	printf("<\n");	
	return(0);
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
	valid_words = select_valid(input,valid_words_array,word_array,NUM_WORDS);

	//aqui a brincadeira começa

//	printf("largest word: %d \n", largest(words_buffer));	
//	printf("%d ",pull_word(temp,words_buffer,24852));
//	pull_word(temp,words_buffer,3);
	//printf(">>%s", word_array[1]);
//	search(input);

	char test[] = "a e i";
	merge(test);
//	printf("%s", test);
	//int ret = comb(test,"aero");
	//printf("ret: %d, test[]:%s blank:%d",ret,test,blank("      "));
//	printf("no_space_strlen:%d strlen:%d",no_space_strlen(test),strlen(test));		
//	for(int i = 0 ; i < valid_words;i++) printf("%d %s\n",i, valid_words_array[i]);
//	printf("ptr:%d  int:%d  long:%d\n",sizeof(int*),sizeof(int),sizeof(long));   
	
	char **dict = NULL;
	int dict_size = NUM_WORDS;	
	dict = (char **)malloc(NUM_WORDS * sizeof(char*));
	for(int i = 0 ;i < dict_size;i++) dict[i] = word_array[i];
	//	dict_size = make_new_dict(input, dict,word_array,NUM_WORDS);

//	for(int i = 0 ; i < dict_size;i++) printf(">>%s\n",dict[i]);
	search(dict,dict_size,input,0,0);
//	fprintf(stderr,"solucoes:%d",ana_count);
	return(0);
}
