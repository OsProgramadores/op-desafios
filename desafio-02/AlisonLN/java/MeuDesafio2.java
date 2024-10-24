public class desafio2 {

    public static void main(String[] args) {

        int max = 10000;

        for (int i = 1; i <= max; i++) {
            int quntDivis = 0;
            for (int j = 1; j <= i; j++){
                if (i % j == 0) {
                    quntDivis ++;
                }
            }
            if (quntDivis == 2) {
                System.out.print(i +" ");
            }
        }
    }
}