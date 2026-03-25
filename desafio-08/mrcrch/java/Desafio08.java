import java.util.Scanner;

public class Desafio08 {

    /**
     * Calcula o MDC (Maior Divisor Comum) entre os parâmetros {@code a} e {@code b}
     *
     * @see https://en.wikipedia.org/wiki/Euclidean_algorithm
     * @param a
     * @param b
     * @return Valor do MDC
     */
    private static final int mdc(final int a, final int b) {

        if (b == 0) {
            return a;
        }

        return mdc(b, a % b);
    }

    private static class Fracao {

        private final int numerador;
        private final int denominador;

        public Fracao(final int numerador, final int denominador) {
            this.numerador = numerador;
            this.denominador = denominador;
        }

        public Fracao simplificar() {
            final int mdc = mdc(numerador, denominador);
            return new Fracao(numerador / mdc, denominador / mdc);
        }

        @Override
        public String toString() {

            if (denominador == 0) {
                return "ERR";
            }

            if (numerador < denominador) {
                return numerador + "/" + denominador;
            }

            final int resto = numerador % denominador;
            final int novoNumerador = numerador / denominador;

            if (resto == 0) {
                return String.valueOf(novoNumerador);
            }

            return novoNumerador + " " + resto + "/" + denominador;

        }

    }

    public static void main(final String[] args) throws Exception {

        try (Scanner scanner = new Scanner(System.in)) {

            while (scanner.hasNextLine()) {

                final String line = scanner.nextLine();
                final String[] splitted = line.split("/");

                final int numerador = Integer.parseInt(splitted[0]);
                final int denominador = (splitted.length == 2) ? Integer.parseInt(splitted[1]) : 1;

                System.out.println(new Fracao(numerador, denominador).simplificar());

            }

        }

    }

}
