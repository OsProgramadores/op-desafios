using System;

namespace palindromos;

class Program
{
    public static void Main(string[] args)
    {
        Palindromo palindromo = new Palindromo();
        
        Console.WriteLine("Informe o número inicial para validação dos palíndromos: ");
        string inicio = Console.ReadLine();
        Console.WriteLine("Informe o número final para validação dos palíndromos: ");
        string fim = Console.ReadLine();
        
        Console.WriteLine("\nNumeros palíndromos entre " + inicio + " e " + fim + ": ");
        foreach (ulong item in palindromo.PalindromosEntre(inicio, fim))   
        {
            Console.WriteLine(item);
        }
        
    }
}