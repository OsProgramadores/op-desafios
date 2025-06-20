import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;

public class Fracoes {
  public static void main(String[] args) {
    if (args.length != 1) {
      System.out.println(
          "Nenhum caminho foi fornecido,  execute o programa usando 'java Fracoes"
              + " <caminho-absoluto>'");
      return;
    }

    File caminho = new File(args[0]);
    if (!caminho.exists()) {
      System.out.println("Arquivo não encontrado.");
      return;
    }
    try (RandomAccessFile aq = new RandomAccessFile(caminho, "r")) {
      String linha;
      while ((linha = aq.readLine()) != null) {
        if (linha.isEmpty()) {
          continue;
        }
        contador(linha);
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  public static int mdc(int a, int b) {
    if (b == 0) {
      return a;
    }
    return mdc(b, a % b);
  }

  public static void contador(String linha) {
    String[] partes = linha.split("/");
    int numerador;
    int denominador;
    if (partes.length == 1) {
      numerador = Integer.parseInt(partes[0]);
      denominador = 1;
    } else {
      numerador = Integer.parseInt(partes[0]);
      denominador = Integer.parseInt(partes[1]);
    }
    if (denominador == 0) {
      System.out.println("ERR");
      return;
    }
    int divisor = mdc(numerador, denominador);
    numerador /= divisor;
    denominador /= divisor;
    if (denominador == 1) {
      System.out.println(numerador);
    } else if (numerador >= denominador) {
      int inteiro = numerador / denominador;
      int resto = numerador % denominador;
      if (resto == 0) {
        System.out.println(inteiro);
      } else {
        System.out.println(inteiro + " " + resto + "/" + denominador);
      }
    } else {
      System.out.println(numerador + "/" + denominador);
    }
  }
}
