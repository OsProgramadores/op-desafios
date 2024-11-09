public class NumerosPalidromicos {

    public static void main(String[] args) {

        for (int i = 0; i <= 100000; ++i) {
            
            if (ehPalindromico(i)) {
                
                System.out.println(i);
            }
        }
    }

    public static boolean ehPalindromico(int num) {

        if (num < 0) {
            return false;
        } else {
            int numeroInvertido = 0;
            int numeroOriginal = num;
            while (num != 0) {
                int resto = num % 10;
                numeroInvertido = numeroInvertido * 10 + resto;
                num /= 10;
            }

            return numeroOriginal == numeroInvertido;
        }
    }
}