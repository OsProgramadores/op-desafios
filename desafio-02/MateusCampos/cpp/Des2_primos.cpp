#include <iostream>
using namespace std;

int main()
{
    cout << "Desfio 2 - Os numeros primos de 0 a 10000 sao: " << endl;

    int primo, num_rac, total = 10000, divisor;

    for (primo = 0; primo <= total; primo++)
    {
        divisor = 0;

        for (num_rac = 2; num_rac <= primo/2; num_rac++)
            if (primo % num_rac == 0)
                divisor++;
        if (divisor == 0)
            cout << primo << " ";
    }
    cout << endl;
    return 0;
}
