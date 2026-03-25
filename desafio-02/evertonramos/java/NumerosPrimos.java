import java.util.ArrayList;
import java.util.List;

public class NumerosPrimos {

    public static void main(String[] args) {
        List<Integer> primos = new ArrayList<>();

        primos.add(2); // primeiro número primo

        for (int numero = 3; numero <= 10000; numero += 2) {
            for (Integer primo : primos) {
                if (numero % primo == 0) {
                    break; // não é primo
                }

                if ((double) numero / primo < primo) { // primo!
                    primos.add(numero);

                    break;
                }
            }
        }

        System.out.println(primos);
    }
}
