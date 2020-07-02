#include <stdlib.h>
#include <stdio.h>
#include <stdio.h>
//#include <sys/ioctl.h>
#define LINE_BUFFER_SIZE 1000

int main(int argc , char* argv[]){
	FILE *fptr;
	long pos = LINE_BUFFER_SIZE-1 ;
	char linebuffer[LINE_BUFFER_SIZE-1] = {0};
	if(argc <= 1){
		printf("Usage: %s path_to_file\n",argv[0]);
		return(0);
	}
	fptr = fopen(argv[1],"r");
	if(fptr == NULL){
		printf("Error opening file");
		return(1);
	}
//	struct winsize w;
//	ioctl(0, TIOCGWINSZ, &w);

//	linebuffer[LINE_BUFFER_SIZE] = 0;
	fseek(fptr,-2,SEEK_END);	
	do{
		pos --;
		linebuffer[pos] = fgetc(fptr);
//		printf("%d\n",pos);
//		printf("%c",linebuffer[pos]);
		if(linebuffer[pos] == '\n'){
			printf("%s\n",linebuffer+pos+1);
			pos = LINE_BUFFER_SIZE-1;
		}
	}while(	fseek(fptr,-2,SEEK_CUR)==0);
	printf("%s\n",linebuffer+pos);
	fclose(fptr);
	return(0);
}
