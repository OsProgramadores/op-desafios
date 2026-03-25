
public class Palindromos {

    private static String reverse(String numero) {
        byte[] numeroAsByteArray = numero.getBytes();

        byte[] resultado = new byte[numeroAsByteArray.length];

        for (int i = 0; i < numeroAsByteArray.length; i++) {
            resultado[i] = numeroAsByteArray[numeroAsByteArray.length - i - 1];
        }

        return new String(resultado);
    }

    private static boolean isPalindromo(String numero) {
        return numero.equals(reverse(numero));
    }

    public static void main(String[] args) {
        long start = System.currentTimeMillis();

        long numA = 1;
        long numB = 9999;

        for (long i = numA; i <= numB; i++) {
            System.out.print(isPalindromo(String.valueOf(i)) ? (i + "\n") : "");
        }

        System.out.println("Tempo total (milliseconds): " + (System.currentTimeMillis() - start));
    }
}
