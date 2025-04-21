using System;

namespace Palindromos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] palindromo;
            Console.WriteLine("Escreva o primeiro número: ");
            int num01 = int.Parse(Console.ReadLine());
            Console.WriteLine("Escreva o segundo número: ");
            int num02 = int.Parse(Console.ReadLine());

            Console.WriteLine($"Os números {num01} e {num02} são legais!");
            Console.ReadLine();

        }
    }
}