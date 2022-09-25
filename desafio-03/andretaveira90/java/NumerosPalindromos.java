public class NumerosPalindromos {
    public static void main(String[] args) {
        int inicioIntervalo = 1;
        int fimIntervalo = 1551;

        for (int contador = inicioIntervalo; contador <= fimIntervalo; contador++) {
            if ((Integer.toString(contador)).equals(new StringBuilder(Integer.toString(contador)).reverse().toString())) {
                System.out.println(contador);
            }
        }
    }
}
