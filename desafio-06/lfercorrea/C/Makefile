SRC := $(wildcard *.c)
BIN := $(basename $(SRC))

CC := clang
CFLAGS := -Wall -Wextra -O2

all: $(BIN)

$(BIN): $(SRC)
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f $(BIN)
