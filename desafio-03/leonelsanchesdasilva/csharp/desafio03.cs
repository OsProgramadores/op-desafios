using System;

namespace OsProgramadores {
    internal static class StringExtensions {
        internal static string Reverse(this string s)
        {
            char[] charArray = s.ToCharArray();
            Array.Reverse(charArray);
            return new string(charArray);
        }
    }

    class Desafio03 {
        static void Main(string[] args) {
            for (int i = 1; i <= 3010; i++) {
                if (i.ToString() == i.ToString().Reverse()) {
                    Console.WriteLine(i);
                }
            }
        }
    }
}