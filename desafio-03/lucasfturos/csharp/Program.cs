using System;
using System.Collections.Generic;

namespace Palindromo
{
    class Program
    {
        public static long num_inicial;
        public static long num_final;

        public static void exibeInfo()
        {
            Console.WriteLine("Informe os numeros limites para achar os palindromos");
            Console.WriteLine("Inserir o numero limite inicial:");
            num_inicial = Convert.ToInt64(Console.ReadLine());
            Console.WriteLine("Inserir o numero limite final:");
            num_final = Convert.ToInt64(Console.ReadLine());

            if (num_final < num_inicial)
            {
                Console.WriteLine("Erro: Execute o programa novamente");
                Console.WriteLine(
                    "Informe um numero maior que o limite inicial para o limite final"
                );
                Environment.Exit(0);
            }
            else if (num_final <= -1 || num_inicial <= -1)
            {
                Console.WriteLine("Erro: Execute o programa novamente");
                Console.WriteLine("Insira apenas numeros inteiros e positivos");
                Environment.Exit(0);
            }
            else if (num_final == num_inicial)
            {
                Console.WriteLine("Erro: Execute o programa novamente");
                Console.WriteLine("Insira numeros diferentes");
                Environment.Exit(0);
            }
        }

        private static bool isPalindromo(long num)
        {
            long test_palindrom = 0,
                aux = num,
                resto;
            while (num > 0)
            {
                resto = num % 10;
                test_palindrom = (test_palindrom * 10) + resto;
                num = num / 10;
            }
            return aux == test_palindrom;
        }

        public static void exibePalindromo()
        {
            List<long> palindromo = new List<long>();
            for (long i = num_inicial; i < num_final + 1; i++)
            {
                if (isPalindromo(i))
                {
                    palindromo.Add(i);
                }
            }

            Console.WriteLine(
                "Numero que sao palindromos entre " + num_inicial + " a " + num_final + ":"
            );

            foreach (long values in palindromo)
            {
                Console.Write(values + " ");
            }
            Console.WriteLine();
        }

        static void Main(string[] args)
        {
            exibeInfo();
            exibePalindromo();
        }
    }
}
