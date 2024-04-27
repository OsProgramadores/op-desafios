
public class NumerosPalidromicos {
  public static void main(String[] args) {
    for (int i = 1; i <= 1000; i++) {
      verificarPalidromico(i);
    }
  }
  // Verificar se o numero é palidromico
  public static void verificarPalidromico(int numero) {
    int numeroInvertido = 0;
    int resto;
    int numeroOriginal = numero;
    while (numero != 0) {
      resto = numero % 10;
      numeroInvertido = numeroInvertido * 10 + resto;
      numero /= 10;
    }
    if (numeroOriginal == numeroInvertido) {
      System.out.println(numeroInvertido);
    }
  }
}
