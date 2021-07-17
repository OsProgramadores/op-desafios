#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <gmp.h>

/* DEPENDENCIAS
 *
 * libgmp-dev
 *
 * Normalmente tem em quase todas as distros linux
 *
 * Debian-like: apt install libgmp-dev
 *
 * no fedora acho que é gmp-devel
 *
 * COMPILACAO
 *
 * gcc d12.c -lgmp -o d12
 *
 */

// retorna -1 caso não for potencia de 2
// ou N > -1  a potencia ex:
// n = 1; return 0
// n = 128; return 7;
// n = 140; return -1;

long long isPotentenciaDeDois(mpz_t num) {
  if(mpz_cmp_ui(num, 1) == 0) {
    return 0;
  }
  mpz_t div;
  mpz_init(div);
  mpz_set_ui(div, 2);

  unsigned long vezes = 0;
  unsigned long ret;

  ret = mpz_fdiv_ui(num, 2);

  while(ret == 0 && mpz_cmp_ui(num, 0) > 0) {
    mpz_cdiv_q(num, num, div);
    vezes++;

    if(mpz_cmp_ui(num, 1 ) == 0) {
      mpz_clear(div);
      return vezes;
    }

    ret = mpz_fdiv_ui(num, 2);
  }

  mpz_clear(div);
  return -1;
}

void usage() {
  fprintf(stderr, "./d12 <file>\n");
  exit(EXIT_FAILURE);
}

int main(int argc, char *argv[]) {
  mpz_t num;
  mpz_init(num);

  if(argc < 2) {
    usage();
  }

  FILE *fp = fopen(argv[1], "r");

  if(fp == NULL) {
    perror("error opening file");
    exit(EXIT_FAILURE);
  }

  char *p = NULL;
  size_t size = 0;
  unsigned long nread;

  while((nread = getline(&p, &size, fp)) != -1LU) {
    mpz_set_str(num, p, 10);
    long long ret = isPotentenciaDeDois(num);

    if (p[nread - 1] == '\n') {
      p[nread - 1] = 0;
    }

    if(ret == -1) {
      printf("%s false\n", p);
    } else {
      printf("%s true %lli\n", p, ret);
    }
  }

  fclose(fp);
  free(p);
  mpz_clear(num);
}
