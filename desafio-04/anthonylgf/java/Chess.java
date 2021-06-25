import java.util.Scanner;

public class Chess {

  private static final int TAMANHO_TABULEIRO = 8;

  public static void main(final String[] args) {

    final int[][] tabuleiro = fillBoard();

    for(int i=0; i<TAMANHO_TABULEIRO; i++){
      for(int j=0; j<TAMANHO_TABULEIRO; j++){
        // Recupera  a peca pelo codigo inserido pelo usuario
        // e incrementa a quantidade da peca inserida
        Piece.getPieceByCode(tabuleiro[i][j])
          .incrementNumberPiece();
      }
    }

    Piece.printQtyPieces();
  }

  private static int[][] fillBoard(){
    final var tabuleiro = new int[TAMANHO_TABULEIRO][TAMANHO_TABULEIRO];

    try(final var in = new Scanner(System.in)){
      // Código para preencher tabuleiro
      // O usuário ira inserir individualmente cada numero de cada
      // peca do tabuleiro
      for(int i=0; i<TAMANHO_TABULEIRO; i++){
        for(int j=0; j<TAMANHO_TABULEIRO; j++){
          tabuleiro[i][j] = in.nextInt();
        }
      }
    }

    return tabuleiro;
  }
}
