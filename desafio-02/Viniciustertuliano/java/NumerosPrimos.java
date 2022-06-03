public class NumerosPrimos {
    public static void main(String[] args) {
        for (int i = 2; i <= 10000; i++) {
            if(primo(i)){
                System.out.println(i);
            }
        }
    }

    private static boolean primo(int numero) {
        for (int a = 2; a < numero; a++) {
            if(numero % a == 0){
                return false;
            }
        }
        return true;
    }
}

