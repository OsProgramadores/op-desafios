SRC := $(wildcard *.c)
BIN := $(basename $(SRC))

CC := clang

# agora eu vou aprender de verdade.. kkk
CFLAGS := -Wall -Wextra -Wpedantic -Werror \
	-Wshadow -Wconversion -Wsign-conversion \
	-Wuninitialized -Winit-self -Wfloat-equal \
	-Wstrict-prototypes -Wold-style-definition \
	-Wmissing-prototypes -Wmissing-declarations \
	-Wredundant-decls -Wnull-dereference \
	-Wdouble-promotion -Wformat=2 -Wformat-security \
	-Wcast-align -Wcast-qual -Wbad-function-cast \
	-Wvla -Wstack-protector -Wwrite-strings \
	-Wno-unused-parameter \
	-O2


all: $(BIN)

$(BIN): $(SRC)
	$(CC) $(CFLAGS) $< -o $@ -lm

clean:
	rm -f $(BIN)
