package br.com.osprogramadores;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Optional;
import java.util.Queue;
import java.util.Set;
import java.util.TreeSet;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import org.eclipse.collections.api.map.primitive.IntIntMap;

public class Main {

  private static final PalavrasValidas PALAVRAS_VALIDAS = new PalavrasValidas(
      System.getenv("CAMINHO_PALAVRAS_VALIDAS"));

  private static final BufferedWriter SAIDA =
      new BufferedWriter(new OutputStreamWriter(System.out), 4096);

  private static final Lock SAIDA_LOCK = new ReentrantLock();

  private static final ExecutorService EXECUTOR_THREADS = Executors.newWorkStealingPool(
      Runtime.getRuntime().availableProcessors() * 2
  );

  private static final AtomicInteger QTD_TAREFAS = new AtomicInteger(0);

  public static void main(final String[] listaPalavras) {
    if (listaPalavras.length == 0) {
      System.out.println(
          "Defina uma lista de palavras para se obter o anagrama: java Desafio6 [lista-palavras]");
      System.exit(1);
    }

    final String stringFormatada = recuperarStringFormatada(listaPalavras);
    final IntIntMap mapaInicialDeCaracteres =
        PALAVRAS_VALIDAS.montarMapaCaracteres(stringFormatada);

    PALAVRAS_VALIDAS.filtrarPalavrasValidas(mapaInicialDeCaracteres);

    executarRecursao(mapaInicialDeCaracteres, new HashSet<>(),
        PALAVRAS_VALIDAS.palavrasParaQtdCaracteres);

    try {
      esperarTaskFinalizarem();
      SAIDA.flush();
    } catch (IOException | ExecutionException | InterruptedException e) {
      throw new RuntimeException("Erro na hora de imprimir anagrama!", e);
    }

  }

  private static void esperarTaskFinalizarem() throws ExecutionException, InterruptedException {
    while (QTD_TAREFAS.get() > 0) {
      Thread.sleep(100);
    }
  }

  private static void executarRecursao(final IntIntMap mapaCaracteres,
      final Set<String> conjuntoPalavras,
      final Map<String, IntIntMap> palavrasParaChars) {
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

      final IntIntMap novoMapa =
          PALAVRAS_VALIDAS.recuperaNovoMapa(mapaChars, mapaCaracteres);

      if (novoMapa != null) {
        final var palavrasOrdernadas = new HashSet<>(conjuntoPalavras);
        palavrasOrdernadas.add(palavra);

        iterator.remove();

        QTD_TAREFAS.incrementAndGet();
        final var palavrasExcluindoUtilizadas = new HashMap<>(palavrasParaChars);
        EXECUTOR_THREADS.submit(
            () -> {
              executarRecursao(novoMapa, palavrasOrdernadas,
                  palavrasExcluindoUtilizadas);
              QTD_TAREFAS.decrementAndGet();
            });
      }
    }
  }

  private static void imprimirAnagrama(final Set<String> conjuntoPalavras) {
    final var sb = new StringBuilder();

    conjuntoPalavras.stream()
        .sorted()
        .forEach(palavra -> sb.append(palavra).append(' '));

    // Remover o último espaço da palavra
    sb.deleteCharAt(sb.length() - 1);

    SAIDA_LOCK.lock();
    try {
      SAIDA.write(sb.toString());
      SAIDA.write('\n');
    } catch (IOException e) {
      throw new RuntimeException("Erro no momento de imprimir anagrama!", e);
    } finally {
      SAIDA_LOCK.unlock();
    }
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