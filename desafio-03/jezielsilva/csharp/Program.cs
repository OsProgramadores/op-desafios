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

        int numeroInvertido, i, aux, resto;
        numeroInvertido = 0;
        aux = numero;
        do
        {
            resto = numero % 10;
            numeroInvertido = numeroInvertido * 10 + resto;
            aux /= 10;
        } while (aux > 0);

        if (numero == numeroInvertido)
        {
            Console.WriteLine(numeroInvertido + " é um palíndromo");
        }

        return 0;
    }

}

