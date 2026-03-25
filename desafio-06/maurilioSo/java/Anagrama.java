import java.io.*;
import java.util.*;

public class Anagrama {

  public static Set<String> carregarPalavrasValidas(String arquivo) throws IOException {
    Set<String> palavrasValidas = new HashSet<>();
    BufferedReader reader = new BufferedReader(new FileReader(arquivo));
    String linha;
    while ((linha = reader.readLine()) != null) {
      linha = linha.trim().toUpperCase();
      if (linha.matches("[A-Z]+")) {
        palavrasValidas.add(linha);
      }
    }
    reader.close();
    return palavrasValidas;
  }

  public static void validarEntrada(String expressao) {
    if (!expressao.replaceAll(" ", "").matches("[A-Za-z]+")) {
      System.out.println("Erro: a expressão contém caracteres inválidos.");
      System.exit(1);
    }
  }

  public static Set<String> gerarAnagramas(String expressao, Set<String> palavrasValidas) {
    expressao = expressao.replaceAll(" ", "").toUpperCase();
    Set<String> resultados = new HashSet<>();
    List<String> listaLetras = new ArrayList<>(Arrays.asList(expressao.split("")));
    gerarCombinacoes(listaLetras, palavrasValidas, new ArrayList<>(), resultados);
    return resultados;
  }

  private static void gerarCombinacoes(
      List<String> letrasRestantes,
      Set<String> palavrasValidas,
      List<String> combinacaoAtual,
      Set<String> resultados) {
    if (letrasRestantes.isEmpty()) {
      List<String> combinacaoOrdenada = new ArrayList<>(combinacaoAtual);
      Collections.sort(combinacaoOrdenada);
      String anagrama = String.join(" ", combinacaoOrdenada);
      resultados.add(anagrama);
      return;
    }

    for (int i = 1; i <= letrasRestantes.size(); i++) {
      List<String> permutacoes = permutar(letrasRestantes, i);
      for (String perm : permutacoes) {
        if (palavrasValidas.contains(perm)) {
          List<String> novasLetras = new ArrayList<>(letrasRestantes);
          for (char c : perm.toCharArray()) {
            novasLetras.remove(String.valueOf(c));
          }
          List<String> novaCombinacao = new ArrayList<>(combinacaoAtual);
          novaCombinacao.add(perm);
          gerarCombinacoes(novasLetras, palavrasValidas, novaCombinacao, resultados);
        }
      }
    }
  }

  public static List<String> permutar(List<String> lista, int tam) {
    List<String> result = new ArrayList<>();
    permutarRecursivo(lista, 0, tam, result);
    return result;
  }

  private static void permutarRecursivo(
      List<String> lista, int index, int tam, List<String> result) {
    if (index == tam) {
      result.add(String.join("", lista.subList(0, tam)));
      return;
    }

    Set<String> permutacoesGeradas = new HashSet<>();
    for (int i = index; i < lista.size(); i++) {
      Collections.swap(lista, i, index);
      String perm = String.join("", lista.subList(0, tam));
      if (!permutacoesGeradas.contains(perm)) {
        permutacoesGeradas.add(perm);
        permutarRecursivo(lista, index + 1, tam, result);
      }
      Collections.swap(lista, i, index);
    }
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Digite a expressão (palavra ou frase): ");
    String expressao = scanner.nextLine();
    validarEntrada(expressao);
    Set<String> palavrasValidas = null;
    try {
      palavrasValidas = carregarPalavrasValidas("words.txt");
    } catch (IOException e) {
      System.out.println("Erro ao carregar o arquivo words.txt.");
      System.exit(1);
    }
    Set<String> anagramas = gerarAnagramas(expressao, palavrasValidas);
    System.out.println("\nAnagramas encontrados:");
    List<String> sortedAnagramas = new ArrayList<>(anagramas);
    Collections.sort(sortedAnagramas);
    for (String anagrama : sortedAnagramas) {
      System.out.println(anagrama);
    }
    scanner.close();
  }
}
