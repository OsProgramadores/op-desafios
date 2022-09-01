#include <stdio.h>

#define LIMIT 10000

unsigned is_prime(unsigned n);

int main(void)
{
	printf("%d\n", 2); /* 2 is prime */
	printf("%d\n", 3); /* 3 is prime */
	for (unsigned n = 5; n <= LIMIT; n += 2) {
		if (is_prime(n)) {
			printf("%d\n", n);
		}
	}

	return 0;
}

unsigned is_prime(unsigned n)
{
	if (n % 3 == 0)
		return 0;

	for (unsigned i = 5; i * i <= n; i += 6) {
		if (n % i == 0 || n % (i + 2) == 0) {
			return 0;
		}
	}

	return 1;
}
