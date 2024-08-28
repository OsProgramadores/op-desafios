public class Main {
  public static void main(String[] args) {

    int tamanhoDaLista = 10000;
    int inicioLista = 1;
    boolean primos;

    for (int inicio = inicioLista; inicio <= tamanhoDaLista; inicio++) {
      if (inicio == 1) {
        continue;
      }
      if (inicio == 2) {
        System.out.println(inicio);
        continue;
      }

      primos = true;
      for (int divisor = 2; divisor < inicio; divisor++) {
        if (inicio % divisor == 0) {
          primos = false;
          break;
        }
      }

      if (primos) {
        System.out.println(inicio);
      }
    }
  }
}
