#include <stdlib.h>
#include <stdio.h>
#include <stdio.h>
#define LINE_BUFFER_SIZE	1000
#define BUFFER_SIZE		10000 
#define ERROR			-1


/* TODO LIST	
 * (DONE!)		-need to deal with lines bigger then LINE_BUFFER_SIZE(yes, im noob)
 * (IMPOSSIBLE)		-print the line using the data stored in buffer, not loading linebuffer 
 * (UNNECESSARY)	-use malloc instead of arrays 
 */



// print line delimited by file indexes : start , end
// Precisa preservar o SEEK_CUR no arquivo 
int print_line(FILE *fptr,long start, long end){
	long cur_pos = ftell(fptr);
	// o +1 facilita as contas já que posso encher 
	// o buffer com LINE_BUFFER_SIZE bytes e o último
	// elemento será deixado em '\0' facilitando o printf
	char linebuffer[LINE_BUFFER_SIZE+1];

	fseek(fptr,start,SEEK_SET);
	if(ferror(fptr)) return(ERROR);
	
	while(end-start > LINE_BUFFER_SIZE){
		start += fread(&linebuffer, 1, LINE_BUFFER_SIZE, fptr);
		linebuffer[LINE_BUFFER_SIZE] = '\0';
		if(ferror(fptr)) return(ERROR);
		printf("%s",linebuffer);
		fseek(fptr,start,SEEK_SET);
		if(ferror(fptr)) return(ERROR);
	}
//	if((end - start) <= LINE_BUFFER_SIZE){
		fread(&linebuffer, 1,end - start, fptr);
		if(ferror(fptr)) return(ERROR);
		linebuffer[end - start] = '\0';
		printf("%s\n",linebuffer);
//	}

	// precisa retornar pra onde o ponteiro do arquivo estava antes
	fseek(fptr,cur_pos,SEEK_SET);
	if(ferror(fptr)) return(ERROR);
	return(0);
}

int main(int argc , char* argv[]){
	FILE *fptr;
	char buffer[BUFFER_SIZE];
	long pos = LINE_BUFFER_SIZE-1 ;
	long read_ret;
	long seek_ret;
	int last_bytes = BUFFER_SIZE; // last bytes to read when fseek reaches SEEK_SET
	long fsize = 0;
	long last_cr = 0;
	if(argc <= 1){
		fprintf(stderr,"Usage: %s path_to_file\n",argv[0]);
		return(0);
	}
	fptr = fopen(argv[1],"rb+");
	if(fptr == NULL){
		perror("Error opening file");
		return(ERROR);
	}
	// dispensa o último char do arquivo porque costuma ser convertido em \n
	fseek(fptr,-1,SEEK_END);	
	if(ferror(fptr)){
		perror("Seek error");
		return(ERROR);
	}
	fsize = ftell(fptr);
		
	long count = 1;
	long end = fsize; // end of line intended to print
	long cr_pos = -1; // position os CR found, start of line intended to print
	long bytes_to_read = BUFFER_SIZE;	
	// this while must start with fseek to end 
	while(seek_ret == 0){ // pega buffers de todo o arquivo

		seek_ret = fseek(fptr,-BUFFER_SIZE,SEEK_CUR);
		if(ferror(fptr)){
			perror("Seek error");
			return(ERROR);
		}
		if(seek_ret != 0){
			if(count == 1) bytes_to_read = fsize;	// se for a primeira leitura
			else bytes_to_read = cr_pos;		
		       	fseek(fptr,0,SEEK_SET);
			if(ferror(fptr)){
				perror("Seek error");
				return(ERROR);
			}
		}
		cr_pos = ftell(fptr);
//		printf("bytes_to_read: %d ,  cr_pos: %d \n",bytes_to_read, cr_pos);
		read_ret = fread(&buffer, 1,bytes_to_read, fptr);
		if(ferror(fptr)){
			perror("Read error");
			return(ERROR);
		}
		for(long i = 1; i <= read_ret ; i++){
			if(buffer[read_ret - i] == '\n'){
				cr_pos = ftell(fptr) - i  ;
				if(print_line(fptr,cr_pos+1,end) == ERROR){
					perror("Erro ao imprimir linha do arquivo");
					return(ERROR);
				}
				end = cr_pos;
			}
		}
		fseek(fptr,cr_pos,SEEK_SET);
		if(ferror(fptr)){
			perror("Seek error");
			return(ERROR);
		}
		count++;
	}
	if(print_line(fptr,0,end) == ERROR){
		perror("Erro ao imprimir linha do arquivo");
		return(ERROR);
	}
	fclose(fptr);
	return(0);
}
