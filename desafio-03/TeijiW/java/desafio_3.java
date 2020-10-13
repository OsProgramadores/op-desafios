public class desafio_3 {
    public static void main(String[] args) {
        var start = Integer.parseInt(args[0]);
        var end = Integer.parseInt(args[1]);
        for (Integer i = start; i <= end; i++) {
            var original = i.toString();
            var reverse = new StringBuilder(original).reverse().toString();
            if (reverse.equals(original)) {
                System.out.println(i);
            }
        }
    }
}
