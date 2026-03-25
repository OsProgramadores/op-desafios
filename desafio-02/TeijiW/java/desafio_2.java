public class desafio_2 {
    public static void main(String[] args) {
        for (var i = 1; i < 10000; i++) {
            var is_prime = true;
            for (var j = 2; j < i; j++) {
                if (i % j == 0 && i != j) {
                    is_prime = false;
                    break;
                }
            }
            if (is_prime)
                System.out.println(i);
        }
    }
}