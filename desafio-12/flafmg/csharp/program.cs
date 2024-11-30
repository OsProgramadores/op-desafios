using System;
using System.IO;
using System.Numerics;

public class Program
{
    private static void Main(string[] args)
    {
        if (args.Length != 1)
        {
            Console.WriteLine("uso correto: dotnet run <arquivo>");
            return;
        }

        var fileName = args[0];
        if (!File.Exists(fileName))
        {
            Console.WriteLine($"arquivo não encontrado: {fileName}");
            return;
        }

        try
        {
            ProcessFile(fileName);
        }
        catch (IOException ex)
        {
            Console.WriteLine($"erro ao processar o arquivo: {ex.Message}");
        }
    }

    private static void ProcessFile(string fileName)
    {
        var lines = File.ReadAllLines(fileName);
        foreach (var line in lines)
        {
            if (!BigInteger.TryParse(line, out var number))
            {
                Console.WriteLine($"{line} false");
                continue;
            }

            if (number <= 0)
            {
                Console.WriteLine($"{number} false");
                continue;
            }

            var (isPowerOfTwo, exponent) = IsPowerOfTwo(number);
            Console.WriteLine(isPowerOfTwo ? $"{number} true {exponent}" : $"{number} false");
        }
    }

    private static (bool, int) IsPowerOfTwo(BigInteger number)
    {
        var exponent = 0;

        while (number > 1)
        {
            if (number % 2 != 0)
                return (false, -1);

            number /= 2;
            exponent++;
        }

        return (true, exponent);
    }
}
