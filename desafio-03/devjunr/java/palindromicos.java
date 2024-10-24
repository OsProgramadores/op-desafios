public class palindromicos {
  public static void main(String[] args) {
    try {
      int valorInicial = Integer.parseInt(args[0]);
      int valorFinal = Integer.parseInt(args[1]);
      if (valorInicial > 0 & valorFinal > 0) {
        if (valorFinal < valorInicial) {
          System.out.println("O valor final não pode ser menor que o valor inicial");
        } else {
          System.out.println(
              "_".repeat(15)
                  + "\nValor Inicial: "
                  + valorInicial
                  + "\nValor Final: "
                  + valorFinal
                  + "\n"
                  + "_".repeat(15));
          tratamentoDosValores(valorInicial, valorFinal);
        }
      } else if (valorInicial <= 0 || valorFinal <= 0) {
        System.out.println("Os dois valores precisam ser inteiros positivos");
      }
    } catch (NumberFormatException e) {
      System.out.println("Apenas números inteiros positivos são aceitos");
    } catch (ArrayIndexOutOfBoundsException e) {
      System.out.println("É necessário pelo menos dois valores inteiros positivos como argumento");
    }
  }

  public static void tratamentoDosValores(int valorInicial, int valorFinal) {
    for (int i = valorInicial; i <= valorFinal; i++) {
      String numero = Integer.toString(i);
      String reversed = new StringBuilder(numero).reverse().toString();
      if (reversed.equals(numero)) {
        System.out.println(numero);
      }
    }
  }
}
