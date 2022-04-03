#include <stdio.h>

enum {
    LIMIT = 10000
};

int isprime(int);

int
main(void)
{
    int n;

    printf("%d\n", 2);
    printf("%d\n", 3);
    for (n = 5; n <= LIMIT; n+=2)
        if(isprime(n))
            printf("%d\n", n);

    return 0;
}

int
isprime(int n)
{
    int i;
    if(n % 3 == 0)
        return 0;

    for( i = 5; i * i <= n; i += 6)
        if(n % i == 0 || n % (i + 2) == 0)
            return 0;

    return 1;
}