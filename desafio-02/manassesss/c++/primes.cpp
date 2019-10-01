#include <iostream>
#define N 10000

using namespace std;


void isPrime(int k)
{
	int c = 1;
	for ( int i = 2 ; i <= k - 1; i++)
	{
		if(k % 2 != 0 || i == 2 )
		{
			if (k % i == 0)
			{
				c++;
			}
			if(c > 2)
				break;
		}
	}
	if (c + 1 == 2)
		cout << k << " ";
}

int main ()
{
	for (int i = 2 ; i <= N ; i++)
	{
		isPrime(i);
	}
	return 0;
}
