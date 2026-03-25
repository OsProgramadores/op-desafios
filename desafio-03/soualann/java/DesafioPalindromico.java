public class DesafioPalindromico {
  public static void main(String[] args) {
    int ninicial = 1;
    int nfinal = 2000;

    VerificarPalindromico(ninicial, nfinal);
  }

  private static void VerificarPalindromico(int numberinicial, int b) {
    for (int i = numberinicial; i <= b; i++) {
      if ((Integer.toString(i))
          .equals(new StringBuilder(Integer.toString(i)).reverse().toString())) {
        System.out.println(i);
      }
    }
  }
}
