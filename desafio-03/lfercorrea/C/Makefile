SRC := $(wildcard *.c)
BIN := $(basename $(SRC))

CC := clang

# agora eu vou aprender de verdade.. kkk
CFLAGS := -Wall -Wextra -Wpedantic -Wconversion \
	-Wshadow -Wstrict-prototypes -Wundef -Wcast-align \
	-Wunreachable-code -Wswitch-enum \
	-O2


all: $(BIN)

$(BIN): $(SRC)
	$(CC) $(CFLAGS) $< -o $@ -lm

clean:
	rm -f $(BIN)
