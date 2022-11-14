#include <iostream>

using namespace std;

int main()
{
    char numero[5];
    char inverso[5];
    for (int i = 1; i <= 3010; i++) {
        sprintf(numero, "%d", i);
        sprintf(inverso, "%d", i);
        strrev(inverso);

        if (strcmp(numero, inverso) == 0) {
            cout << i << endl;
        }
    }

    return 0;
}