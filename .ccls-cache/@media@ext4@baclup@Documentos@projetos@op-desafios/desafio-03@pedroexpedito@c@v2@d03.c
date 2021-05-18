#include <ctype.h>
#include <gmp.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* com as dicas do Frederico Pissarra  */

/* LIB: GMP em algumas  distros não vem instalado para dev para instalar
 * em debian-based é apt install libgmp-dev */
/* USO: passar o intervalo por argumento  */

/* check if it is a palindrome */

bool isPalindrome(char *p) {
  size_t size;
  char *q;

  size = strlen(p);

  if (!size)
    return false;

  q = p + size - 1;

  while (p < q)
    if (*p++ != *q--)
      return false;

  return true;
}

/* check is Numeric  */

int isStringNumeric(char *p) {
  while (*p) {
    if (!isdigit(*p))
      return 0;

    p++;
  }

  return 1;
}

int main(int argc, char **argv) {
  if (argc < 3) {
    fprintf(stderr, "exemple:./d03 1 20\n");
    exit(EXIT_FAILURE);
  }

  if (!(isStringNumeric(argv[1]) && isStringNumeric(argv[2]))) {
    fprintf(stderr, "arg is not number\n");
    exit(EXIT_FAILURE);
  }

  // string para mpz_t inteiros


  mpz_t number1;
  mpz_init(number1);
  mpz_set_str(number1, argv[1], 10);
  mpz_t number2;
  mpz_init(number2);
  mpz_set_str(number2, argv[2], 10);

  // check if number1 < number2


  int ret = mpz_cmp(number1, number2);

  if( ret > 0) {
    fprintf(stderr, "first argument must be less than the second\n");
    exit(EXIT_FAILURE);
  }


  char *num;

  while(mpz_cmp(number1, number2) != 0) {
    num = mpz_get_str(NULL,10,number1);
    if(isPalindrome(num)) {
      printf("%s ", num);
    }
    mpz_add_ui(number1,number1, 1);
  }

  puts("");

  return EXIT_SUCCESS;
}
