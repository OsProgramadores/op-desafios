#include <stdlib.h>
#include <stdio.h>
#include <stdio.h>
#define LINE_BUFFER_SIZE 100000 
#define BUFFER_SIZE 1000000

/* TODO LIST	
 * -need to deal with lines bigger then LINE_BUFFER_SIZE(yes, im noob)
 * -print the line using the data stored in buffer, not loading linebuffer
 * -use malloc instead of arrays 
 * 
 *
 */



//print line delimited by file indexes : start , end
//Precisa preservar o SEEK_CUR no arquivo 
int print_line(FILE *fptr,long start, long end){
	long cur_pos = ftell(fptr);
	char linebuffer[LINE_BUFFER_SIZE];

	fseek(fptr,start,SEEK_SET);
	if(ferror(fptr)){
	     perror("Seek error");
	     return(-1);
	}
	if((end - start) <= LINE_BUFFER_SIZE){

		fread(&linebuffer, sizeof(char),end - start, fptr);
		if(ferror(fptr)){
			perror("Read error");
			return(-1);
		}
		linebuffer[end - start] = '\0';
		printf("%s\n",linebuffer);
	}

	// precisa retornar pra onde o ponteiro do arquivo estava antes
	fseek(fptr,cur_pos,SEEK_SET);
	if(ferror(fptr)){
	     perror("Seek error");
	     return(-1);
	}
	return(0);
}

int main(int argc , char* argv[]){
	
	
	FILE *fptr;
	char buffer[BUFFER_SIZE];
	
	
	long pos = LINE_BUFFER_SIZE-1 ;
	long read_ret;
	long seek_ret;
	int last_bytes = BUFFER_SIZE; //last bytes to read when fseek reaches SEEK_SET
	long fsize = 0;
	long last_cr = 0;
	if(argc <= 1){
		fprintf(stderr,"Usage: %s path_to_file\n",argv[0]);
		return(0);
	}
	fptr = fopen(argv[1],"rb+");
	if(fptr == NULL){
		perror("Error opening file");
		return(-1);
	}
	//dispensa o último char do arquivo porque costuma ser convertido em \n
	fseek(fptr,-1,SEEK_END);	
	if(ferror(fptr)){
	     perror("Seek error");
	     return(-1);
	}
	fsize = ftell(fptr);
		
	long count = 1;
	long end = fsize; //end of line intended to print
	long cr_pos = -1;  // position os CR found, start of line intended to print
	long bytes_to_read = BUFFER_SIZE;	
	// this while must start with fseek to end 
	while(seek_ret == 0){ // pega buffers de todo o arquivo
		seek_ret = fseek(fptr,-BUFFER_SIZE,SEEK_CUR);
		if(ferror(fptr)){
			perror("Seek error");
			return(-1);
		}
		if(seek_ret != 0){
			bytes_to_read = end;
		       	fseek(fptr,0,SEEK_SET);
			if(ferror(fptr)){
				perror("Seek error");
				return(-1);
			}
		}
		cr_pos = ftell(fptr);
//		clear_buffer();
		read_ret = fread(&buffer, sizeof(char),bytes_to_read, fptr);
		if(ferror(fptr)){
			perror("Read error");
			return(-1);
		}
		for(long i = 1; i <= read_ret ; i++){
			if(buffer[read_ret - i] == '\n'){
				cr_pos = ftell(fptr) - i  ;
				print_line(fptr,cr_pos+1,end);

				end = cr_pos;
			}

		}
		fseek(fptr,cr_pos,SEEK_SET);
		if(ferror(fptr)){
			perror("Seek error");
			return(-1);
		}
		count++;
		
	}
	print_line(fptr,0,end);
	fclose(fptr);
	return(0);
}
