package br.com.osprogramadores.antr4;

import br.com.osprogramadores.exception.SyntaxException;
import org.antlr.v4.runtime.BaseErrorListener;
import org.antlr.v4.runtime.RecognitionException;
import org.antlr.v4.runtime.Recognizer;

public class ErrorListener extends BaseErrorListener {

  @Override
  public void syntaxError(final Recognizer<?, ?> recognizer, final Object offendingSymbol,
      final int line, final int charPositionInLine, final String msg,
      final RecognitionException e) {
    throw new SyntaxException(line, e);
  }
}
