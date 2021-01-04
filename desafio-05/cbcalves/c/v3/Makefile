#!make
CC=gcc
CFLAGS=-I. -flto -funroll-loops -pthread -lm -ftree-vectorize
LFLAGS=-I. -flto -funroll-loops -pthread -lm -ftree-vectorize
OBJ=obj/d5_v3.o
DBG=-Ofast

obj/%.o: ./%.c
	@echo "    CC      $<"
	@$(CC) $(DBG) -c -o $@ $< $(CFLAGS)

./d5_v3: obj $(OBJ)
	@echo "    LD      $@"
	@$(CC) $(DBG) -o $@ $(OBJ) $(LFLAGS)

obj:
	@mkdir obj

obj/d5_v3.o: ./d5_v3.c ./uthash_mod.h

.PHONY: clean

clean:
	@echo "Removendo arquivos"
	@rm -rf *.o ./obj
	@rm -f ./d5_v3

