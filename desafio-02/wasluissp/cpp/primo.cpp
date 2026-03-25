#include <iostream>

using namespace std;

int main() {
  int i, j;
  bool isPrime;

  for (i = 2; i <= 10000; i++) {
    isPrime = true;
    for (j = 2; j * j <= i; j++) {
      if (i % j == 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      cout << i << endl;
    }
  }

  return 0;
}
