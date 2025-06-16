#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

#define bool char
#define false 0
#define true 1

#define RESET "\033[0m"
#define RED "\033[0;31m"

// iterates an null-terminate str (\0)
// and check if its chars is digit
bool strisdigits(const char *str) {
  for (int i = 0; str[i] != '\0'; ++i) {
    if (!isdigit(str[i]))
      return false;
  }
  return true;
}

// From
// https://pt.stackoverflow.com/questions/37031/inverter-um-n%C3%BAmero-de-3-d%C3%ADgitos-em-c
unsigned int reverse_int(unsigned int v) {
  unsigned int vreversed = 0;
  while (v > 0) {
    vreversed = 10 * vreversed + v % 10;
    v /= 10;
  }
  return vreversed;
}

void check_palindromes(unsigned int min, unsigned int max) {
  for (int i = min; i < max; ++i) {
    unsigned int reversed = reverse_int(i);
    if (reversed == i) {
      printf("%d\n", reversed);
    }
  }
}

int main(int argc, char *argv[]) {
  if (argc < 3) {
    printf("Usage %s <min_number> <max_number>\n",
           argv[0]); // argv[0] is program binary file
    return 1;
  }
  // get arguments and check if its a valid int value
  char *minStr = argv[1];
  char *maxStr = argv[2];
  if (!strisdigits(minStr) || !strisdigits(maxStr)) {
    printf("%s[ERROR]%s Min and Max values should be Integers!\n", RED, RESET);
    return 0;
  }
  // atoi: converts string(char*) to int
  // returns 0 if its not valid
  unsigned int min = atoi(minStr);
  unsigned int max = atoi(maxStr);
  if (min >= max) {
    printf("%s[ERROR]%s Min can't be higher or equals than max.\n", RED, RESET);
    return 1;
  }
  check_palindromes(min, max);
  return 0;
}
