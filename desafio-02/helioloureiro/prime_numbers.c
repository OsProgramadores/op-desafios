#include <stdio.h>
#include <time.h>

#define false 1
#define true 0

int is_prime(int number){
  /*
  src: https://en.wikipedia.org/wiki/Primality_test
   function is_prime(n)
     if n ≤ 3
        return n > 1
     else if n mod 2 = 0 or n mod 3 = 0
        return false
     let i ← 5
     while i * i ≤ n
        if n mod i = 0 or n mod (i + 2) = 0
            return false
        i ← i + 6
     return true
  */
  if (number <= 3) {
    return true;
  }
  if ((number%2) == 0) {
    return false;
  }
  if ((number%3) == 0) {
    return false;
  }
  int i = 5;
  while (i*i <= number) {
    if ((number%i) == 0) {
      return false;
    }
    if ((number%(i+2)) == 0) {
      return false;
    }
    i += 6;
  }
  return true;
}

int main() {
  time_t time_start = time(NULL);
  int prime_counter = 0;
  printf("Prime numbers\n");
  for (int n=1; n<= 10000; n++) {
    if (is_prime(n) == true) {
      printf("%d\n", n);
      prime_counter++;
    }
  }
  time_t time_stop = time(NULL);
  printf("Prime numbers found: %d\n", prime_counter);
  printf("Total time: %d\n", (time_stop - time_start));

  return 0;
}

