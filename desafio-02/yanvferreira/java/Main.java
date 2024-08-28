public class Main {
  public static void main(String[] args) {

    int tamanhoDaLista = 30;
    int inicioLista = 1;
    boolean primos;

    for (int inicio = inicioLista; inicio <= tamanhoDaLista; inicio++) {
      if (inicio == 1) {
        continue;
      }
      if (inicio == 2 || inicio == 3 || inicio == 5) {
        System.out.println(inicio);
        continue;
      }

      // numeros 2, 3 e 5 são números primos conhecidos e serão usados para calcular a lista sem
      // precisar percorrer todos os números

      if (inicio % 2 == 0 || inicio % 3 == 0 || inicio % 5 == 0) {
        primos = false;
        continue;
      } else {
        primos = true;
      }

      if (primos) {
        System.out.println(inicio);
      }
    }
  }
}
