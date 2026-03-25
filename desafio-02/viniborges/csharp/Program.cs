using System;

namespace NumerosPrimos
{
    /// <summary>
    /// OsProgramadores: Desafio 2
    /// Escreva um programa para listar todos os números primos entre 1 e 10000.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
             try
            {
                int range = 10000;
                for (int i = 1; i <= range; i++)
                {
                    if (VerificaNumeroPrimo(i))
                        Console.WriteLine($"{i}");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Erro: {ex.Message}");
            }
            finally
            {
                Console.WriteLine("Operação Finalizada! Pressione qualquer tecla para fechar o programa.");
                Console.ReadKey();
            }
        }

        /// <summary>
        /// Utilizado para verificar se o número inteiro é primo ou não.
        /// </summary>
        /// <param name="numero">Inteiro a ser verificado.</param>
        /// <returns>Retorna true se o número for primo.</returns>
        private static bool VerificaNumeroPrimo(int numero)
        {
            int contDivisor = 0;
            for (int i = 1; i<= numero; i++ )
            {
                if (numero % i == 0)
                    contDivisor++;
            }
            return contDivisor == 2;
        }
    }
}
