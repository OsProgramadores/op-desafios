#!make
# Feito o Makefile, infelizmente não sei dizer se funcionará em windows, pois não uso
# para processar 1 Milhão de numeros e combinações de arrays tem que ter threads
# e aumento da velocidade de execução.
# obs.: Eu uso clang, se for usar gcc tem que mudar abaixo.
#CC=g++
CC=clang++
CFLAGS=-I.
LFLAGS=-I. -lm -pthread
OBJ=obj/primospi.o
DBG=-O2  	#retirei o -g de debug (finalizado) e coloquei -O2 para ter velocidade de execução na array geral

obj/%.o: ./%.cpp
	@echo "    CC      $<"
	@$(CC) $(DBG) -c -o $@ $< $(CFLAGS)

./primospi: obj $(OBJ)
	@echo "    LD      $@"
	@$(CC) $(DBG) -o $@ $(OBJ) $(LFLAGS)

obj:
	@mkdir obj

obj/primospi.o: ./primospi.cpp

.PHONY: clean

clean:
	@echo "Removendo arquivos"
	@rm -rf *.o ./obj
	@rm -f ./primospi

