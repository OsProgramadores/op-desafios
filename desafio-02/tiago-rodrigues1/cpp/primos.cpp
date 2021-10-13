#include <bits/stdc++.h>

using namespace std;

int main()
{
    cout << 2 << "\n";

    for (int i = 3; i <= 10000; i++)
    {
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