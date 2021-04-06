package horse;

import java.util.Optional;

/**
 * Algorithm used to solve horse tour problem using Warnsdoff's rule
 */
public class KnightTour {

  public static void main(final String[] args) {
    if (args.length != 1 || args[0].length() != 2) {
      System.out.println("Wou must run the program as java KnightTour <initial-square>");
      System.out.println("Example: java KnightTour a1 or java KnightTour b3");
      System.exit(1);
    }

    final var initialCoordinate = args[0].toLowerCase();

    final Square initialSquare = SquareManager.getInitialSquare(initialCoordinate);

    printMovements(initialSquare);
  }

  private static void printMovements(final Square initialSquare) {
    initialSquare.reachAndUpdateStatus();
    Optional<Square> actualSquare = Optional.of(initialSquare);

    do {
      actualSquare.ifPresent(Square::printSquareRepresentation);
      actualSquare = actualSquare.flatMap(Square::nextToMove);
    } while (actualSquare.isPresent());
  }

}
