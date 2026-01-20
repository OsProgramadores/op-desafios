import java.io.*;
import java.math.BigInteger;
import java.util.Scanner;

public class Potencia {
    public static void main(String[] args) throws IOException{
      if (args.length != 1) {
          System.out.println(
                  "Nenhum caminho foi fornecido,  execute o programa usando 'java Potencia"
                          + " <caminho-absoluto>'");
          return;
      }

      File caminho = new File(args[0]);
      if (!caminho.exists()) {
          System.out.println("Arquivo não encontrado.");
          return;
      }
      try (Scanner sc = new Scanner(caminho)) {
          while (sc.hasNext()) {
              String linha = sc.next().trim();
              if (linha.isEmpty()) {
                  continue;
              }
              BigInteger numero  = new BigInteger(linha);
              boolean ehPotencia =
                      numero.signum() > 0 && numero.and(numero.subtract(BigInteger.ONE)).equals(BigInteger.ZERO);
              if (ehPotencia) {
                  int expoente = numero.bitLength() - 1;
                  System.out.println(numero + " " + ehPotencia + " " + expoente);
              } else {
                  System.out.println(numero + " " + ehPotencia);
              }
          }
      }
  }
}
