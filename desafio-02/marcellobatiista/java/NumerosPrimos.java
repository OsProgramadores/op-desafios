public class NumerosPrimos {
    public static void main(String[] args) {
        int quantidade = 10000;

        for (int numero = 2; numero <= quantidade; numero++) {
            int qt_divisores = 0;
            for (int div = 1; div <= quantidade; div++) {
                if (numero % div == 0) {
                    qt_divisores += 1;
                }
                if (qt_divisores > 2) {
                    break;
                }
             }
             if (qt_divisores == 2) {
                 System.out.printf("%d ", numero);
             }
        }
    }
}
