/*
Solução Desafio 07
Author: Guilherme Silva Schultz
Data: 21-01-2023

Solução Desafio 07 usando *syscalls
(o uso de syscalls não é nescessario
apenas um desafio pessoal pois estudo C para aplicaçoes de baixo nivel)
*syscalls unix
*/


#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>


//tamanho maximpo do buffer
//quanto maior, melhor a eficiencia para se trabalhar com syscalls
#define BUFFER_SIZE 5000


//enum para verificação de erros
typedef enum {
  OK,
  ERROR,
} erro_status;

//struct com dados do arquivo
typedef struct {
  int file;
  size_t size;
  size_t end_file;
  erro_status error;
} file_status;


file_status open_and_process(const char *file_name) {
    //inicia um strcut padrao
    file_status file;
    file.file = -1;
    file.size = 0;
    file.error = ERROR;
    file.end_file = 0;

    //abre o arquivo com a open syscall
    int file_dp = open(file_name, O_RDONLY);
    // retorna em caso de erro
    if (file_dp == -1) {
        return file;
    }

    //usa stat syscall para receber o tamanho do arquivo
    struct stat file_stat;
    fstat(file_dp, &file_stat);
    size_t size = file_stat.st_size;

    file.error = OK;
    file.file = file_dp;
    file.size = size;
    file.end_file = size - 1;

    return file;
}

//fecha o arquivo com close syscall
void close_file(file_status file) { close(file.file); }

// escreve o buffer na tela
// recebe o arquivo e a posição de inicio e fim do print
// caso o do conteudo seja maior que o buffer BUFFER_SIZE < (end - begin)
// divide o conteudo em tamanhos de BUFFER_SIZE
void print_buffer(int file, int begin, int end){
    char buffer[BUFFER_SIZE];
    int print_size = (end-begin);
    int off_set_begin = begin;
    while(print_size > BUFFER_SIZE){
        //pread syscall ja recebe a posição de leitura
        //então não ha necessidade da seek syscall
        pread(file, buffer, BUFFER_SIZE, off_set_begin);
        write(STDOUT_FILENO, buffer, BUFFER_SIZE);
        print_size -= BUFFER_SIZE;
        off_set_begin += BUFFER_SIZE;
    }
    pread(file, buffer, print_size, off_set_begin);
    write(STDOUT_FILENO, buffer, print_size);

}

//começa a leitura pelo final do arquivo, até encontrar \n ou o inicio do arquivo
//chama print_buffer passando a posição atual do \n encontrado e o fim
//apos cada chamado fim é igualado a posição do ultimo \n
void reverse_print(file_status file) {
    char buf[1];
    int end = (int) file.end_file;
    int i = end;
    for(;i >= -1; i--){
        pread(file.file, buf, 1, i);
        if(*buf == '\n'){
            print_buffer(file.file, i+1, end+1);
            end = i;
        }else if(i == 0){
            print_buffer(file.file, i, end+1);
            break;
        }
    }
}

  int main(int argc, char *argv[]){
    if(argc < 2){
        puts("chame esse programa passando o path do arquivo de texto");
        puts("Ex ./main arquivo.txt");
        return ERROR;
    }

    file_status file = open_and_process(argv[1]);
    switch (file.error) {
    case OK:
      reverse_print(file);
      close_file(file);
      break;
    case ERROR:
        perror("o programa encontrou o seguinte error");
        return ERROR;
        break;
    }
    return 0;
  }
