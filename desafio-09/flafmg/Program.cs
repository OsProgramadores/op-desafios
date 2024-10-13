using System;
using System.Collections.Generic;
using System.Numerics;

class Program
{
    private const string Digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

    static void Main(string[] args)
    {
        if (args.Length < 1)
        {
            Console.WriteLine("os argumentos estao vazios, passe o caminho do arquivo no argumento");
            return;
        }

        string filePath = args[0];

        try
        {
            var lines = System.IO.File.ReadAllLines(filePath);

            BigInteger maxLimit = ConvertToBase10("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz", 62);

            foreach (var line in lines)
            {
                string[] parts = line.Split(' ');
                if (parts.Length != 3)
                {
                    Console.WriteLine("???");
                    continue;
                }

                int baseInput, baseOutput;
                string numberInput = parts[2];
                
                if (!int.TryParse(parts[0], out baseInput) || !int.TryParse(parts[1], out baseOutput))
                {
                    Console.WriteLine("???");
                    continue;
                }
                
                if (baseInput < 2 || baseInput > 62 || baseOutput < 2 || baseOutput > 62)
                {
                    Console.WriteLine("???");
                    continue;
                }
                
                if (!IsValidNumberForBase(numberInput, baseInput))
                {
                    Console.WriteLine("???");
                    continue;
                }

                try
                {
                    BigInteger numberBase10 = ConvertToBase10(numberInput, baseInput);
                    
                    if (numberBase10 > maxLimit)
                    {
                        Console.WriteLine("???");
                        continue;
                    }
                    
                    string result = ConvertFromBase10(numberBase10, baseOutput);
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
    static bool IsValidNumberForBase(string number, int baseInput)
    {
        foreach (char c in number)
        {
            int digitValue = Digits.IndexOf(c);
            if (digitValue == -1 || digitValue >= baseInput)
            {
                return false;
            }
        }
        return true;
    }
    
    static BigInteger ConvertToBase10(string number, int baseInput)
    {
        BigInteger result = 0;
        foreach (char c in number)
        {
            result = result * baseInput + Digits.IndexOf(c);
        }
        return result;
    }
    
    static string ConvertFromBase10(BigInteger number, int baseOutput)
    {
        if (number == 0)
            return "0";

        string result = "";
        while (number > 0)
        {
            int remainder = (int)(number % baseOutput);
            result = Digits[remainder] + result;
            number /= baseOutput;
        }
        return result;
    }
}
