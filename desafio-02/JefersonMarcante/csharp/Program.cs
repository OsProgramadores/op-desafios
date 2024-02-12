bool EhPrimo(int num)
{
    int aux = 0;

    if (num < 2)
        return false;

    for(int j = 2; j <= num; j++)
        if (num % j == 0)
            aux++;

    if (aux <= 1)
        return true;

    return false;
}

for (int i = 0; i < 10000; i++)
    if (EhPrimo(i))
        Console.WriteLine(i);