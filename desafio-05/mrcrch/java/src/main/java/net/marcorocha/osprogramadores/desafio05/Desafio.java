package net.marcorocha.osprogramadores.desafio05;

import com.jsoniter.JsonIterator;
import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.stream.Collectors;

class Desafio {

  private final EstatisticasSalariais estatisticaEmpresa = new EstatisticasSalariais("EMPRESA");
  private final Map<String, EstatisticasSalariais> estatisticasPorArea = new HashMap<>();
  private final Map<String, EstatisticasSalariais> estatisticasPorSobrenome = new HashMap<>();

  private final Map<String, String> areas = new HashMap<>();
  private final Map<String, Integer> quantidadeFuncionariosPorArea = new HashMap<>();

  private void adicionarFuncionario(String area, String nome, String sobrenome, double salario) {

    // Estatísticas gerais (questão 1)
    estatisticaEmpresa.adicionar(salario, nome, sobrenome);

    // Estatísticas por área (questão 2)
    EstatisticasSalariais resumoArea = estatisticasPorArea.get(area);
    if (resumoArea == null) {
      resumoArea = new EstatisticasSalariais(area);
    }

    resumoArea.adicionar(salario, nome, sobrenome);
    estatisticasPorArea.put(area, resumoArea);

    // Funcionários por área (questão 3)
    Integer funcionariosPorArea = quantidadeFuncionariosPorArea.get(area);
    if (funcionariosPorArea == null) {
      funcionariosPorArea = 1;
    } else {
      funcionariosPorArea++;
    }

    quantidadeFuncionariosPorArea.put(area, funcionariosPorArea);

    // Estatísticas por sobrenome (questão 4)
    EstatisticasSalariais resumoSobrenome = estatisticasPorSobrenome.get(sobrenome);
    if (resumoSobrenome == null) {
      resumoSobrenome = new EstatisticasSalariais(sobrenome);
    }

    resumoSobrenome.adicionar(salario, nome, sobrenome);
    estatisticasPorSobrenome.put(sobrenome, resumoSobrenome);
  }

  void resolver(String arquivo) {
    lerArquivo(arquivo);
    exibirResultado();
  }

  private void lerArquivo(String arquivo) {

    final File file = new File(arquivo);
    if (!file.exists() || !file.isFile()) {
      throw new IllegalArgumentException("Arquivo inválido");
    }

    try (InputStream is = new BufferedInputStream(new FileInputStream(file))) {

      JsonIterator iterator = JsonIterator.parse(is, 32 * 1024);

      for (String field = iterator.readObject(); field != null; field = iterator.readObject()) {
        switch (field) {
          case "funcionarios":
            lerFuncionarios(iterator);
            break;

          case "areas":
            lerAreas(iterator);
            break;

          default:
            // Ignorando atributo desconhecido
            iterator.skip();
        }
      }

    } catch (final IOException e) {
      throw new IllegalStateException("Erro lendo o arquivo", e);
    }
  }

  private static final void exibirEstatisticaIndividual(
      CustomWriter cw,
      Double salario,
      Collection<String> nomes,
      String tipo,
      String prefixo,
      String area)
      throws IOException {

    String inicio = prefixo + "_" + tipo + "|";
    if (area != null) {
      inicio += area + "|";
    }

    String salarioFormatado = String.format("%.2f", salario).replace(',', '.');
    if (nomes != null) {
      salarioFormatado = "|" + salarioFormatado;
      for (final String s : nomes) {
        cw.writeln(inicio + s + salarioFormatado);
      }
    } else {
      cw.writeln(inicio + salarioFormatado);
    }
  }

  private static final void exibirEstatistica(
      CustomWriter cw, EstatisticasSalariais es, String prefixo, String area) throws IOException {

    exibirEstatisticaIndividual(
        cw, es.getMaiorSalario(), es.getFuncionariosMaiorSalario(), "max", prefixo, area);
    exibirEstatisticaIndividual(
        cw, es.getMenorSalario(), es.getFuncionariosMenorSalario(), "min", prefixo, area);
    exibirEstatisticaIndividual(cw, es.getMediaSalarial(), null, "avg", prefixo, area);
  }

  private void exibirResultado() {

    try (CustomWriter cw = new CustomWriter()) {

      // Questão 1
      exibirEstatistica(cw, estatisticaEmpresa, "global", null);

      // Questão 2
      for (final Entry<String, EstatisticasSalariais> e : estatisticasPorArea.entrySet()) {
        final EstatisticasSalariais es = e.getValue();
        exibirEstatistica(cw, es, "area", areas.get(es.getCodigo()));
      }

      // Questão 3
      final List<Entry<String, Integer>> sorted =
          quantidadeFuncionariosPorArea.entrySet().stream()
              .sorted(Map.Entry.comparingByValue())
              .collect(Collectors.toList());

      final int min = sorted.get(0).getValue();
      final int max = sorted.get(sorted.size() - 1).getValue();

      for (final Entry<String, Integer> e : sorted) {
        final int v = e.getValue().intValue();
        if (v == max) {
          cw.writeln("most_employees|" + areas.get(e.getKey()) + "|" + max);
        } else if (v == min) {
          cw.writeln("least_employees|" + areas.get(e.getKey()) + "|" + min);
        }
      }

      // Questão 4
      for (final Entry<String, EstatisticasSalariais> e : estatisticasPorSobrenome.entrySet()) {

        final EstatisticasSalariais estatisticas = e.getValue();
        if (estatisticas.getTotalFuncionarios() > 1) {

          exibirEstatisticaIndividual(
              cw,
              estatisticas.getMaiorSalario(),
              estatisticas.getFuncionariosMaiorSalario(),
              "max",
              "last_name",
              e.getKey());
        }
      }

    } catch (final IOException e) {
      throw new IllegalStateException("Erro exibindo a saída", e);
    }
  }

  private final void lerFuncionarios(JsonIterator iterator) throws IOException {

    while (iterator.readArray()) {
      lerFuncionario(iterator);
    }
  }

  private void lerFuncionario(JsonIterator iterator) {

    String nome = null;
    String sobrenome = null;
    String area = null;
    double salario = 0.0;

    try {

      for (String name = iterator.readObject(); name != null; name = iterator.readObject()) {

        switch (name) {
          case "id":
            // Não será necessário
            iterator.skip();
            break;

          case "nome":
            nome = iterator.readString();
            break;

          case "sobrenome":
            sobrenome = iterator.readString();
            break;

          case "salario":
            salario = iterator.readDouble();
            break;

          case "area":
            area = iterator.readString();
            break;

          default:
            // Ignorando atributo desconhecido
            break;
        }
      }

      adicionarFuncionario(area, nome, sobrenome, salario);

    } catch (final IOException e) {
      throw new IllegalStateException("Erro lendo registro de funcionário", e);
    }
  }

  private final void lerAreas(JsonIterator iterator) throws IOException {

    while (iterator.readArray()) {
      lerArea(iterator);
    }
  }

  private void lerArea(JsonIterator iterator) {

    String codigo = null;
    String nome = null;

    try {

      for (String name = iterator.readObject(); name != null; name = iterator.readObject()) {

        switch (name) {
          case "codigo":
            codigo = iterator.readString();
            break;

          case "nome":
            nome = iterator.readString();
            break;

          default:
            // Ignorando atributo desconhecido
            break;
        }
      }

      areas.put(codigo, nome);

    } catch (final IOException e) {
      throw new IllegalStateException("Erro lendo registro de área", e);
    }
  }
}
