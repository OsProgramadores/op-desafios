int numDivisor;

for (int num = 1; num <= 10000; num++)
{
    numDivisor = 0;
    for (int i = num; i > 0; i--)
    {
        if (num % i == 0)
            numDivisor++;
    }

    if (numDivisor == 2)
        Console.WriteLine(num);
}

// 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,53, 59, 61, 67, 71, 73, 79, 83, 89, 97 -- Números primos.