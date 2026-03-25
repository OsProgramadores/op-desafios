using System;
using System.Collections.Generic;
using System.IO;
using System.Numerics;

public class Program
{
    private const string Digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    private static BigInteger MaxLimit = ConvertToBase10("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz", 62);

    private static void Main(string[] args)
    {
        if (args.Length < 1)
        {
            Console.WriteLine("os argumentos estao vazios, passe o caminho do arquivo no argumento");
            return;
        }

        var filePath = args[0];

        if (!File.Exists(filePath))
        {
            Console.WriteLine("arquivo não encontrado.");
            return;
        }

        try
        {
            var lines = File.ReadAllLines(filePath);

            foreach (var line in lines)
            {
                var parts = line.Split(' ');
                if (parts.Length != 3 ||
                    !int.TryParse(parts[0], out int baseInput) ||
                    !int.TryParse(parts[1], out int baseOutput) ||
                    baseInput < 2 || baseInput > 62 ||
                    baseOutput < 2 || baseOutput > 62 ||
                    !IsValidNumberForBase(parts[2], baseInput))
                {
                    Console.WriteLine("???");
                    continue;
                }

                var numberInput = parts[2];
                try
                {
                    var numberBase10 = ConvertToBase10(numberInput, baseInput);

                    if (numberBase10 > MaxLimit)
                    {
                        Console.WriteLine("???");
                        continue;
                    }

                    var result = ConvertFromBase10(numberBase10, baseOutput);
                    Console.WriteLine(result);
                }
                catch
                {
                    Console.WriteLine("???");
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"erro: {ex.Message}");
        }
    }

    private static bool IsValidNumberForBase(string number, int baseInput)
    {
        foreach (var c in number)
        {
            var digitValue = Digits.IndexOf(c);
            if (digitValue == -1 || digitValue >= baseInput)
            {
                return false;
            }
        }
        return true;
    }

    private static BigInteger ConvertToBase10(string number, int baseInput)
    {
        BigInteger result = 0;
        foreach (var c in number)
        {
            result = result * baseInput + Digits.IndexOf(c);
        }
        return result;
    }

    private static string ConvertFromBase10(BigInteger number, int baseOutput)
    {
        if (number == 0)
            return "0";

        var result = "";
        while (number > 0)
        {
            int remainder = (int)(number % baseOutput);
            result = Digits[remainder] + result;
            number /= baseOutput;
        }
        return result;
    }
}
