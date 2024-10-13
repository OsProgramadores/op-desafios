using System;
using System.IO;

class Program
{
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
            using (StreamReader sr = new StreamReader(filePath))
            {
                string line;
                while ((line = sr.ReadLine()) != null)
                {
                    Console.WriteLine(ProcessFraction(line.Trim()));
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"erro: {ex.Message}");
        }
    }

    static string ProcessFraction(string input)
    {
        if (int.TryParse(input, out int simpleNumber))
        {
            return simpleNumber.ToString();
        }
        string[] parts = input.Split('/');
        if (parts.Length == 2 && int.TryParse(parts[0], out int numerator) && int.TryParse(parts[1], out int denominator))
        {
            if (denominator == 0)
            {
                return "ERR";
            }

            int gcd = GCD(Math.Abs(numerator), Math.Abs(denominator));
            numerator /= gcd;
            denominator /= gcd;

            if (denominator == 1)
            {
                return numerator.ToString();
            }
            if (Math.Abs(numerator) > Math.Abs(denominator))
            {
                int wholePart = numerator / denominator;
                int remainder = Math.Abs(numerator % denominator);
                return $"{wholePart} {remainder}/{Math.Abs(denominator)}";
            }
            return $"{numerator}/{denominator}";
        }
        return "ERR";
    }
    static int GCD(int a, int b)
    {
        while (b != 0)
        {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
