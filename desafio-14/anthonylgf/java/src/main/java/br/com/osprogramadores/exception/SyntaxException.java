package br.com.osprogramadores.exception;

public class SyntaxException extends RuntimeException {

  private int line = 0;

  public SyntaxException(final int line, final Throwable cause) {
    super(cause);
    this.line = line;
  }

  @Override
  public String toString() {
    return "SyntaxException{" +
        "line=" + line +
        '}';
  }
}
