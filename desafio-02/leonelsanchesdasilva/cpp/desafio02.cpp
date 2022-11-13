#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    for (int i = 1; i <= 10000; i++) {
        int primo = 1;
        for (int j = 2; j <= floor(sqrt(i)); j++) {
            if (i % j == 0) {
                primo = 0;
                break;
            }
        }

        if (primo > 0) {
            cout << i << endl;
        }
    }

    return 0;
}