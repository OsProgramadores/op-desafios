using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

public class Program
{
    public static void Main(string[] args)
    {
        if (args.Length < 1)
        {
            Console.WriteLine("usio correto: dotnet run <arquivo>");
            return;
        }

        var fileName = args[0];
        if (!File.Exists(fileName))
        {
            Console.WriteLine($"arquivo não encontrado: {fileName}");
            return;
        }

        var primes = GeneratePrimesUpTo(9973);
        var biggestSequence = string.Empty;
        var decimalDigits = ReadDigitsFromFile(fileName);

        for (var i = 0; i < decimalDigits.Length; i++)
        {
            var sequence = FindLongestPrimeSequence(primes, decimalDigits, i);
            if (sequence.Length > biggestSequence.Length)
            {
                biggestSequence = sequence;
            }
        }

        Console.WriteLine(biggestSequence);
    }
    private static HashSet<int> GeneratePrimesUpTo(int limit)
    {
        var primes = new HashSet<int>();
        for (var num = 2; num <= limit; num++)
        {
            if (IsPrime(num))
            {
                primes.Add(num);
            }
        }
        return primes;
    }
    private static bool IsPrime(int number)
    {
        if (number < 2) return false;
        var sqrt = (int)Math.Sqrt(number);
        for (var i = 2; i <= sqrt; i++)
        {
            if (number % i == 0) return false;
        }
        return true;
    }
    private static string ReadDigitsFromFile(string fileName)
    {
        using var reader = new StreamReader(fileName);
        var content = reader.ReadToEnd();

        var digits = new List<char>();
        foreach (var ch in content)
        {
            if (char.IsDigit(ch))
            {
                digits.Add(ch);
            }
            else if (ch == '.')
            {
                digits.Clear();
            }
            else if (!char.IsWhiteSpace(ch))
            {
                throw new Exception("arquivo contem caracteres invalidos");
            }
        }

        return new string(digits.ToArray());
    }
    private static string FindLongestPrimeSequence(HashSet<int> primes, string digits, int startIndex)
    {
        var sequence = string.Empty;
        var longestSequence = string.Empty;

        for (var i = startIndex; i < Math.Min(startIndex + 4, digits.Length); i++)
        {
            sequence += digits[i];
            if (!int.TryParse(sequence, out var number) || !primes.Contains(number)) continue;

            var newSequence = FindLongestPrimeSequence(primes, digits, i + 1);
            var candidate = sequence + newSequence;
            if (candidate.Length > longestSequence.Length)
            {
                longestSequence = candidate;
            }
        }

        return longestSequence;
    }
}
