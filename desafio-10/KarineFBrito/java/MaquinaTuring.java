import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MaquinaTuring {
  public static void main(String[] args) throws Exception {
    if (args.length != 1) {
      System.out.println(
          "Nenhum caminho foi fornecido, execute o programa usando: ' java MaquinaTuring"
              + " <caminho-absoluto>'");
      return;
    }
    File caminho = new File(args[0]);
    if (!caminho.exists()) {
      System.out.println("Esse caminho não existe");
      return;
    }
    File pastaRegras = caminho.getParentFile();
    try (BufferedReader br = new BufferedReader(new FileReader(caminho))) {
      String linha;
      while ((linha = br.readLine()) != null) {
        linha = linha.trim();
        if (linha.isEmpty()) {
          continue;
        }
        String[] partes = linha.split(",", 2);
        if (partes.length < 2) {
          System.err.println("Linha inválida (esperado 'arquivo,fitaEntrada'): " + linha);
          continue;
        }

        String arquivoRegras = partes[0].trim();
        String fitaEntrada = partes[1].replace(" ", "_");

        File arquivoRegra = new File(pastaRegras, arquivoRegras);
        Map<String, Map<String, List<Regra>>> regras =
            carregaRegras(arquivoRegra.getAbsolutePath());

        Fita fita = new Fita(fitaEntrada);
        String saida = executarMaquina(regras, fita, "0");
        System.out.println(
            arquivoRegras
                + ","
                + fitaEntrada.replace("_", " ").trim()
                + ","
                + saida.replace("_", " ").trim());
      }
    }
  }

  public static Map<String, Map<String, List<Regra>>> carregaRegras(String ArquivoRegras)
      throws Exception {
    Map<String, Map<String, List<Regra>>> regras = new HashMap<>();
    int posicao = 0;
    try (BufferedReader br = new BufferedReader(new FileReader(ArquivoRegras))) {
      String linha;
      while ((linha = br.readLine()) != null) {
        linha = linha.trim();
        if (linha.isEmpty() || linha.startsWith(";")) {
          continue;
        }
        int posComentario = linha.indexOf(";");
        if (posComentario != -1) {
          linha = linha.substring(0, posComentario);
        }
        if (linha.trim().isEmpty()) {
          continue;
        }
        String[] partes = linha.split("\\s+");
        if (partes.length == 5) {
          String estadoAtual = partes[0];
          String simboloLido = partes[1];
          String novoSimbolo = partes[2];
          String direcao = partes[3];
          String estadoNovo = partes[4];
          Regra regra =
              new Regra(posicao++, estadoAtual, simboloLido, novoSimbolo, direcao, estadoNovo);
          Map<String, List<Regra>> mapaSimboloRegras =
              regras.computeIfAbsent(estadoAtual, k -> new HashMap<>());
          List<Regra> listaRegras =
              mapaSimboloRegras.computeIfAbsent(simboloLido, k -> new ArrayList<>());
          listaRegras.add(regra);
        }
      }
    }
    return regras;
  }

  public static Regra procurarRegra(
      Map<String, Map<String, List<Regra>>> regras, String estadoAtual, char simboloLido) {
    Map<String, List<Regra>> mapaEstado = regras.get(estadoAtual);
    String simbolo = String.valueOf(simboloLido);
    if (mapaEstado != null && mapaEstado.containsKey(simbolo)) {
      return menorPosicao(mapaEstado.get(simbolo));
    }
    Map<String, List<Regra>> generico = regras.get("*");
    if (mapaEstado != null
        && mapaEstado.containsKey("*")
        && generico != null
        && generico.containsKey(simbolo)) {
      Regra r1 = menorPosicao(mapaEstado.get("*"));
      Regra r2 = menorPosicao(generico.get(simbolo));
      return (r1.posicao < r2.posicao) ? r1 : r2;
    }
    if (mapaEstado != null && mapaEstado.containsKey("*")) {
      return menorPosicao(mapaEstado.get("*"));
    }
    if (generico != null && generico.containsKey(simbolo)) {
      return menorPosicao(generico.get(simbolo));
    }
    if (generico != null && generico.containsKey("*")) {
      return menorPosicao(generico.get("*"));
    }

    return null;
  }

  public static Regra menorPosicao(List<Regra> lista) {
    if (lista == null || lista.isEmpty()) {
      return null;
    }
    Regra menor = lista.get(0);
    for (Regra r : lista) {
      if (r.posicao < menor.posicao) {
        menor = r;
      }
    }
    return menor;
  }

  public static String executarMaquina(
      Map<String, Map<String, List<Regra>>> regras, Fita fita, String estadoAtual) {
    do {
      char simboloLido = fita.ler();
      Regra regra = procurarRegra(regras, estadoAtual, simboloLido);

      if (regra == null) {
        return "ERR";
      }

      String novoSimbolo = regra.novoSimbolo;
      String direcao = regra.direcao;
      String estadoNovo = regra.estadoNovo;

      if (!novoSimbolo.equals("*")) {
        fita.escrever(novoSimbolo.charAt(0));
      }
      fita.mover(direcao);
      estadoAtual = estadoNovo;
    } while (!estadoAtual.startsWith("halt"));
    return fita.toString();
  }
}
