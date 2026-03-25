package br.com.osprogramadores;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;
import org.eclipse.collections.api.map.primitive.IntIntMap;
import org.eclipse.collections.impl.factory.primitive.IntIntMaps;

public class PalavrasValidas {

  Map<String, IntIntMap> palavrasParaQtdCaracteres;

  PalavrasValidas(final String caminhoArquivoPalavrasValidas) {
    if (caminhoArquivoPalavrasValidas == null) {
      throw new RuntimeException(
          "Voce deve definir a variavel de ambiente CAMINHO_PALAVRAS_VALIDAS" +
              " com o path para o arquivo com as palavras validas.");
    }

    this.palavrasParaQtdCaracteres = montarMapaDePalavrasParaCaracteres(
        caminhoArquivoPalavrasValidas);
  }

  private Map<String, IntIntMap> montarMapaDePalavrasParaCaracteres(
      final String caminhoArquivoPalavrasValidas) {
    final var palavrasParaQtdCaracteres = new HashMap<String, IntIntMap>();

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

  IntIntMap montarMapaCaracteres(final String palavraValida) {
    final var caracteresParaQuantidades = IntIntMaps.mutable.empty();

    palavraValida.chars()
        .forEach(caractere -> {
          try {
            int qtdCaracetere = caracteresParaQuantidades.getOrThrow(caractere);
            caracteresParaQuantidades.put(caractere, qtdCaracetere + 1);
          } catch (Exception e) {
            caracteresParaQuantidades.put(caractere, 1);
          }
        });
    return caracteresParaQuantidades;
  }


  IntIntMap recuperaNovoMapa(final IntIntMap mapaPalavraValida,
      final IntIntMap mapaAtualdaString) {

    if (mapaPalavraValida.size() > mapaAtualdaString.size()) {
      return null;
    }

    final var mapaResultante =
        IntIntMaps.mutable.ofAll(mapaAtualdaString);

    for (final var caractereQtd : mapaPalavraValida.keyValuesView()) {
      final var caractere = caractereQtd.getOne();
      final var qtd = caractereQtd.getTwo();

      final var qtdFinal = mapaAtualdaString.get(caractere) - qtd;

      if (qtdFinal < 0) {
        return null;
      }

      if (qtdFinal > 0) {
        mapaResultante.put(caractere, qtdFinal);
      } else {
        mapaResultante.remove(caractere);
      }
    }

    return mapaResultante;
  }


  void filtrarPalavrasValidas(final IntIntMap mapaInicial) {
    this.palavrasParaQtdCaracteres = this.palavrasParaQtdCaracteres
        .entrySet()
        .stream()
        .filter(e -> palavraCandidataAAnagrama(mapaInicial, e.getValue()))
        .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
  }

  private boolean palavraCandidataAAnagrama(final IntIntMap mapaInicial,
      final IntIntMap mapaPalavraValida) {
    if (mapaPalavraValida.size() > mapaInicial.size()) {
      return false;
    }

    for (final var caractereQtd : mapaPalavraValida.keyValuesView()) {
      final var caractere = caractereQtd.getOne(); // returns the character

      try {
        final var qtdFinal = mapaInicial.getOrThrow(caractere) - caractereQtd.getTwo();
        if (qtdFinal < 0) {
          return false;
        }
      } catch (Exception e) {
        return false;
      }
    }

    return true;
  }
}