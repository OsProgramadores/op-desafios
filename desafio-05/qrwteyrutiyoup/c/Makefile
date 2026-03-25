all:
	gcc d5.c -o d5-c -m64 -Ofast -flto -march=native -funroll-loops
debug:
	gcc d5.c -o d5-c-debug -O0 -g
clean:
	rm -f d5-c d5-c-debug
