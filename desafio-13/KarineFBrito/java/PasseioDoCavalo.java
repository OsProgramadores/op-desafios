import java.util.List;
import java.util.ArrayList;

public class PasseioDoCavalo {

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
    int[][] tabuleiro = new int[8][8];

    for (int i = 0; i < 8; i++) {
      for (int j = 0; j < 8; j++) {
        tabuleiro[i][j] = -1;
      }
    }

    char letraDaColuna = casaInicial.charAt(0);
    int colunaInicial = letraDaColuna - 'a';

    char numeroDaLinhaChar = casaInicial.charAt(1);
    int numeroDaLinhaNoXadrez = Character.getNumericValue(numeroDaLinhaChar);
    int linhaInicial = 8 - numeroDaLinhaNoXadrez;

    resolverWarnsdorff(linhaInicial, colunaInicial, tabuleiro);
  }

  public static void resolverWarnsdorff(int linha, int coluna, int[][] tabuleiro) {
    int linhaAtual = linha;
    int colunaAtual = coluna;
    tabuleiro[linhaAtual][colunaAtual] = 0;

    List<String> caminho = new ArrayList<>();
    caminho.add(converterParaAlgebrica(linhaAtual, colunaAtual)); // ATENÇÃO

    for (int passo = 1; passo < 64; passo++) {
      int proximaLinha = -1;
      int proximaColuna = -1;
      int menorGrau = 9;

      for (int i = 0; i < 8; i++) {
        int nextLinha = linhaAtual + movimentosLinha[i];
        int nextColuna = colunaAtual + movimentosColuna[i];

        if (validando(nextLinha, nextColuna, tabuleiro)) {
          int grau = contarSaidasVazias(nextLinha, nextColuna, tabuleiro);
          if (grau < menorGrau) {
            menorGrau = grau;
            proximaLinha = nextLinha;
            proximaColuna = nextColuna;
          }
        }
      }

      if (proximaLinha == -1){
        break;
      }

      linhaAtual = proximaLinha;
      colunaAtual = proximaColuna;
      tabuleiro[linhaAtual][colunaAtual] = passo;
      caminho.add(converterParaAlgebrica(linhaAtual, colunaAtual));
    }

    for (int i = 0; i < caminho.size(); i++) {
      String casa = caminho.get(i);
      System.out.println(casa);
    }
  }

  private static int contarSaidasVazias(int linha, int coluna, int[][] tabuleiro) {
    int totalFugas = 0;
    for (int i = 0; i < 8; i++) {

      int linhaPulo = linha + movimentosLinha[i];
      int colunaPulo = coluna + movimentosColuna[i];
      if (validando(linhaPulo, colunaPulo, tabuleiro)) {
        totalFugas++;
      }
    }
    return totalFugas;
  }

  private static boolean validando(int linha, int coluna, int[][] tabuleiro) {

    boolean linhaValida = (linha >= 0 && linha < 8);
    boolean colunaValida = (coluna >= 0 && coluna < 8);

    if (!linhaValida || !colunaValida) {
      return false;
    }

    boolean casaVazia = (tabuleiro[linha][coluna] == -1);

    return casaVazia;
  }

  private static String converterParaAlgebrica(int linha, int coluna) {
    char letraDaColuna = (char) ('a' + coluna);
    int numeroDaLinha = 8 - linha;

    String resultado = "" + letraDaColuna + numeroDaLinha;

    return resultado;
  }
}
