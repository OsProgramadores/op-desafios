import java.util.ArrayList;
import java.util.List;

public class PasseioDoCavalo {

  private static final int tamanhoTabuleiro = 8;
  private static final int totalCasas = tamanhoTabuleiro * tamanhoTabuleiro;
  private static final int casaVazia = -1;
  private static final int grauMax = 9;
  private static final int[] movimentosLinha = {2, 1, -1, -2, -2, -1, 1, 2};
  private static final int[] movimentosColuna = {1, 2, 2, 1, -1, -2, -2, -1};

  public static void main(String[] args) {
    if (args.length != 1) {
      System.out.println(
          "Nenhuma casa foi fornecido,  execute o programa usando java PasseioDoCavalo <casa>"
              + " (ex.:a1)");
      return;
    }

    String casaInicial = args[0].toLowerCase();

    if (casaInicial.length() != 2
        || casaInicial.charAt(0) < 'a'
        || casaInicial.charAt(0) > 'h'
        || casaInicial.charAt(1) < '1'
        || casaInicial.charAt(1) > '8') {

      System.out.println("Erro: Posicao '" + casaInicial + "' invalida! Use de a1 a h8.");
      return;
    }
    int[][] tabuleiro = inicializarTabuleiro();

    char letraDaColuna = casaInicial.charAt(0);
    int colunaInicial = letraDaColuna - 'a';

    char numeroDaLinhaChar = casaInicial.charAt(1);
    int numeroDaLinhaNoXadrez = Character.getNumericValue(numeroDaLinhaChar);
    int linhaInicial = tamanhoTabuleiro - numeroDaLinhaNoXadrez;

    List<String> caminho = new ArrayList<>();

    if (!resolverWarnsdorff(linhaInicial, colunaInicial, 0, tabuleiro, caminho)) {
      System.out.println(
          "Caminho incompleto! O cavalo ficou preso apos " + caminho.size() + " casas:");
      for (String casa : caminho) {
        System.out.println(casa);
      }
    }
  }

  private static int[][] inicializarTabuleiro() {
    int[][] novoTabuleiro = new int[tamanhoTabuleiro][tamanhoTabuleiro];
    for (int i = 0; i < tamanhoTabuleiro; i++) {
      for (int j = 0; j < tamanhoTabuleiro; j++) {
        novoTabuleiro[i][j] = casaVazia;
      }
    }
    return novoTabuleiro;
  }

  public static boolean resolverWarnsdorff(
      int linha, int coluna, int passo, int[][] tabuleiro, List<String> caminho) {
    tabuleiro[linha][coluna] = passo;
    caminho.add(converterParaAlgebrica(linha, coluna));

    if (passo == totalCasas - 1) {
      for (String casa : caminho) {
        System.out.println(casa);
      }
      return true;
    }

    int[][] opcoes = new int[8][3];
    int qtdOpcoes = 0;

    for (int i = 0; i < 8; i++) {
      int nextLinha = linha + movimentosLinha[i];
      int nextColuna = coluna + movimentosColuna[i];

      if (movimentoValido(nextLinha, nextColuna, tabuleiro)) {
        opcoes[qtdOpcoes][0] = nextLinha;
        opcoes[qtdOpcoes][1] = nextColuna;
        opcoes[qtdOpcoes][2] = contarSaidasVazias(nextLinha, nextColuna, tabuleiro);
        qtdOpcoes++;
      }
    }

    ordenarOpcoes(opcoes, qtdOpcoes);

    for (int i = 0; i < qtdOpcoes; i++) {
      int proximaL = opcoes[i][0];
      int proximaC = opcoes[i][1];

      if (resolverWarnsdorff(proximaL, proximaC, passo + 1, tabuleiro, caminho)) {
        return true;
      }
    }

    tabuleiro[linha][coluna] = casaVazia;
    caminho.remove(caminho.size() - 1);
    return false;
  }

  private static void ordenarOpcoes(int[][] opcoes, int qtd) {
    for (int i = 0; i < qtd - 1; i++) {
      for (int j = 0; j < qtd - i - 1; j++) {
        if (opcoes[j][2] > opcoes[j + 1][2]) {
          int[] temp = opcoes[j];
          opcoes[j] = opcoes[j + 1];
          opcoes[j + 1] = temp;
        }
      }
    }
  }

  private static int contarSaidasVazias(int linha, int coluna, int[][] tabuleiro) {
    int totalFugas = 0;
    for (int i = 0; i < tamanhoTabuleiro; i++) {

      int linhaPulo = linha + movimentosLinha[i];
      int colunaPulo = coluna + movimentosColuna[i];
      if (movimentoValido(linhaPulo, colunaPulo, tabuleiro)) {
        totalFugas++;
      }
    }
    return totalFugas;
  }

  private static boolean movimentoValido(int linha, int coluna, int[][] tabuleiro) {

    boolean linhaValida = (linha >= 0 && linha < tamanhoTabuleiro);
    boolean colunaValida = (coluna >= 0 && coluna < tamanhoTabuleiro);

    if (!linhaValida || !colunaValida) {
      return false;
    }

    boolean casaVazia = (tabuleiro[linha][coluna] == -1);

    return casaVazia;
  }

  private static String converterParaAlgebrica(int linha, int coluna) {
    char letraDaColuna = (char) ('a' + coluna);
    int numeroDaLinha = tamanhoTabuleiro - linha;

    String resultado = String.valueOf(letraDaColuna) + numeroDaLinha;

    return resultado;
  }
}
