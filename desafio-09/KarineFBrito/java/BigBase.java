import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.math.BigInteger;

public class BigBase {
  static final String DIGITOS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
  static final int BASE_MIN = 2;
  static final int BASE_MAX = 62;
  static final String LIMITE =
      "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"; // determino o Limite de acordo com o que foi pedido

  public static void main(String[] args) {
    if (args.length != 1) {
      System.out.println(
          "Nenhum caminho foi fornecido,  execute o programa usando 'java BigBase"
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
      BigInteger limiteMax = converterBase10(LIMITE, 62);
      while ((linha = aq.readLine()) != null) {
        String[] partes = linha.split(" ");
        if (partes.length != 3) {
          System.out.println("???");
          continue;
        }
        int baseEntrada = Integer.parseInt(partes[0]);
        int baseSaida = Integer.parseInt(partes[1]);
        String numero = partes[2];
        if (negativo(numero)
            || baseEntrada < BASE_MIN
            || baseEntrada > BASE_MAX
            || baseSaida < BASE_MIN
            || baseSaida > BASE_MAX) {
          System.out.println("???");
          continue;
        }
        BigInteger decimal = converterBase10(numero, baseEntrada);
        if (decimal == null || decimal.compareTo(limiteMax) > 0) {
          System.out.println("???");
          continue;
        }
        String converterBaseSaida = paraBase(decimal, baseSaida);
        System.out.println(converterBaseSaida);
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  static boolean negativo(String numero) {
    return numero.startsWith("-");
  }

  public static BigInteger converterBase10(String numero, int baseEntrada) {
    BigInteger resultado = BigInteger.ZERO;
    BigInteger base = BigInteger.valueOf(baseEntrada);
    for (int i = 0; i < numero.length(); i++) {
      char c = numero.charAt(i);
      int valor = valorDigito(c);
      if (valor < 0 || valor >= baseEntrada) {
        return null;
      }
      resultado = resultado.multiply(base).add(BigInteger.valueOf(valor));
    }
    return resultado;
  }

  public static String paraBase(BigInteger numero, int base) {
    if (numero.equals(BigInteger.ZERO)) {
      return "0";
    }
    StringBuilder resultado = new StringBuilder();
    BigInteger baseBig = BigInteger.valueOf(base);
    while (numero.compareTo(BigInteger.ZERO) > 0) {
      BigInteger[] divmod = numero.divideAndRemainder(baseBig);
      int resto = divmod[1].intValue();
      resultado.append(DIGITOS.charAt(resto));
      numero = divmod[0];
    }
    return resultado.reverse().toString();
  }

  public static int valorDigito(char c) {
    if (c >= '0' && c <= '9') {
      return c - '0';
    }
    if (c >= 'A' && c <= 'Z') {
      return c - 'A' + 10;
    }
    if (c >= 'a' && c <= 'z') {
      return c - 'a' + 36;
    }
    return -1;
  }
}
