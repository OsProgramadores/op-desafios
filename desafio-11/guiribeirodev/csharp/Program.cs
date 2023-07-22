using System.Text;

internal class Program
{
    public static bool IsPrime(int number)
    {
        var divisor = 0;

        for (var count = 1; count <= number / 2; count++)
        {
            if (number % count == 0)
            {
                divisor++;
            }

            if (divisor > 1)
            {
                return false;
            }
        }

        if (divisor == 1)
        {
            return true;
        }

        return false;
    }

    public static HashSet<int> GetPrimeNumbers(int startNumber, int endNumber)
    {
        var primes = new HashSet<int>();

        for (var i = startNumber; i <= endNumber; i++)
        {
            if (IsPrime(i))
            {
                primes.Add(i);
            }
        }

        return primes;
    }

    public static StringBuilder FindLongestSequence(string numberPi, HashSet<int> primeNumbers)
    {
        var longestSequence = new StringBuilder();

        void Sequence(int startIndex, StringBuilder currentSequence)
        {
            var updatedSequence = new StringBuilder();

            for (var i = 4; i > 0 && startIndex + i < numberPi.Length; i--)
            {
                var currentChars = numberPi.AsSpan(startIndex, i);

                if (int.TryParse(currentChars, out int currentNumbers))
                {
                    if (primeNumbers.Contains(currentNumbers))
                    {
                        updatedSequence.Clear();

                        updatedSequence.Append(currentSequence);
                        updatedSequence.Append(currentChars);

                        Sequence(startIndex + i, updatedSequence);
                    }
                }
            }

            if (updatedSequence.Length > longestSequence.Length)
            {
                longestSequence.Clear();
                longestSequence.Append(updatedSequence);
            }
        }

        for (var i = 0; i < numberPi.Length && numberPi.Length - i > longestSequence.Length; i++)
        {
            Sequence(i, new StringBuilder());
        }

        return longestSequence;
    }

    private static void Main(string[] args)
    {
        try
        {
            var file = args[0];
            var data = File.ReadAllText(file)[2..];

            var primeNumbers = GetPrimeNumbers(2, 9973);
            var primeNumber = IsPrime(0);

            Console.WriteLine(primeNumber);

            var longestSequence = FindLongestSequence(data, primeNumbers);

            Console.WriteLine(longestSequence);
        }
        catch (System.IndexOutOfRangeException)
        {
            Console.WriteLine("Por favor coloque como argumento o arquivo com o número Pi");
            throw;
        }
    }
}
