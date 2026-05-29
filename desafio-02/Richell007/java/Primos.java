public class Primos {
 
    public static void main(String[] args) {
        boolean[] ehPrimo = new boolean[10001];
 
        for (int i = 2; i <= 10000; i++) {
            ehPrimo[i] = true;
        }
 
        for (int i = 2; i * i <= 10000; i++) {
            if (ehPrimo[i]) {
                for (int j = i * i; j <= 10000; j += i) {
                    ehPrimo[j] = false;
                }
            }
        }
 
        for (int i = 2; i <= 10000; i++) {
            if (ehPrimo[i]) {
                System.out.println(i);
            }
        }
    }
}
 
