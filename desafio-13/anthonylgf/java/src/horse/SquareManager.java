package horse;

import java.util.HashSet;

public class SquareManager {

  private static final Square[][] boardSquares = initiateSquareArray();

  static Square getInitialSquare(final String initialCoordinate) {
    final int longitude = initialCoordinate.charAt(0) - 97;
    final int latitude = initialCoordinate.charAt(1) - 49;

    try {
      return boardSquares[latitude][longitude];
    } catch (Exception e) {
      throw new RuntimeException("You defined an invalid coordinate!");
    }
  }

  private static Square[][] initiateSquareArray() {
    final var squareArray = new Square[8][8];

    final var possibilitiesToMoveFirst = new int[]{2, -2};
    final var possibilitiesToMoveSecond = new int[]{1, -1};

    for (int i = 0; i < 8; i++) {
      for (int j = 0; j < 8; j++) {
        initiateSquareForCoordinate(i, j, squareArray, possibilitiesToMoveFirst,
            possibilitiesToMoveSecond);
      }
    }

    return squareArray;
  }

  private static void initiateSquareForCoordinate(final int latitude, final int longitude,
      final Square[][] squares, final int[] possibilitiesToMoveFirst,
      final int[] possibilitiesToMoveSecond) {
    final Square square = ensureSquareExists(latitude, longitude, squares);

    getTheNextSquareThatCanMove(longitude, latitude, squares, square, possibilitiesToMoveFirst,
        possibilitiesToMoveSecond, false);

    getTheNextSquareThatCanMove(latitude, longitude, squares, square, possibilitiesToMoveFirst,
        possibilitiesToMoveSecond, true);
  }

  private static void getTheNextSquareThatCanMove(final int coordinate1, final int coordinate2,
      final Square[][] squares, final Square square, final int[] possibilitiesToMoveFirst,
      final int[] possibilitiesToMoveSecond, final boolean isLatitudeFirst) {
    for (final int k : possibilitiesToMoveFirst) {
      for (final int i : possibilitiesToMoveSecond) {
        try {
          final Square squareThatCanMove;

          if (isLatitudeFirst) {
            squareThatCanMove = ensureSquareExists(coordinate1 + k,
                coordinate2 + i, squares);
          } else {
            squareThatCanMove = ensureSquareExists(coordinate2 + i,
                coordinate1 + k, squares);
          }

          square.addSquareInPossibilityList(squareThatCanMove);
        } catch (Exception ignored) {
        }
      }
    }
  }

  private static Square ensureSquareExists(final int latitude, final int longitude,
      final Square[][] squares) {
    final var square = squares[latitude][longitude];

    if (square != null) {
      return square;
    }

    final var createdSquare = new Square(latitude, longitude, new HashSet<>());
    squares[latitude][longitude] = createdSquare;

    return createdSquare;
  }
}
