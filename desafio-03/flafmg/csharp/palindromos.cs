    using System;

    class Program
    {
        static void Main()
        {
            Console.WriteLine("Digite o número inicial:");
            int start = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Digite o número final:");
            int end = Convert.ToInt32(Console.ReadLine());

            PrintPalindromes(start, end);
        }

        static bool IsPalindrome(int number)
        {
            string strNumber = number.ToString();
            char[] charArray = strNumber.ToCharArray();
            Array.Reverse(charArray);
            string reversedStr = new string(charArray);
            return strNumber == reversedStr;
        }

        static void PrintPalindromes(int start, int end)
        {
            for (int i = start; i <= end; i++)
            {
                if (IsPalindrome(i))
                {
                    Console.Write(i + " ");
                }
            }
            Console.WriteLine();
        }
    }
