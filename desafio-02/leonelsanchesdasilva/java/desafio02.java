class Desafio02 {
  public static void main(String[] args) {
    for (int i = 1; i <= 10000; i++) {
      Boolean primo = true;
      for (int j = 2; j <= Math.floor(Math.sqrt(i)); j++) {
        if (i % j == 0) {
          primo = false;
          break;
        }
      }

      if (primo) {
        System.out.println(i);
      }
    }
  }
}
