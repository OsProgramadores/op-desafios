using System;

namespace Desafio02
{
    class Program
    {
        static void Main(string[] args)
        {
            int numero = 2;
            int[] numPrimos = new int[10000];
            int contador = 0;
            bool primo;

            while (numero <= 10000)
            {
                primo = true;
                for (int i = 2; i <= (int)Math.Sqrt(numero); i++)
                {
                    if (numero % i == 0)
                    {
                        primo = false;
                        break;
                    }
                }

                if (primo)
                {
                    numPrimos[contador] = numero;
                    contador++;
                }
                numero++;
            }
            Console.WriteLine("Os números primos de 1 a 10.000 são:");
            for (int i = 0; i < contador; i++)
            {
                Console.Write(numPrimos[i] + " ");
            }

            Console.ReadLine();
        }
    }
}
