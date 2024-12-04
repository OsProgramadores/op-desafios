using System;
using System.IO;
using System.Numerics;
using System.Security;
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

        try//Adiciona os outros tratamentos de erro, exceto os que já são tratados pelo !File.Exists
        {
            ProcessFile(fileName);
        }
        catch (ArgumentException ex)
        {
            Console.WriteLine($"erro: {ex.Message}");
        }
        catch (UnauthorizedAccessException)
        {
            Console.WriteLine("erro: acesso negado ao arquivo");
        }
        catch (SecurityException)
        {
            Console.WriteLine("erro: sem permissões para acessar o arquivo");
        }
        catch (IOException ex)
        {
            Console.WriteLine($"erro: {ex.Message}");
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

            var result = IsPowerOfTwo(number);
            Console.WriteLine(result.IsPowerOfTwo ? $"{number} true {result.Exponent}" : $"{number} false");
        }
    }
    private static PowerOfTwoResult IsPowerOfTwo(BigInteger number)//Nodificado para usar record
    {
        var exponent = 0;

        while (number > 1)
        {
            if (number % 2 != 0)
                return new PowerOfTwoResult(false, -1);

            number /= 2;
            exponent++;
        }

        return new PowerOfTwoResult(true, exponent);
    }
}
public record PowerOfTwoResult(bool IsPowerOfTwo, int Exponent);
