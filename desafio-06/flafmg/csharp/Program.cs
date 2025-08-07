using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;

public class AnagramGenerator
{
    private static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("uso correto: dotnet run <expressao>");
            return;
        }

        var expression = string.Join("", args).ToUpper().Replace(" ", "");
        if (!IsValidExpression(expression))
        {
            Console.WriteLine("erro: a expressão contém caracteres inválidos. somente letras de A a Z são permitidas");
            return;
        }

        var validWords = LoadValidWords("words.txt");
        if (validWords == null || validWords.Count == 0)
        {
            Console.WriteLine("erro: words.txt está vazio ou não foi possível ler");
            return;
        }

        var anagrams = GenerateAnagrams(expression, validWords);

        if (anagrams.Count > 0)
        {
            foreach (var anagram in anagrams)
            {
                Console.WriteLine(anagram);
            }
        }
        else
        {
            Console.WriteLine("nenhum anagrama encontrado.");
        }
    }
    private static bool IsValidExpression(string expression)
    {
        return expression.All(c => c >= 'A' && c <= 'Z'); //para garantir que seja so de A a Z
    }

    private static HashSet<string> LoadValidWords(string filePath)
    {
        try
        {
            return File.ReadAllLines(filePath)
                .Select(line => line.Trim().ToUpper())
                .Where(line => line.All(char.IsLetter))
                .ToHashSet();
        }
        catch
        {
            return null;
        }
    }

    private static List<string> GenerateAnagrams(string expression, HashSet<string> validWords)
    {
        var result = new HashSet<string>();
        var charCounts = GetCharCounts(expression);
        GenerateAnagramsRecursive(expression, validWords, new HashSet<string>(), result, charCounts);
        return result.OrderBy(x => x).ToList();
    }

    private static void GenerateAnagramsRecursive(string remaining, HashSet<string> validWords,
        HashSet<string> currentWords, HashSet<string> result, Dictionary<char, int> charCounts)
    {
        if (string.IsNullOrEmpty(remaining))
        {
            var anagram = string.Join(" ", currentWords.OrderBy(word => word));
            result.Add(anagram);
            return;
        }

        foreach (var word in validWords)
        {
            if (CanFormWord(word, charCounts))
            {
                var newCharCounts = UpdateCharCounts(charCounts, word, -1);
                currentWords.Add(word);
                GenerateAnagramsRecursive(RemoveUsedChars(remaining, word), validWords, currentWords, result, newCharCounts);
                currentWords.Remove(word);
            }
        }
    }

    private static Dictionary<char, int> GetCharCounts(string expression)
    {
        var counts = new Dictionary<char, int>();
        foreach (var c in expression)
        {
            if (!counts.ContainsKey(c))
                counts[c] = 0;
            counts[c]++;
        }
        return counts;
    }

    private static bool CanFormWord(string word, Dictionary<char, int> charCounts)
    {
        var tempCounts = new Dictionary<char, int>(charCounts);
        foreach (var c in word)
        {
            if (!tempCounts.ContainsKey(c) || tempCounts[c] <= 0)
                return false;
            tempCounts[c]--;
        }
        return true;
    }

    private static Dictionary<char, int> UpdateCharCounts(Dictionary<char, int> charCounts, string word, int delta)
    {
        var newCounts = new Dictionary<char, int>(charCounts);
        foreach (var c in word)
        {
            if (!newCounts.ContainsKey(c))
                newCounts[c] = 0;
            newCounts[c] += delta;
        }
        return newCounts;
    }

    private static string RemoveUsedChars(string expression, string word)
    {
        foreach (var c in word)
        {
            expression = expression.Remove(expression.IndexOf(c), 1);
        }
        return expression;
    }
}
