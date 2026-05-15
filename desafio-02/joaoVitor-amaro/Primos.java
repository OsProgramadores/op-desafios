public class Primos {
    public static boolean isPrimo(int num) {
        if(num < 2) {
            return false;
        }
        for(int i = 2; i < num; i++) {
            if(num % i == 0) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        int limit = 10000;
        for (int i = 1; i < limit; i++) {
            if(Primos.isPrimo(i)) {
                System.out.println(i);
            }
        }
    }
}
