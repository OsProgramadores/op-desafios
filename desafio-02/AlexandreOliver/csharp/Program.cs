using System;

namespace csharp
{
    class Program
    {
        static void Main(string[] args)
        { 
            int countDivisores = 1;
            
            for (int n = 1; n < 10000; n++)
            {
                for (int div = n; div != 1; div--)
                {
                    if (n % div == 0)
                        countDivisores++;
                }

                if (countDivisores == 2)
                    Console.WriteLine(n);
                
                countDivisores = 1;
                
            } 
        }
    }
}
