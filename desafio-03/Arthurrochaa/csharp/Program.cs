using System;
using System.Linq;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace DesafioPalindromos
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Console.Write("Digite o número inicial: ");
                var nInitial = long.Parse(Console.ReadLine());

                Console.Write("Digite o número final: ");
                var nFinal = long.Parse(Console.ReadLine());

                var resul = palindromos(nInitial, nFinal);

                foreach (var r in resul)
                {
                    Console.Write(r + " ");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        public static List<long> palindromos(long numberInitial, long numberFinal)
        {
            List<long> numbers = new List<long>();
            List<long> palins = new List<long>();

            if (numberInitial >= 0 && numberFinal > numberInitial)
            {
                for (var i = numberInitial; i <= numberFinal; i++)
                {
                    numbers.Add(i);
                }

                var numbersString = numbers.Select(x => x.ToString());

                foreach (var n in numbersString)
                {
                    var stringInver = String.Concat(n.Reverse().Where(c => n.Contains(c)));
                    if (n == stringInver || long.Parse(n) < 10)
                    {
                        palins.Add(long.Parse(n));
                    }
                }
            }
            else
            {
                throw new Exception("Valores inválidos!");
            }

            return palins;
        }
    }
}
