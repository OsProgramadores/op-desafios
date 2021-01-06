#include <stdio.h>

// compilar: cc d02.c -o d02
// executar: ./d02

#define MAX 10000

int is_prime(int x) {
 int i = 0;

 for (i = 2; i <= x/ 2; i++) {
    if (x % i == 0) {
      return 0;
      break;
    }
 }
 return 1;
}

int main(void) {
  int i;

  for ( i = 2; i < MAX; i++ ) {
    if(is_prime(i) != 0) {
      printf("%d ", i);
    }
  }
  puts("");
  return 0;
}
