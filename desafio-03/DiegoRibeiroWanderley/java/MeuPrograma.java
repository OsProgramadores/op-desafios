public class MeuPrograma {
  public static void main(String[] args) {

    int numeroComeco = Integer.parseInt(args[0]);
    int numeroFim = Integer.parseInt(args[1]);

    for (int i = numeroComeco; i <= numeroFim; i++) {

      String ns = String.valueOf(i);
      StringBuilder sn = new StringBuilder();

      for (int j = ns.length() - 1; j >= 0; j--) {
        sn.append(ns.charAt(j));
      }

      if (ns.contentEquals(sn)) {
        System.out.println(ns);
      }
    }
  }
}
