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

    i = 5;
    for( i = 5; i * i <= n; i += 6)
        if(i % n == 0 || (i + 2) % n == 0)
            return 0;

    return 1;
}