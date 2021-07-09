using System;

class MainClass
{
    public static void Main(string[] args)
    {
        int numeroInicial, numeroFinal, auxiliar, testepalindromo;
        int[] listaDeNumeros = new int[100000];


        Console.WriteLine("Digite o numero Inicial?");
        numeroInicial = int.Parse(Console.ReadLine());
        Console.WriteLine("Digite o numero Final?");
        numeroFinal = int.Parse(Console.ReadLine());
        auxiliar = numeroInicial;

        for (int i = auxiliar; i <= numeroFinal; i++)
        {
            listaDeNumeros[i] = auxiliar;
            auxiliar++;
            testepalindromo = listaDeNumeros[i];
            palindromo(testepalindromo);
        }


    }

    public static int palindromo(int numero)
    {
        int divisaoPorOnze = numero % 11;

        if (numero >= 1 && numero <= 9)
        {
            Console.WriteLine(numero + " é um palíndromo");
        }
        else if (divisaoPorOnze == 0)
        {
            Console.WriteLine(numero + " é um palíndromo");
        }
        return 0;
    }

}
