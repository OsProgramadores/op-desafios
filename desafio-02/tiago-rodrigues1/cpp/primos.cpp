#include <bits/stdc++.h>

using namespace std;

int main()
{
    for (int i = 1; i <= 10000; i++)
    {
        if (i == 2)
        {
            cout << i << "\n";
        }

        if (i % 2 != 0)
        {
            if (sqrt(i) != floor(sqrt(i)))
            {
                cout << i << "\n";
            }
        }
    }

    return 0;
}