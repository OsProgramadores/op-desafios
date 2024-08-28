import java.util.ArrayList;

public class Desafio03 {
  private static boolean reverteNumero(int numeroInicial) {
    String numeroInvertido = "";

    // converte em array de String
    String numeroInicialString = Integer.toString(numeroInicial);

    // inverte as posições dos números
    for (int x = 0; x < numeroInicialString.length(); x++) {
      numeroInvertido = numeroInicialString.charAt(x) + numeroInvertido;
    }

    // se o numeroInvertido for igual ao array de String do NumeroInicial, então adiciona no
    // Arraylist Palindromico
    if (numeroInvertido.equals(numeroInicialString)) {
      return true;
    }

    return false;
  }

  private static ArrayList<Integer> verificaPalindromicos(int numeroInicial, int numeroFinal) {
    ArrayList<Integer> palindromico =
        new ArrayList<Integer>(); // Array para armazenar os números palindromicos

    while (numeroInicial <= numeroFinal) {
      if (numeroInicial < 10) { // por regra, de 1 a 9 são palindromicos
        palindromico.add(numeroInicial);
        numeroInicial++;
        continue;
      }

      if (reverteNumero(numeroInicial)) {
        palindromico.add(numeroInicial);
      }

      numeroInicial++;
    }

    return palindromico;
  }

  public static void main(String[] args) {
    int numeroInicial = 1000;
    int numeroFinal = 2000;

    System.out.println(
        "Números Palíndromicos: " + verificaPalindromicos(numeroInicial, numeroFinal));
    ;
  }
}
