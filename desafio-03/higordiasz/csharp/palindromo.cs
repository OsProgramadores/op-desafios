using System;

namespace palindromo
{
    class Program
    {
        static void Palimdromo(int a, int b)
        {
            for (int i = a; i <= b; i++)
            {
                if (i < 10)
                {
                    Console.WriteLine(i);
                    continue;
                }
                char[] nArr = i.ToString().ToCharArray();
                char[] zArr = new char[nArr.Length];
                int c = 0;
                for (int j = nArr.Length; j > 0; j--)
                {
                    zArr[c] = nArr[j - 1];
                    c++;
                }
                string d = new String(nArr);
                string e = new String(zArr);
                if (d == e)
                {
                    Console.WriteLine(i);
                }
            }
            return;
        }
        static void Main()
        {
            Palimdromo(1, 10000);
        }
    }
}
