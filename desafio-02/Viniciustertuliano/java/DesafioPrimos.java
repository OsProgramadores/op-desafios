public class DesafioPrimos {
    public static void main(String[] args) {
        for (int i = 2; i <= 10000; i++) {
            boolean primo = true;
            for (int a = 2; a < i; a++) {
                if (i % a == 0) primo = false;
            }
            if (primo) System.out.println(i);
        }
    }
}
