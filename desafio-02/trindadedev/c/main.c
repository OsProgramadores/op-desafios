#include <stdio.h>

static void desafio_prime_numbers_between(unsigned int min, unsigned int max) {
  for (int i = min; i < max; ++i) {
    if (i < 2)
      continue;  // va para o próximo, pois números menores que 2 não sao primos
    int is_prime = 1;
    for (int j = 2; j <= i / 2; ++j) {
      if (i % j == 0) {
        is_prime = 0;
        break;
      }
    }
    if (is_prime)
      printf("%d\n", i);
  }
}

int main() {
  desafio_prime_numbers_between(1, 10000);
  return 0;
}