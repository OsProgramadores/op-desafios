import java.util.Map;
import java.util.Optional;

public enum Piece {

    VAZIO("Vazio", 0),
    PEAO("Peao", 1),
    BISPO("Bispo", 2),
    CAVALO("Cavalo", 3),
    TORRE("Torre", 4),
    DAMA("Dama", 5),
    REI("Rei", 6);

    private static final Map<Integer, Piece> CODE_TO_PIECE;

    static {
        CODE_TO_PIECE = Map.of(
            VAZIO.getPieceCode(), VAZIO,
            PEAO.getPieceCode(), PEAO,
            BISPO.getPieceCode(), BISPO,
            CAVALO.getPieceCode(), CAVALO,
            TORRE.getPieceCode(), TORRE,
            DAMA.getPieceCode(), DAMA,
            REI.getPieceCode(), REI
        );
    }
    
    private final String namePiece;

    private final int pieceCode;
    
    private int qtyPieces;

    Piece(final String namePiece, final int pieceCode){
        this.namePiece = namePiece;
        this.pieceCode = pieceCode;
        this.qtyPieces = 0;
    }

    public void incrementNumberPiece(){
        this.qtyPieces++;
    }

    public static Piece getPieceByCode(final int pieceCode) {
        return Optional.ofNullable(CODE_TO_PIECE.get(pieceCode))
            .orThrow(() -> new RuntimeException(String.format("Codigo de peca invalido: %d", pieceCode)));
    }

    public String getNamePiece(){
        return this.namePiece;
    }

    public String getQtyPieces(){
        return this.qtyPieces;
    }

    public int getPieceCode(){
        return this.pieceCode;
    }
}