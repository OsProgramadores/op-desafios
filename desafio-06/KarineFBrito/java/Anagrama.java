import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeSet;

public class Anagrama {

  public static void main(String[] args) {
    if (args.length == 0) {
      System.out.println("Nenhuma expressão foi fornecida.");
      return;
    }
    String expressao = String.join("", args).toUpperCase();
    if (!expressao.matches("[A-Z]+")) {
      System.out.println("Expressão inválida! Apenas letras são permitidas.");
      return;
    }

    String caminho = System.getenv("CAMINHO");
    System.out.println(caminho);
    if (caminho == null) {
      System.out.println("O caminho do arquivo não foi definido");
      return;
    }

    Map<String, Map<Character, Integer>> mapAnagramas = new HashMap<>();
    try (Scanner arquivoScanner = new Scanner(new File(caminho))) {
      while (arquivoScanner.hasNextLine()) {
        String palavra = arquivoScanner.nextLine().trim().toUpperCase();
        if (!palavra.isEmpty()) {
          mapAnagramas.put(palavra, contarLetras(palavra));
        }
      }
    } catch (FileNotFoundException e) {
      System.out.println("Arquivo words.txt não encontrado!");
      return;
    }

    if (mapAnagramas.isEmpty()) {
      System.out.println("Erro: Nenhuma palavra válida encontrada no arquivo.");
      return;
    }
    Map<Character, Integer> letrasExpressao = contarLetras(expressao);
    List<String> palavrasCabem = new ArrayList<>();
    for (Map.Entry<String, Map<Character, Integer>> palavraLetras : mapAnagramas.entrySet()) {
      if (cabe(letrasExpressao, palavraLetras.getValue())) {
        palavrasCabem.add(palavraLetras.getKey());
      }
    }
    TreeSet<String> anagramas = new TreeSet<>();
    permutar(new TreeSet<>(), letrasExpressao, palavrasCabem, mapAnagramas, anagramas, expressao);
    if (anagramas.isEmpty()) {
      System.out.println("Nenhum anagrama válido encontrado.");
    } else {
      for (String anagrama : anagramas) {
        System.out.println(anagrama);
      }
    }
  }

  private static void permutar(
      TreeSet<String> caminhoAtual,
      Map<Character, Integer> letrasRestantes,
      List<String> palavrasCabem,
      Map<String, Map<Character, Integer>> mapAnagramas,
      TreeSet<String> anagramas,
      String expressao) {
    if (letrasRestantes.isEmpty()) {
      String p = String.join("", caminhoAtual);
      if (verificacao(p, expressao)) {
        anagramas.add(String.join(" ", caminhoAtual));
        return;
      }
    }
    for (String palavra : palavrasCabem) {
      Map<Character, Integer> letrasPalavra = mapAnagramas.get(palavra);
      if (cabe(letrasRestantes, letrasPalavra)) {
        TreeSet<String> caminhoNovo = new TreeSet<>(caminhoAtual);
        caminhoNovo.add(palavra);
        Map<Character, Integer> novasLetras = verificar(letrasRestantes, letrasPalavra);
        permutar(caminhoNovo, novasLetras, palavrasCabem, mapAnagramas, anagramas, expressao);
      }
    }
  }

  private static boolean verificacao(String palavra, String expressao) {
    Map<Character, Integer> contaExpressao = contarLetras(expressao);
    Map<Character, Integer> contaPalavra = contarLetras(palavra);
    return contaExpressao.equals(contaPalavra);
  }

  private static Map<Character, Integer> verificar(
      Map<Character, Integer> expressao, Map<Character, Integer> palavra) {
    Map<Character, Integer> resultado = new HashMap<>(expressao);
    for (Map.Entry<Character, Integer> entry : palavra.entrySet()) {
      char letra = entry.getKey();
      int qtd = resultado.get(letra) - entry.getValue();
      if (qtd == 0) {
        resultado.remove(letra);
      } else {
        resultado.put(letra, qtd);
      }
    }
    return resultado;
  }

  private static boolean cabe(Map<Character, Integer> expressao, Map<Character, Integer> palavra) {
    for (Map.Entry<Character, Integer> entry : palavra.entrySet()) {
      char letra = entry.getKey();
      int qtdP = entry.getValue();
      int qtdE = expressao.getOrDefault(letra, 0);
      if (qtdP > qtdE) {
        return false;
      }
    }
    return true;
  }

  private static Map<Character, Integer> contarLetras(String expressao) {
    Map<Character, Integer> letras = new HashMap<>();
    for (char c : expressao.toCharArray()) {
      letras.compute(c, (chave, valorAtual) -> (valorAtual == null ? 1 : valorAtual + 1));
    }
    return letras;
  }
}
