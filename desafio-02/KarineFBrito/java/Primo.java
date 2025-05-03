public class Primo {

    public static void main(String[] args) {
        for (int num = 2; num <= 10000; num++) {
            boolean ehPrimo = true;
            for (int i = 2; i < num; i++) {
                if (num % i == 0) {
                    ehPrimo = false;
                    break;
                }
            }
            if (ehPrimo) {
                System.out.println(num);
            }
        }
    }
}
