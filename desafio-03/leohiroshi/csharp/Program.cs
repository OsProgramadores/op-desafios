using System;
using System.Linq;

namespace Palindromos
{
    class Program
    {
        static void Main(string[] args)
        {

            int num01 = ObterNumero("Escreva o primeiro número: ");
            int num02 = ObterNumero("Escreva o segundo número: ");

            if (num01 < 0 || num02 < 0)
            {
                Console.WriteLine("Apenas inteiros positivos podem ser usados como limites.");
                return;
            }

            if (num01 > num02)
            {
                int temp = num01;
                num01 = num02;
                num02 = temp;
            }

            int[] palindromosEncontrados = new int[num02 - num01 + 1];
            int contador = 0;

            for (int i = num01; i <= num02; i++)
            {
                    
                string numero = i.ToString();
                string reverso = new string(numero.Reverse().ToArray());

                if (numero == reverso)
                {
                    palindromosEncontrados[contador] = i;
                    contador++;
                }
            }

            if (contador > 0)
            {
                Console.WriteLine($"Os palíndromos entre {num01} e {num02} são: ");
                Console.WriteLine(string.Join(", ", palindromosEncontrados.Take(contador)));
            }
            else
            {
                Console.WriteLine($"Não há palíndromos entre {num01} e {num02}");
            }
            Console.ReadLine();
        }

        static int ObterNumero (string mensagem)
        {
            int numero = 0;
            do
            {
                Console.Write(mensagem);
                string entrada = Console.ReadLine();

                if (int.TryParse(entrada, out numero) && numero >= 0)
                {
                    return numero;
                }
                else
                {
                    Console.WriteLine("Por favor, insira um número inteiro positivo.");
                }
            } while (true);
        }
    }
}