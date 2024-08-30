import java.util.Arrays;

public class Main {
  public static void main(String[] args) {

    // implementando o código seguindo a teroria do Crivo de Eratóstenes
    int n = 50;

    // iniciando um array setando todos os valores como true
    Boolean[] ehPrimo = new Boolean[n + 1];
    Arrays.fill(ehPrimo, true);

    // número 0 e 1 não são número primos
    ehPrimo[0] = false;
    ehPrimo[1] = false;

    for (int i = 2; i * i <= n; i++) {
      if (ehPrimo[i]) {
        // se o número for primo, seta todos os múltiplos dele como falso
        for (int j = i * i; j <= n; j += i) {
          ehPrimo[j] = false;
        }
      }
    }

    System.out.println("Números primos até: " + n);

    for (int i = 2; i <= n; i++) {
      if (ehPrimo[i]) {
        System.out.println(i + " ");
      }
    }
  }
}
