public class ListaPrimos {

  public static void main(String[] args) {

    System.out.println(2);

    for (int i = 3; i <= 10000; i += 2) {
      boolean numeroComposto = false;
      int limite = (int) Math.sqrt(i);

      for (int j = 3; j <= limite; j += 2) {
        if (i % j == 0) {
          numeroComposto = true;
          break;
        }
      }
      if (!numeroComposto) {
        System.out.println(i);
      }
    }
  }
}
