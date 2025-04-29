public class PalindromosSimples {
    public static void main(String[] args) {
        for (int i = 1; i <= 20; i++) {
            if (ehPalindromo(i)) {
                System.out.print(i + " ");
            }
        }
    }

    public static boolean ehPalindromo(int numero) {
        String numeroStr = String.valueoOf(numero);
        StringBuilder sb = new StringBuilder(numeroStr).reverse();
        return numeroStr.equals(sb.toString());
    }
}
