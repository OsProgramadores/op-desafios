using System;

namespace palindromos;

class Program
{
    public static void Main(string[] args)
    {
        Palindromo palindromo = new Palindromo();
        
        Console.WriteLine("Palindromos entre 1 e 20: ");
        foreach (ulong item in palindromo.PalindromosEntre("1", "20"))   
        {
            Console.WriteLine(item);
        }
        
        Console.WriteLine("Palindromos entre 3000 e 3010: ");
        foreach (ulong item in palindromo.PalindromosEntre("3000", "3010"))   
        {
            Console.WriteLine(item);
        }
        
        Console.WriteLine("Palindromos entre 101 e 121: ");
        foreach (ulong item in palindromo.PalindromosEntre("101", "121"))   
        {
            Console.WriteLine(item);
        }
    }
}