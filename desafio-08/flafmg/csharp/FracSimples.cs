using System;
using System.IO;

public class Program
{
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
            var sr = new StreamReader(filePath);
            string line;

            while ((line = sr.ReadLine()) != null)
            {
                Console.WriteLine(ProcessFraction(line.Trim()));
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"erro: {ex.Message}");
        }
    }

    private static string ProcessFraction(string input)
    {
        if (int.TryParse(input, out int simpleNumber))
        {
            return simpleNumber.ToString();
        }
<<<<<<< HEAD
        string[] parts = input.Split('/');
=======

        var parts = input.Split('/');
>>>>>>> 5560d2a (corrige legibilidade do codigo)
        if (parts.Length == 2 && int.TryParse(parts[0], out int numerator) && int.TryParse(parts[1], out int denominator))
        {
            if (denominator == 0)
            {
                return "ERR";
            }

            var gcd = GCD(Math.Abs(numerator), Math.Abs(denominator));
            numerator /= gcd;
            denominator /= gcd;

            if (denominator == 1)
            {
                return numerator.ToString();
            }

            if (Math.Abs(numerator) > Math.Abs(denominator))
            {
<<<<<<< HEAD
                int wholePart = numerator / denominator;
                int remainder = Math.Abs(numerator % denominator);
=======
                var wholePart = numerator / denominator;
                var remainder = Math.Abs(numerator % denominator);
>>>>>>> 5560d2a (corrige legibilidade do codigo)
                return $"{wholePart} {remainder}/{Math.Abs(denominator)}";
            }

            return $"{numerator}/{denominator}";
        }
        return "ERR";
    }

    private static int GCD(int a, int b)
    {
        while (b != 0)
        {
            var temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
