#include <stdio.h>


int main(void)
{
  int i, j;
  int max = 10000;
  int primes[max + 1];
  
  // adding natural numbers to array
  for (i = 2; i<=max; i++){
    primes[i] = i;
  }
    

  i = 2;
  while ((i * i) <= max) {
    if (primes[i] != 0) {
      for (j = 2; j < max; j++) {
	if (primes[i] * j > max) {
	  break;
	} else {
	  primes[primes[i] * j] = 0; // creating 0's, not deleteing it
	}
      }
    }
    i++;
  }
  for (i = 2; i <= max; i++) {
    if (primes[i] != 0)
      printf("%d\n", primes[i]);
  }

  return 0;
}
