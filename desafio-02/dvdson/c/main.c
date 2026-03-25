#include "math.h"
#include "stdio.h"


int is_prime(int number){
	int limit = sqrt(number);
	int count;
	for (count = 2; count <= limit; ++count){
		if(number%count == 0) return 0;
	}
	return 1;
}

int main (){
	int number;
		for (number = 2; number < 1000; ++number){
		if(is_prime(number)) printf("%d\n", number);
	}
}
