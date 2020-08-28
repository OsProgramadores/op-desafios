#!make
# obs.: Eu uso clang, se for usar gcc tem que mudar abaixo.
#CC=gcc
CC=clang
CFLAGS=-I. -flto -funroll-loops
LFLAGS=-I. -flto -funroll-loops
OBJ=obj/d5.o
DBG=-Ofast

obj/%.o: ./%.c
	@echo "    CC      $<"
	@$(CC) $(DBG) -c -o $@ $< $(CFLAGS)

./d5: obj $(OBJ)
	@echo "    LD      $@"
	@$(CC) $(DBG) -o $@ $(OBJ) $(LFLAGS)

obj:
	@mkdir obj

obj/d5.o: ./d5.c

.PHONY: clean

clean:
	@echo "Removendo arquivos"
	@rm -rf *.o ./obj
	@rm -f ./d5

