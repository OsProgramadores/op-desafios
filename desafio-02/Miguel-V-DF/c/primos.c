#include <stdio.h>
#include <math.h>

int main()
{
    printf("2\n");
    for (int i = 3; i < 10000; i++)
    {
        int notP = 0;
        if(i % 2 != 0)
        {
            int j = 2;
            int result = 1;
            while(notP == 0 && j <= sqrt(i))
            {
                result = i % j;
                if(result == 0)
                {
                    notP++;
                }
                j++;
            }
            if(notP == 0)
            {
                printf("%d\n", i);
            }
        }
    }

    return 0;
}