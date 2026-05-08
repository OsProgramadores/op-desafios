public class MeuPrograma {
  public static void main(String[] args) {
    List<Integer> primos = new ArrayList<>();
    for (int i = 2; i <= 10000; i++) {
      primos.add(i);
    }

    for (int i = 2; i <= primos.size(); i++) {
      if (i * i > 10000) {
        break;
      }
      int finalI = i;
      primos.removeIf(p -> p % finalI == 0 && p != finalI);
    }

    primos.forEach(System.out::println);
  }
}
