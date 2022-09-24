#include <stdio.h>
#include <stdint.h>

#define BEGIN 1
#define END 10000

uint8_t is_palindrome(uint64_t);

int main(void)
{
	for (uint64_t i = BEGIN; i <= END; ++i) {
	 	if (is_palindrome(i) == 1) {
	 		printf("%lu is a palindrome\n", i);
	 	}
	}

	return 0;
}

uint8_t is_palindrome(uint64_t n) {
	if (n < 10)
		return 1;
	else if (n % 10 == 0)
		return 0;

	uint64_t number = n;
	uint64_t reversed = 0;

	while (number > 0) {
		reversed = reversed * 10 + number % 10;
		number /= 10;
	}

	return n == reversed;
}
