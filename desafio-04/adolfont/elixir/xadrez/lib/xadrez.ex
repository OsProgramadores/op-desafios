defmodule Xadrez do
  def contabiliza_pecas(tabuleiro) do
    tabuleiro
    |> String.trim()
    |> String.split(["\n", " "])
    |> Enum.frequencies()
    |> cria_tupla_resultante()
  end

  defp cria_tupla_resultante(mapa) do
    {obtem(mapa, 1), obtem(mapa, 2), obtem(mapa, 3), obtem(mapa, 4), obtem(mapa, 5),
     obtem(mapa, 6)}
  end

  defp obtem(mapa, valor) do
    Map.get(mapa, "#{valor}", 0)
  end

  def gera_string({peao, bispo, cavalo, torre, rainha, rei}) do
    """
    Peão: #{peao} peça(s)
    Bispo: #{bispo} peça(s)
    Cavalo: #{cavalo} peça(s)
    Torre: #{torre} peça(s)
    Rainha: #{rainha} peça(s)
    Rei: #{rei} peça(s)
    """
  end
end

# Use
# mix run
# para executar e gerar a saída

entrada_1 = """
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0
0 0 0 1 1 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
"""

entrada_1
|> Xadrez.contabiliza_pecas()
|> Xadrez.gera_string()
|> IO.puts()

entrada_2 = """
4 3 2 5 6 2 3 4
1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
4 3 2 5 6 2 3 4
"""

entrada_2
|> Xadrez.contabiliza_pecas()
|> Xadrez.gera_string()
|> IO.puts()
