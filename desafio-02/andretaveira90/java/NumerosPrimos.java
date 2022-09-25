public class NumerosPrimos {
    public static void main(String[] args) {
        for (int numero = 2; numero <= 10000; numero++) {
            boolean ehPrimo = true;
            for (int contador = 2; contador < numero; contador++) {
                if (numero % contador == 0) {
                    ehPrimo = false;
                }
            }
            if (ehPrimo) {
                System.out.println(numero);
            }
        }
    }
}

