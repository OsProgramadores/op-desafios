using System;

namespace Anagramas;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Escreva sua expressão: ");
        string expressao = Console.ReadLine().ToUpper().Trim();
        string expressaoSemEspacos = (expressao.Replace(" ", ""));

        foreach (char c in expressaoSemEspacos)
        {
            if (!char.IsLetter(c) || c < 'A' || c > 'Z')
            {
                Console.WriteLine("Escreva somente expressões de A a Z. (Sem acentos e números)");
                Console.ReadLine();
                return;   
            }
        }
        string[] palavras = LerArquivo();
        FormarAnagrama(palavras, expressao);
        Console.ReadLine();
    }

    private static string[] LerArquivo()
    {
        string caminho = @"C:\Hrsh\dev\op-desafios\desafio-06\leohiroshi\csharp\words.txt";
        return File.ReadAllLines(caminho);
    }

    static void FormarAnagrama(string[] linhas, string expressao)
    {
        string expressaoSemEspacos = expressao.Replace(" ", "");
        string expressaoOrdenada = new string(expressaoSemEspacos.OrderBy(c => c).ToArray());
        bool naoTemAnagrama = true;
        int contador = 0;
        List<string> anagramas = new();
        foreach (string arquivo in linhas)
        {
            string palavra = arquivo.Replace(" ", "").ToUpper();
            string palavraOrdenada = new string(palavra.OrderBy(c => c).ToArray());
            if (palavraOrdenada == expressaoOrdenada)
            {
                anagramas.Add(palavra);
            }
        }
        if (anagramas.Count == 0)
        {
            Console.WriteLine($"Não foram encontrados nenhum anagrama para a palavra {expressao}");
        }
        else
        {
            Console.Write($"O(s) anagrama(s) da expressão {expressao} são:");
            foreach (var palavra in anagramas)
            {
                Console.Write($" - {palavra}");
            }
        }
    }
}
