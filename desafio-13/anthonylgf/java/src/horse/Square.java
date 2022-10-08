package horse;

import java.util.Optional;
import java.util.Set;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.function.BinaryOperator;
import java.util.stream.Collectors;

public class Square {

  private Set<Square> squaresThatCanMove;

  private final AtomicBoolean reached = new AtomicBoolean(false);

  private final String coordinate;

  public Square(final int latitude, final int longitude, final Set<Square> squaresThatCanMove) {
    this.squaresThatCanMove = squaresThatCanMove;
    this.coordinate = getCoordinateRepresentation(latitude, longitude);
  }

  private String getCoordinateRepresentation(final int latitude, final int longitude) {
    final char latitudeChar = (char) (latitude + 49);
    final char longitudeChar = (char) (longitude + 97);

    return String.format("%c%c", longitudeChar, latitudeChar);
  }

  public int quantityOfSquaresToMove() {
    this.squaresThatCanMove =
        this.squaresThatCanMove.stream().filter(Square::isNotReached).collect(Collectors.toSet());

    return this.squaresThatCanMove.size();
  }

  public void addSquareInPossibilityList(final Square square) {
    this.squaresThatCanMove.add(square);
  }

  public boolean isNotReached() {
    return !this.reached.get();
  }

  public Optional<Square> nextToMove() {
    final var nextToMove =
        Optional.ofNullable(squaresThatCanMove.stream().reduce(null, squareBinaryOperator));

    nextToMove.ifPresent(Square::reachAndUpdateStatus);

    return nextToMove;
  }

  public boolean reachAndUpdateStatus() {
    return reached.getAndSet(true);
  }

  private final BinaryOperator<Square> squareBinaryOperator =
      (square, square2) -> {
        if (square == null) {
          square2.quantityOfSquaresToMove();
          return square2;
        }

        if (square2 == null) {
          square.quantityOfSquaresToMove();
          return square;
        }

        final var quantitySquare1 = square.quantityOfSquaresToMove();
        final var quantitySquare2 = square2.quantityOfSquaresToMove();

        return quantitySquare1 <= quantitySquare2 ? square : square2;
      };

  public void printSquareRepresentation() {
    System.out.println(this);
  }

  @Override
  public String toString() {
    return coordinate;
  }
}
