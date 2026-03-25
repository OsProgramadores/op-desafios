package br.com.osprogramadores.antr4;

import br.com.osprogramadores.antlr4.CalculatorBaseVisitor;
import br.com.osprogramadores.antlr4.CalculatorParser.BracesContext;
import br.com.osprogramadores.antlr4.CalculatorParser.ChangeSignContext;
import br.com.osprogramadores.antlr4.CalculatorParser.DivisionContext;
import br.com.osprogramadores.antlr4.CalculatorParser.IntContext;
import br.com.osprogramadores.antlr4.CalculatorParser.MinusContext;
import br.com.osprogramadores.antlr4.CalculatorParser.MultiplicationContext;
import br.com.osprogramadores.antlr4.CalculatorParser.PlusContext;
import br.com.osprogramadores.antlr4.CalculatorParser.PowerContext;

public class Visitor extends CalculatorBaseVisitor<Integer> {

  @Override
  public Integer visitPlus(final PlusContext ctx) {
    return visit(ctx.plusOrMinus()) + visit(ctx.multOrDiv());
  }

  @Override
  public Integer visitMinus(final MinusContext ctx) {
    return visit(ctx.plusOrMinus()) - visit(ctx.multOrDiv());
  }

  @Override
  public Integer visitMultiplication(final MultiplicationContext ctx) {
    return visit(ctx.multOrDiv()) * visit(ctx.pow());
  }

  @Override
  public Integer visitDivision(final DivisionContext ctx) {
    return visit(ctx.multOrDiv()) / visit(ctx.pow());
  }

  @Override
  public Integer visitPower(final PowerContext ctx) {
    if (ctx.pow() != null) {
      return (int) Math.pow(visit(ctx.unaryMinus()), visit(ctx.pow()));
    }

    return visit(ctx.unaryMinus());
  }

  @Override
  public Integer visitChangeSign(final ChangeSignContext ctx) {
    return -1 * visit(ctx.unaryMinus());
  }

  @Override
  public Integer visitBraces(final BracesContext ctx) {
    return visit(ctx.plusOrMinus());
  }

  @Override
  public Integer visitInt(final IntContext ctx) {
    return Integer.parseInt(ctx.INT().getText());
  }
}
