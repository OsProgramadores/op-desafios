import static java.lang.String.format;

import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

public enum Pieces {
  VAZIO("Vazio", 0),
  PEAO("Peao", 1),
  BISPO("Bispo", 2),
  CAVALO("Cavalo", 3),
  TORRE("Torre", 4),
  DAMA("Dama", 5),
  REI("Rei", 6);

  private static final Map<Integer, Pieces> CODE_TO_PIECE;

  static {
    CODE_TO_PIECE =
        Map.of(
            VAZIO.getPieceCode(), VAZIO,
            PEAO.getPieceCode(), PEAO,
            BISPO.getPieceCode(), BISPO,
            CAVALO.getPieceCode(), CAVALO,
            TORRE.getPieceCode(), TORRE,
            DAMA.getPieceCode(), DAMA,
            REI.getPieceCode(), REI);
  }

  private final String namePiece;

  private final int pieceCode;

  private int qtyPieces;

  Pieces(final String namePiece, final int pieceCode) {
    this.namePiece = namePiece;
    this.pieceCode = pieceCode;
    this.qtyPieces = 0;
  }

  public void incrementNumberPiece() {
    this.qtyPieces++;
  }

  public static Pieces getPieceByCode(final int pieceCode) {
    return Optional.ofNullable(CODE_TO_PIECE.get(pieceCode))
        .orElseThrow(() -> new RuntimeException(format("Codigo de peca invalido: %d", pieceCode)));
  }

  public static void printQtyPieces() {
    final var filteredPieces =
        CODE_TO_PIECE.values().stream()
            .filter(p -> p.getPieceCode() > 0)
            .collect(Collectors.toList());

    for (final Pieces piece : filteredPieces) {
      final var stringToPrint =
          format("%s: %d peca(s)", piece.getNamePiece(), piece.getQtyPieces());
      System.out.println(stringToPrint);
    }
  }

  public String getNamePiece() {
    return this.namePiece;
  }

  public int getQtyPieces() {
    return this.qtyPieces;
  }

  public int getPieceCode() {
    return this.pieceCode;
  }
}
