using System;
using System.Collections.Generics

namespace csharp
{
        class numerosPrimos
        {
            static void Main(string[] args)
            {
            var numeros = new List<int>();
            var primos = new List<int>();

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