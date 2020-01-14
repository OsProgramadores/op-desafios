using System;

namespace desafio2 {
    class Primos {
        static void Main () {
            int counter = 0;
            for (int i = 0; i <= 100; i++) {
                counter = 0;
                for (int j = 1; j <= i; j++) {
                    if (i % j == 0) counter++;
                    if (counter > 2) break;
                }
                if (counter == 2) {
                    Console.WriteLine (i);
                }

            }
        }
    }
}