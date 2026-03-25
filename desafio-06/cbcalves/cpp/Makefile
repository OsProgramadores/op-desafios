#!make
# obs.: Eu uso clang, se for usar gcc tem que mudar os comentados abaixo.
#CC=g++
CC=clang++
CFLAGS=-I.
LFLAGS=-I. -lm
OBJ=obj/anagrama.o
DBG=-Ofast

obj/%.o: ./%.cpp
	@echo "    CC      $<"
	@$(CC) $(DBG) -c -o $@ $< $(CFLAGS)

./anagrama: obj $(OBJ)
	@echo "    LD      $@"
	@$(CC) $(DBG) -o $@ $(OBJ) $(LFLAGS)

obj:
	@mkdir obj

obj/anagrama.o: ./anagrama.cpp

.PHONY: clean

clean:
	@echo "Removendo arquivos"
	@rm -rf ./obj
	@rm -f ./anagrama

