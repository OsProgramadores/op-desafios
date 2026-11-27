package desafio6;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MeuPrograma {
  public static void main(String[] args) {

    if (args.length == 0) {
      System.out.println("ERRO: O programa precisa de pelo menos um parâmetro.");
      System.exit(1);
    }

    StringBuilder palavra = new StringBuilder();
    for (String p : args) {
      palavra.append(p);
    }
    String palavraString = palavra.toString().toUpperCase().replace(" ", "");

    if (!palavraString.matches("[A-Z]+")) {
      System.out.println("ERRO: Caracteres inválidos.");
      System.exit(1);
    }

    int[] freqPalavra = gerarFrequencia(palavraString);
    List<PalavraFreq> dicionarioFiltrado = gerarDicionario("words.txt", freqPalavra);
    procurarAnagramas(
        freqPalavra, dicionarioFiltrado, 0, new ArrayList<>(), palavraString.length());
  }

  private static class PalavraFreq {
    final String palavra;
    final int[] freq;

    PalavraFreq(String palavra, int[] freq) {
      this.palavra = palavra;
      this.freq = freq;
    }
  }

  public static int[] gerarFrequencia(String palavra) {
    char[] palavraArray = palavra.toCharArray();
    int[] freqPalavra = new int[26];

    for (char c : palavraArray) {
      if (c >= 'A' && c <= 'Z') {
        freqPalavra[c - 'A']++;
      }
    }

    return freqPalavra;
  }

  public static List<PalavraFreq> gerarDicionario(String caminho, int[] freqPalavra) {
    List<PalavraFreq> dicionario = new ArrayList<>();

    try (BufferedReader br = new BufferedReader(new FileReader(caminho))) {
      String linha = br.readLine();

      while (linha != null) {
        if (!linha.isEmpty()) {
          int[] freqLinha = gerarFrequencia(linha);
          boolean cabeNoEstoque = cabeNoEstoque(freqPalavra, freqLinha);
          if (cabeNoEstoque) dicionario.add(new PalavraFreq(linha, freqLinha));
        }

        linha = br.readLine();
      }

    } catch (IOException e) {
      System.out.println("ERRO: O arquivo não existe ou seu caminho está errado");
      System.exit(1);
    }

    return dicionario;
  }

  public static boolean cabeNoEstoque(int[] freqPalavra, int[] freqLinha) {
    for (int i = 0; i < 26; i++) {
      if (freqPalavra[i] < freqLinha[i]) {
        return false;
      }
    }

    return true;
  }

  public static void procurarAnagramas(
      int[] freqPalavra,
      List<PalavraFreq> dicionario,
      int comeco,
      List<String> atual,
      int letrasRestantes) {
    if (letrasRestantes == 0) {
      List<String> resultado = new ArrayList<>(atual);
      Collections.sort(resultado);
      System.out.println(String.join(" ", resultado));
      return;
    }

    for (int i = comeco; i < dicionario.size(); i++) {
      PalavraFreq item = dicionario.get(i);
      String palavra = item.palavra;
      int[] freqP = item.freq;

      if (cabeNoEstoque(freqPalavra, freqP) && !atual.contains(palavra)) {
        for (int j = 0; j < 26; j++) {
          freqPalavra[j] -= freqP[j];
        }
        atual.add(palavra);

        procurarAnagramas(freqPalavra, dicionario, i, atual, letrasRestantes - palavra.length());

        atual.remove(atual.size() - 1);
        for (int j = 0; j < 26; j++) freqPalavra[j] += freqP[j];
      }
    }
  }
}
