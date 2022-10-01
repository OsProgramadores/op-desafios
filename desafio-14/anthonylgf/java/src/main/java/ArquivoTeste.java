import static java.lang.System.exit;
import static java.lang.System.out;

import br.com.osprogramadores.antlr4.CalculatorLexer;
import br.com.osprogramadores.antlr4.CalculatorParser;
import br.com.osprogramadores.antr4.ErrorListener;
import br.com.osprogramadores.antr4.Visitor;
import br.com.osprogramadores.exception.SyntaxException;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;

public class ArquivoTeste {

  public static void main(final String[] args) {
    if (args.length != 1) {
      out.println("You should run java Main <file-path>");
      exit(-1);
    }

    try (final var scanner = new Scanner(new File(args[0]))) {
      while (scanner.hasNextLine()) {
        final String expression = scanner.nextLine().trim();

        try {
          final int result = solveExpression(expression);
          out.println(result);
        } catch (final ArithmeticException arithmeticException) {
          out.println("ERR DIVBYZERO");
        } catch (final SyntaxException syntaxException) {
          out.println("ERR SYNTAX");
        }
      }

    } catch (FileNotFoundException e) {
      out.println("Defined a non-existent file: " + args[0]);
      exit(-1);
    }
  }

  static int solveExpression(final String expression) {
    final var expressionAsStream = CharStreams.fromString(expression);
    final var listener = new ErrorListener();
    final var lexer = new CalculatorLexer(expressionAsStream);

    lexer.removeErrorListeners();
    lexer.addErrorListener(listener);

    final var token = new CommonTokenStream(lexer);
    final var parser = new CalculatorParser(token);

    parser.removeErrorListeners();
    parser.addErrorListener(listener);

    final ParseTree rootNode = parser.plusOrMinus();

    final Visitor visitor = new Visitor();

    return visitor.visit(rootNode);
  }
}
