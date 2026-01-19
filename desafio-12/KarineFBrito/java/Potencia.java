import java.io.*;
import java.math.BigInteger;
import java.util.Scanner;

public class Potencia {
  public static void main(String[] args) {

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
        String linha = sc.next();
        if (linha.trim().isEmpty()) {
          continue;
        }
        BigInteger n = new BigInteger(linha.trim());
        boolean ehPotencia =
            n.signum() > 0 && n.and(n.subtract(BigInteger.ONE)).equals(BigInteger.ZERO);
        if (ehPotencia) {
          int expoente = n.bitLength() - 1;
          System.out.println(n + " " + ehPotencia + " " + expoente);
        } else {
          System.out.println(n + " " + ehPotencia);
        }
      }
    } catch (IOException e) {
      System.err.println("Erro ao ler o arquivo: " + e.getMessage());
    }
  }
}
