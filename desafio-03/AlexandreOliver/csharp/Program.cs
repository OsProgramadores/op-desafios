using System;
using System.Collections.Generic;

namespace csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            int inicio, fim;

            Console.Write("Valor inicial: ");
            inicio = int.Parse(Console.ReadLine());
            Console.Write("Valor Final: ");
            fim = int.Parse(Console.ReadLine());

            for (int num = inicio; num <= fim; num++)
            {
                int tamanho = num.ToString().Length;

                List<int> numero = new List<int>();
                
                for (int i = 0; i < tamanho; i++)
                {
                    numero.Add((int)(num.ToString()[i]));
                }
                
                List<int> reverso = new List<int>(numero);
                reverso.Reverse();

                int count = 0;
                for (int i = 0; i < tamanho; i++)
                {
                    if (numero[i] == reverso[i])
                    {
                        count++;
                    }
                }

                if (count == tamanho)
                    Console.WriteLine(num);
            }
        }
    }
}