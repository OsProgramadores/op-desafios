#include <iostream>
#include <list>

using namespace std;


int main()
{
    list<int> primes = { 2, 3, 5, 7 };

    for( int i = 11; i <= 10000; ++i ) 
    {
        bool is_prime = true;

        for( int prime: primes )
        {
            if( i % prime == 0 )
            {
                is_prime = false;
                break;
            }
        }

        if( is_prime )
            primes.push_back(i);
    }

    for( int prime: primes )
        cout << prime << endl;
}

