using System;
namespace primos
{
    class Program
    {
        static bool Checar(int n)
        {
            int divisores = 0;
            for (int i = 1; i <= n; i++)
            {
                if (n == 0)
                    continue;
                if (n % i == 0)
                    divisores++;
            }
            return divisores == 2;
        }
        static void Primos(int a, int b)
        {
            for(int i = a;  i <= b; i++)
            {
                if (Checar(i))
                    Console.WriteLine(i);
            }
            return;
        }
        static void Main()
        {
            Primos(1, 10000);
        }
    }
}
