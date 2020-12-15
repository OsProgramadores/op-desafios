
using System;
class MainClass
{
    static bool isPalindrome(int original, int reverse)
    {
        if (original == reverse)
        {
            return true;
        }
        return false;
    }

    static void Main(string[] args)
    {
        int n, reverse = 0, rem;
        Console.WriteLine("Type the min number: ");
        int min = int.Parse(Console.ReadLine());
        Console.WriteLine("Type the max number: ");
        int max = int.Parse(Console.ReadLine());
        for (int counter = min; counter <= max; counter++)
        {
            n = counter;
            while (n != 0)
            {
                rem = n % 10;
                reverse = reverse * 10 + rem;
                n /= 10;
            }
            if (isPalindrome(counter, reverse))
            {
                Console.WriteLine(counter);
            }
            rem = 0;
            reverse = 0;
        }
    }
}