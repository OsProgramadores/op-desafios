public class MeuPrograma {
  public static void main(String[] args) {
    for (int i = 0; i <= 10000; i++) {
      int cont = 0;
      for (int j = 1; j <= i; j++) {

        if (i % j == 0) {
          cont += 1;
        }
      }

      if (cont == 2) {
        System.out.println(i);
      }
    }
  }
}
