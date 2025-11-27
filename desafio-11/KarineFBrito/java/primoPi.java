import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.BufferedReader;
import java.io.FileReader;

public class primoPi {

  private static final int MAX_PRIME = 9973;
  private static Set<Integer> conjuntoPrimos;
  private static String piDecimais = "";

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
    try (BufferedReader aq = new BufferedReader(new FileReader(caminho))) {
      String linha;
      while ((linha = aq.readLine()) != null) {
        if (linha.isEmpty()) {
          continue;
        }
        processarLinha(linha);
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
    preCalcularPrimos(MAX_PRIME);

    String sequenciaMaisLonga = encontrarSequenciaMaisLonga();

    System.out.println(sequenciaMaisLonga);
  }

  private static void processarLinha(String linha) {
    Pattern p = Pattern.compile("\\d+");
    Matcher m = p.matcher(linha);

    while (m.find()) {
      piDecimais += m.group();
    }
  }

  private static void preCalcularPrimos(int limite) { // metodo do Eratóstenes
    conjuntoPrimos = new HashSet<>();
    if (limite < 2) {
      return;
    }

    boolean[] ehComposto = new boolean[limite + 1];

    for (int p = 2; p * p <= limite; p++) {
      if (!ehComposto[p]) {
        for (int i = p * p; i <= limite; i += p) {
          ehComposto[i] = true;
        }
      }
    }

    for (int p = 2; p <= limite; p++) {
      if (!ehComposto[p]) {
        conjuntoPrimos.add(p);
      }
    }
  }

  private static boolean ehPrimo(String s) {
    if (s.isEmpty()){
      return false;
    }
    
    try {
      int num = Integer.parseInt(s);
      if (num > MAX_PRIME) {
        return false;
      }
      return conjuntoPrimos.contains(num);
    } catch (NumberFormatException e) {
      return false;
    }
  }

  private static String encontrarSequenciaMaisLonga() {
    int N = piDecimais.length();
    if (N == 0){
      return "";
    }

    int[] comprimentoMax = new int[N + 1];
    int[] indiceAnterior = new int[N + 1];
    Arrays.fill(indiceAnterior, -1);

    int maiorComprimento = 0;
    int fimDaSequencia = 0;

    for (int i = 1; i <= N; i++) {
      for (int j = Math.max(0, i - 4); j < i; j++) {
        String sub = piDecimais.substring(j, i);

        if (ehPrimo(sub)) {
          int novoComprimento = comprimentoMax[j] + (i - j);

          if (novoComprimento > comprimentoMax[i]) {
                comprimentoMax[i] = novoComprimento;
                indiceAnterior[i] = j;
          }

            if (comprimentoMax[i] > maiorComprimento) {
                maiorComprimento = comprimentoMax[i];
                fimDaSequencia = i;
          }
        }
      }
    }

    return reconstruirSequencia(indiceAnterior, fimDaSequencia);
  }

  private static String reconstruirSequencia(int[] indiceAnterior, int fimDaSequencia) {
    if (fimDaSequencia == 0){
       return "";
    }
    StringBuilder sequenciaCompleta = new StringBuilder();
    int atual = fimDaSequencia;

    while (atual > 0 && indiceAnterior[atual] != -1) {
      int inicio = indiceAnterior[atual];
      int fim = atual;

      String primo = piDecimais.substring(inicio, fim);

      sequenciaCompleta.insert(0, primo);

      atual = inicio;
    }

    return sequenciaCompleta.toString();
  }
}