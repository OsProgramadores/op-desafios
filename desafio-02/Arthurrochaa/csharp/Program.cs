using System;
using System.Collections.Generic;

namespace numerosprimos
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numeros = new List<int>();
            List<int> primos = new List<int>();

            for (int i = 2; i <= 1000; i++)
            {
                numeros.Add(i);
            }

            foreach (int n in numeros)
            {
                int aux = 0;
                foreach (int j in numeros)
                {
                    if (n % j == 0)
                    {
                        aux++;
                    }
                }
                if (aux <= 1)
                {
                    primos.Add(n);
                }
            }

            foreach (int n in primos)
            {
                Console.Write(n + ", ");
            }
        }
    }
}
