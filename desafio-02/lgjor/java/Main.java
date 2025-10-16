public class Main{

    enum LIMITS{
        LOWER(2),
        UPPER(10000);
        int number;

        private LIMITS(int number){
            this.number = number;
        }
    }

    private static boolean isPrimeNumber(int number){
        for (int i = LIMITS.LOWER.number; i * i <= number; i++) {
            if (number%i==0){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        for (int i = LIMITS.LOWER.number; i <= LIMITS.UPPER.number; i++) {
            if (isPrimeNumber(i)){
                System.out.println(i);
            }
        }
    }
}