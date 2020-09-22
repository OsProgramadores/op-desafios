#!make
CC=gcc
CFLAGS=-I.
LFLAGS=-I. -lm
OBJ=obj/anagrama.o
DBG=-Ofast

obj/%.o: ./%.c
	@echo "    CC      $<"
	@$(CC) $(DBG) -c -o $@ $< $(CFLAGS)

./anagrama: obj $(OBJ)
	@echo "    LD      $@"
	@$(CC) $(DBG) -o $@ $(OBJ) $(LFLAGS)

obj:
	@mkdir obj

obj/anagrama.o: ./anagrama.c

.PHONY: clean

clean:
	@echo "Removendo arquivos"
	@rm -rf ./obj
	@rm -f ./anagrama

