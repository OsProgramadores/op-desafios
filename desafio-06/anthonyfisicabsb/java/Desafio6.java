import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Optional;
import java.util.Set;
import java.util.TreeSet;
import java.util.stream.Collectors;

public class Desafio6 {

  private static final PalavrasValidas PALAVRAS_VALIDAS = new PalavrasValidas(
      System.getenv("CAMINHO_PALAVRAS_VALIDAS"));

  public static void main(final String[] listaPalavras) {
    if (listaPalavras.length == 0) {
      System.out.println(
          "Defina uma lista de palavras para se obter o anagrama: java Desafio6 [lista-palavras]");
      System.exit(1);
    }

    final String stringFormatada = recuperarStringFormatada(listaPalavras);
    final Map<Character, Integer> mapaInicialDeCaracteres =
        PALAVRAS_VALIDAS.montarMapaCaracteres(stringFormatada);

    PALAVRAS_VALIDAS.filtrarPalavrasValidas(mapaInicialDeCaracteres);

    executarRecursao(mapaInicialDeCaracteres, new HashSet<>(),
        PALAVRAS_VALIDAS.palavrasParaQtdCaracteres);
  }

  private static void executarRecursao(final Map<Character, Integer> mapaCaracteres,
      final Set<String> conjuntoPalavras,
      final Map<String, Map<Character, Integer>> palavrasParaChars) {
    if (mapaCaracteres.size() == 0) {
      imprimirAnagrama(conjuntoPalavras);
      return;
    }

    final var iterator = palavrasParaChars
        .entrySet()
        .iterator();

    while (iterator.hasNext()) {
      final var palavraMapaChars = iterator.next();
      final var palavra = palavraMapaChars.getKey();
      final var mapaChars = palavraMapaChars.getValue();

      Optional<Map<Character, Integer>> novoMapa =
          PALAVRAS_VALIDAS.recuperaNovoMapa(palavra, mapaChars, mapaCaracteres, conjuntoPalavras);

      novoMapa.ifPresent(novoMapaChars -> {
        final var palavrasOrdernadas = new TreeSet<>(conjuntoPalavras);
        palavrasOrdernadas.add(palavra);

        iterator.remove();

        executarRecursao(novoMapaChars, palavrasOrdernadas, new HashMap<>(palavrasParaChars));
      });
    }
  }

  private static void imprimirAnagrama(final Set<String> conjuntoPalavras) {
    final var sb = new StringBuilder();

    conjuntoPalavras.forEach(palavra -> sb.append(palavra).append(' '));

    // Remover o último espaço da palavra
    sb.deleteCharAt(sb.length() - 1);

    System.out.println(sb.toString());
  }

  private static String recuperarStringFormatada(final String[] listaPalavras) {
    final var sb = new StringBuilder();

    for (final var palavra : listaPalavras) {
      sb.append(palavra);
    }

    final var stringConcatenada = sb.toString();

    if (!stringConcatenada.matches("^[a-zA-Z ]*$")) {
      throw new RuntimeException(
          "Apenas palavras com letras, sem acentuacao e espaco sao permitidos.");
    }

    return stringConcatenada.replace(" ", "").toUpperCase();
  }
}

class PalavrasValidas {

  Map<String, Map<Character, Integer>> palavrasParaQtdCaracteres;

  PalavrasValidas(final String caminhoArquivoPalavrasValidas) {
    if (caminhoArquivoPalavrasValidas == null){
      throw new RuntimeException("Voce deve definir a variavel de ambiente CAMINHO_PALAVRAS_VALIDAS" +
          " com o path para o arquivo com as palavras validas.");
    }

    this.palavrasParaQtdCaracteres = montarMapaDePalavrasParaCaracteres(
        caminhoArquivoPalavrasValidas);
  }

  private Map<String, Map<Character, Integer>> montarMapaDePalavrasParaCaracteres(
      final String caminhoArquivoPalavrasValidas) {
    final var palavrasParaQtdCaracteres = new HashMap<String, Map<Character, Integer>>();

    try (final var leitorArquivo = new BufferedReader(
        new FileReader(caminhoArquivoPalavrasValidas))) {
      String palavraValida;
      while ((palavraValida = leitorArquivo.readLine()) != null) {
        final var caracteresParaQuantidades = montarMapaCaracteres(palavraValida);

        palavrasParaQtdCaracteres.put(palavraValida, caracteresParaQuantidades);
      }
    } catch (final IOException excecao) {
      throw new RuntimeException("Problema ao se abrir arquivo com palavras validas!", excecao);
    }

    return palavrasParaQtdCaracteres;
  }

  Map<Character, Integer> montarMapaCaracteres(final String palavraValida) {
    final var caracteresParaQuantidades = new HashMap<Character, Integer>();

    palavraValida.chars()
        .forEach(caractere -> caracteresParaQuantidades.merge((char) caractere, 1, Integer::sum));
    return caracteresParaQuantidades;
  }


  Optional<Map<Character, Integer>> recuperaNovoMapa(final String palavraValida,
      final Map<Character, Integer> mapaPalavraValida,
      final Map<Character, Integer> mapaAtualdaString,
      final Set<String> listaDePalavrasAnagrama) {

    if (listaDePalavrasAnagrama.contains(palavraValida) ||
        mapaPalavraValida.size() > mapaAtualdaString.size()) {
      return Optional.empty();
    }

    final var mapaResultante = new HashMap<>(mapaAtualdaString);

    for (final Map.Entry<Character, Integer> caractereQtd : mapaPalavraValida.entrySet()) {
      final var caractere = caractereQtd.getKey();
      final var qtd = caractereQtd.getValue();

      final var qtdFinal = mapaAtualdaString.getOrDefault(caractere, 0) - qtd;

      if (qtdFinal < 0) {
        return Optional.empty();
      }

      if (qtdFinal > 0) {
        mapaResultante.put(caractere, qtdFinal);
      } else {
        mapaResultante.remove(caractere);
      }
    }

    return Optional.of(mapaResultante);
  }


  void filtrarPalavrasValidas(final Map<Character, Integer> mapaInicial) {
    this.palavrasParaQtdCaracteres = this.palavrasParaQtdCaracteres
        .entrySet()
        .stream()
        .filter(e -> palavraCandidataAAnagrama(mapaInicial, e.getValue()))
        .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
  }

  private boolean palavraCandidataAAnagrama(final Map<Character, Integer> mapaInicial,
      final Map<Character, Integer> mapaPalavraValida) {
    if (mapaPalavraValida.size() > mapaInicial.size()) {
      return false;
    }

    for (final Map.Entry<Character, Integer> caractereQtd : mapaPalavraValida.entrySet()) {
      final var caractere = caractereQtd.getKey();

      final var qtdFinal = mapaInicial.getOrDefault(caractere, 0) - caractereQtd.getValue();
      if (qtdFinal < 0) {
        return false;
      }
    }

    return true;
  }
}