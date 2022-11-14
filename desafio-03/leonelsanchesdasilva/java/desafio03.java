class Desafio03 {
  public static void main(String[] args) {
    for (int i = 1; i <= 3010; i++) {
      String numero = String.valueOf(i);
      String inverso = new StringBuilder(numero).reverse().toString();
      if (numero.equalsIgnoreCase(inverso)) {
        System.out.println(i);
      }
    }
  }
}
