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
    String expressao = String.join(" ", args).toUpperCase();
    String entrada = expressao.replaceAll(" ", "");
    if (!entrada.matches("[A-Z]+")) {
      System.out.println("Expressão inválida! Apenas letras são permitidas.");
      return;
    }

    String caminho = System.getenv("CAMINHO");
    System.out.println(caminho);
    if (caminho == null) {
      System.out.println("O caminho do arquivo não foi definido");
      return;
    }

    ArrayList<String> palavrasValidas = new ArrayList<>();
    Map<String, Map<Character, Integer>> mapAnagramas = new HashMap<>();
    try (Scanner arquivoScanner = new Scanner(new File(caminho))) {
      while (arquivoScanner.hasNextLine()) {
        String palavra = arquivoScanner.nextLine().trim().toUpperCase();
        if (!palavra.isEmpty()) {
          palavrasValidas.add(palavra);
        }
        mapAnagramas.put(palavra, contarLetras(palavra));
      }
    } catch (FileNotFoundException e) {
      System.out.println("Arquivo words.txt não encontrado!");
      return;
    }

    if (palavrasValidas.isEmpty()) {
      System.out.println("Erro: Nenhuma palavra válida encontrada no arquivo.");
      return;
    }
    Map<Character, Integer> letrasExpressao = contarLetras(entrada);
    List<String> palavrasCabem = new ArrayList<>();
    for (String palavra : palavrasValidas) {
      if (cabe(letrasExpressao, contarLetras(palavra))) {
        palavrasCabem.add(palavra);
      }
    }
    TreeSet<String> anagramas = new TreeSet<>();
    permutar(new TreeSet<>(), letrasExpressao, palavrasCabem, mapAnagramas, anagramas);
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
      TreeSet<String> anagramas) {
    if (letrasRestantes.isEmpty()) {
      anagramas.add(String.join(" ", caminhoAtual));
      return;
    }
    for (String palavra : palavrasCabem) {
      Map<Character, Integer> letrasPalavra = mapAnagramas.get(palavra);
      if (cabe(letrasRestantes, letrasPalavra)) {
        caminhoAtual.add(palavra);
        Map<Character, Integer> novasLetras = verificar(letrasRestantes, letrasPalavra);
        permutar(caminhoAtual, novasLetras, palavrasCabem, mapAnagramas, anagramas);
        caminhoAtual.remove(palavra);
      }
    }
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
      letras.put(c, letras.getOrDefault(c, 0) + 1);
    }
    return letras;
  }
}
