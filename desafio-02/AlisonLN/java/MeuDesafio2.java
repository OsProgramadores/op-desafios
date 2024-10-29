package desafioOsProgramadores;

import java.util.Arrays;

public class MeuDesafio2 {

    public static void main(String[] args) {

        int max = 10000;
        boolean[] numPrimos = new boolean[max + 1];

        Arrays.fill(numPrimos, true);

        for (int i = 2; i * i <= max; i++) {
            if (numPrimos[i]) {
                for (int j = i * i; j <= max; j += i) {
                    numPrimos[j] = false;
                }
            }
        }

        for (int i = 2; i <= max; i++) {
            if (numPrimos[i]) {
                System.out.print(i + " ");
            }
        }
    }
}