import java.util.Arrays;

public class MeuPrograma {
  public static void main(String[] args) {
    boolean[] primos = new boolean[10000 + 1];
    Arrays.fill(primos, true);

    for (int i = 2; i * i <= 10000; i++) {
      if (primos[i]) {
        for (int j = i * i; j <= 10000; j += i) {
          primos[j] = false;
        }
      }
    }

    for (int i = 2; i <= 10000; i++) {
      if (primos[i]) {
        System.out.println(i);
      }
    }
  }
}
