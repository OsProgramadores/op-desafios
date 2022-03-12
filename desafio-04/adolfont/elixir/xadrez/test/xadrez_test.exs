defmodule XadrezTest do
  use ExUnit.Case

  test "Teste 1 do site" do
    entrada = """
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 1 1 0 0 0
    0 0 0 1 1 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    """

    assert Xadrez.contabiliza_pecas(entrada) == {4, 0, 0, 0, 0, 0}
  end

  test "Teste 2 do site" do
    entrada = """
    4 3 2 5 6 2 3 4
    1 1 1 1 1 1 1 1
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    1 1 1 1 1 1 1 1
    4 3 2 5 6 2 3 4
    """

    assert Xadrez.contabiliza_pecas(entrada) == {16, 4, 4, 4, 2, 2}
  end

  test "Produzir string de saída a partir da tupla" do
    assert Xadrez.gera_string({0, 0, 0, 0, 0, 0}) ==
             """
             Peão: 0 peça(s)
             Bispo: 0 peça(s)
             Cavalo: 0 peça(s)
             Torre: 0 peça(s)
             Rainha: 0 peça(s)
             Rei: 0 peça(s)
             """
  end
end
