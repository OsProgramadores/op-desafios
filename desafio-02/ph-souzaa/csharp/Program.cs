using System;

namespace Primos
{
    class Program
    {
        static void Main(string[] args)
        {

            int maxNum = 10000;

            for(int i = 2; i <= maxNum; i++)
            {
                if(verificaPrimo(i) == true)
                {
                    Console.WriteLine(i);
                }

            }
        }

        static public Boolean verificaPrimo(int n)
        {
            Boolean retorno = false;
            int contador = 0;
            if (n == 1)
            {
                retorno = true;
            }
            else
            {
                for (int i = 1; i <= n; i++)
                {
                    if (n % i == 0)
                    {
                        contador++;
                    }
                }
                if (contador == 2)
                {
                    retorno = true;
                }
            }
            return retorno;

        }
    }
}
