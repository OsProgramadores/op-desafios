TARGET_BIN := primes

SRC := primes.c
OBJ := prime.o
FLAGS := -Wall -Wextra -Wpedantic

$(TARGET_BIN): $(OBJ)
	$(CC) $< -o $@

$(OBJ): $(SRC)
	$(CC) -c $< -o $@


.PHONY: all clean
all:
	$(TARGET_BIN)

clean:
	rm $(OBJ)
	rm $(TARGET_BIN)
