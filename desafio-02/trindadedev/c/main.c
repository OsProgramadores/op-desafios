#include <stdio.h>

#define bool  char
#define false 0
#define true  1

static void desafio_prime_numbers_between(unsigned int max) {
  for (int num = 2; num < max; ++num) {
    bool is_prime = true;
    for (int divider = 2; divider <= num / 2; ++divider) {
      if (num % divider == 0) {
        is_prime = false;
        break;
      }
    }
    if (is_prime)
      printf("%d\n", num);
  }
}

int main() {
  desafio_prime_numbers_between(10000);
  return 0;
}