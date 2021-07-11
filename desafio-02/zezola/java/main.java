public class NumerosPrimos {
    public static void main(String[] args) {

        for (int i = 2; i < 10000; i++) {
            if (primeChecker(i)) {
                System.out.println(i);
            }
        }

    }

    public static boolean primeChecker(int num) {
        for (int i = 2; i < num; i++){
            if (num % i == 0) {
                return false;
            }

        }
        return true;
    }
}