#!make
CC=gcc
CFLAGS=-I. -flto -funroll-loops -pthread -lm
LFLAGS=-I. -flto -funroll-loops -pthread -lm
OBJ=obj/d5_v2.o
DBG=-Ofast

obj/%.o: ./%.c
	@echo "    CC      $<"
	@$(CC) $(DBG) -c -o $@ $< $(CFLAGS)

./d5_v2: obj $(OBJ)
	@echo "    LD      $@"
	@$(CC) $(DBG) -o $@ $(OBJ) $(LFLAGS)

obj:
	@mkdir obj

obj/d5_v2.o: ./d5_v2.c

.PHONY: clean

clean:
	@echo "Removendo arquivos"
	@rm -rf *.o ./obj
	@rm -f ./d5_v2

