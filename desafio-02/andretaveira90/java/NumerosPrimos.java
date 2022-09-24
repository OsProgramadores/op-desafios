public class NumerosPrimos {

    public static void main(String[] args) {
        int inicioIntervalo = 1;
        int fimIntervalo = 10000;
        int inicioContador = 2;

        for (int numero = (inicioIntervalo + 1); numero <= fimIntervalo; numero++) {
            boolean ehPrimo = true;
            for (int contador = inicioContador; contador < numero; contador++) {
                if (numero % contador == 0) {
                    ehPrimo = false;
                    break;
                }
            }
            if (ehPrimo) {
                System.out.println(numero);
            }
        }
    }
}

