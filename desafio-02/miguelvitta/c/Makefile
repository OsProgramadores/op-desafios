CC = gcc
CFLAGS = -Wall -Wextra -Wshadow

primos: primos.c
	$(CC) $(CFLAGS) primos.c -o primos -lm

.PHONY: clean
clean:
	rm -f primos *.o
