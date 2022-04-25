using System;
using System.Collections.Generic;
using System.Linq;

namespace PALÍNDROMOS
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Digite o numero inicial:");
            long NumInicial = long.Parse(Console.ReadLine());
            Console.WriteLine("Digite o numero Final:");
            long NumFinal = long.Parse(Console.ReadLine());
            List<long> list = Palindromos(NumInicial, NumFinal);
            foreach (var i in list)
            {
                Console.WriteLine(i);
            }
        }
        public static List<long> Palindromos(long numInicial, long numFinal)
        {
            List<long> numeros = new List<long>();
            List<long> palindromos = new List<long>();
            if (numInicial >= 0 && numFinal > numInicial)
            {
                for (var i = numInicial; i <= numFinal; i++)
                {
                    numeros.Add(i);
                }
                var convertNumString = numeros.Select(x => x.ToString());
                foreach (string obj in convertNumString)
                {
                    string inverso = String.Concat(obj.Reverse().Where(x => obj.Contains(x)));
                    if (obj == inverso || long.Parse(obj) < 10)
                    {
                        palindromos.Add(long.Parse(obj));
                    }
                }
            }
            else
            {
                Console.WriteLine("Numeros Invalidos, Verifique.");
            }
            return palindromos;
        }
    }
}
