using System;

namespace OsProgramadores {
    class Desafio02 {          
        static void Main(string[] args) {
            for (int i = 1; i <= 10000; i++) {
                bool primo = true;
                for (int j = 2; j <= Math.Floor(Math.Sqrt(i)); j++) {
                    if (i % j == 0) {
                        primo = false;
                        break;
                    }
                }

                if (primo) {
                    Console.WriteLine(i);
                }
            }
        }
    }
}