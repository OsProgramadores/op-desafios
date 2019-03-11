public class Primos {

    public static void main(String[] args) {
        
        for (int i = 2; i < 1000; i++) {
            boolean primo = true;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    primo = false;
                    break;
                }
            }
            if (primo)
                System.out.println(i);
        }
    }
}