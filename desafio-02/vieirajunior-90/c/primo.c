#include <stdio.h>
#include <stdlib.h>

int main()
{
    int arr_primo[10000];

    for(int i = 1; i <= 10000; i++)
    {
        arr_primo[i] = i;
        int count = 0;
        for(int j = 1; j <= arr_primo[i]; j++)
        {
            if (arr_primo[i] % j == 0)
                {
                    count++;
                }
        }
        if (count == 2)
            printf("[%d] ",arr_primo[i]);
    }


    return 0;

}
