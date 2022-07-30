namespace NumPrimosDesafio
{
    public class Program
    {
        static void Main(string[] args)
        {
            const int limiteDesafio = 10000;
            List<int> primos = new();

            for (int i = 3; i < limiteDesafio; i++)
            {
                if ((i % 2) == 0) continue;

                bool ehPrimo = true;
                foreach (int j in primos)
                {
                    if (i % j == 0)
                    {
                        ehPrimo = false;
                        break;
                    }
                }
                if (ehPrimo)
                {
                    primos.Add(i);
                }
            }
            primos.Insert(0, 2);

            foreach (int numPrimo in primos)
            {
                Console.WriteLine(numPrimo);
            }
        }
    }
}