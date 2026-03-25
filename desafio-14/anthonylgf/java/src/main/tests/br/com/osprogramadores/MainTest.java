package br.com.osprogramadores;

import br.com.osprogramadores.exception.SyntaxException;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class MainTest {

  @Test
  public void solveExpression1() {
    final int expressionResult = Main.solveExpression("1 + 0 + 25 - 3");

    Assertions.assertEquals(23, expressionResult);
  }

  @Test
  public void solveExpression2() {
    final int expressionResult = Main.solveExpression("1+1*5-1");

    Assertions.assertEquals(5, expressionResult);
  }

  @Test
  public void solveExpression3() {
    final int expressionResult = Main.solveExpression("1 + 4 / 2 ^2 - 1");

    Assertions.assertEquals(1, expressionResult);
  }

  @Test
  public void solveExpression4() {
    final int expressionResult = Main.solveExpression("1 + 3 * 6 / 2 + 0");

    Assertions.assertEquals(10, expressionResult);
  }

  @Test
  public void solveExpression5() {
    Assertions.assertThrows(ArithmeticException.class,
        () -> Main.solveExpression("0 / 1 + 1 / 0"));
  }

  @Test
  public void solveExpression6() {
    final int expressionResult = Main.solveExpression("1 * (5 + 10) / 3");

    Assertions.assertEquals(5, expressionResult);
  }

  @Test
  public void solveExpression7() {
    final int expressionResult = Main.solveExpression("((5-1) * 2)^2");

    Assertions.assertEquals(64, expressionResult);
  }

  @Test
  public void solveExpression8() {
    final int expressionResult = Main.solveExpression("(2 - 1) * 2^3");

    Assertions.assertEquals(8, expressionResult);
  }

  @Test
  public void solveExpression9() {
    Assertions.assertThrows(ArithmeticException.class,
        () -> Main.solveExpression("4 / (54 - (9 * 6))"));
  }

  @Test
  public void solveExpression10() {
    Assertions.assertThrows(SyntaxException.class,
        () -> Main.solveExpression("54 * * 54 - 1"));
  }

  @Test
  public void solveExpression11() {
    Assertions.assertThrows(SyntaxException.class,
        () -> Main.solveExpression("((79 - 12) * (5 + (2 - 1))"));
  }
}
