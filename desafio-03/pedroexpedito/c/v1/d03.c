#include <errno.h>
#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* check if it is a palindrome */

bool is_polydrome(const char *num) {
  int len = strlen(num) - 1;

  for (int i = 0; i < len; i++) {
    if (num[i] != num[len - i]) {
      return false;
    }
  }
  return true;
}

bool is_valid_string(const char *nptr) {
  if (strlen(nptr) > 21) {
    return false;
  }

  char *endptr = NULL;

  unsigned long long int number = strtoull(nptr, &endptr, 10);

  if (nptr == endptr) {
    fprintf(stderr," number : %llu  invalid  (no digits found, 0 returned)\n", number);
    return false;
  }
  else if (errno == ERANGE && number < 0) {
    fprintf(stderr," number : %llu  invalid  (underflow occurred)\n", number);
    return false;
  }
  else if (errno == ERANGE && number == ULLONG_MAX) {
    fprintf(stderr," number : %llu  invalid  (overflow occurred)\n", number);
    return false;
  }
  else if (errno == EINVAL) { /* not in all c99 implementations - gcc OK */
    fprintf(stderr," number : %llu  invalid  (base contains unsupported value)\n",
           number);
    return false;
  }
  else if (errno != 0 && number == 0) {
    fprintf(stderr," number : %llu  invalid  (unspecified error occurred)\n", number);
    return false;
  }
  else if (errno == 0 && nptr && !*endptr) {
    return true;
  }
  else if (errno == 0 && nptr && *endptr != 0) {
    return true;
  }
  return false;
}

int main(int argc, char **argv) {
  if (argc < 3) {
    fprintf(stderr, "exemple:./d03 1 20\n");
    exit(1);
  }
  if (is_valid_string(argv[1]) != true || is_valid_string(argv[2]) != true) {
    fprintf(stderr, "invalid args\n");
    exit(1);
  }

  unsigned long long int number1 = strtoull(argv[1], NULL, 10);
  unsigned long long int number2 = strtoull(argv[2], NULL, 10);

  if (number1 > number2) {
    fprintf(stderr, "first argument must be greater than the second\n");
    exit(1);
  }

  char buffer[22];

  for (unsigned long long int i = number1; i <= number2; i++) {
    snprintf(buffer, 22, "%llu", i);
    if (is_polydrome(buffer)) {
      printf("%llu ", i);
    }
  }
  puts("");

  return 0;
}
