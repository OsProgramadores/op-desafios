public class DesafioNumPrimo {
    public static void main(String[] args) {
        int quantMax = 10000;
        for (int i = 2; i <= quantMax; i++) {
            int contador = 2;
            boolean isPrimo = true;
            while (isPrimo && contador < i) {
                if (i % contador == 0) {
                    isPrimo = false;
                } else {
                    contador++;
                }
            }
            if (isPrimo) {
                System.out.println(i);
            }
        }
    }
}