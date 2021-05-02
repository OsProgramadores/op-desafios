defmodule Funcionarios do
  def maiores_salarios(json) do
    json
    |> Jason.decode!()
    |> Map.get("funcionarios")
    |> lista_salarios(&Enum.max/1)
  end

  def menores_salarios(json) do
    json
    |> Jason.decode!()
    |> Map.get("funcionarios")
    |> lista_salarios(&Enum.min/1)
  end

  def salario_medio(json) do
    lista_funcionarios =
      json
      |> Jason.decode!()
      |> Map.get("funcionarios")

    total =
      lista_funcionarios
      |> Enum.map(fn x -> x["salario"] end)
      |> Enum.sum()

    duas_casas_decimais(total / Enum.count(lista_funcionarios))
  end

  defp duas_casas_decimais(numero) do
    (round(numero * 100) / 100)
    |> :erlang.float_to_binary(decimals: 2)
  end

  defp lista_salarios(lista_funcionarios, funcao) do
    maior_salario =
      lista_funcionarios
      |> Enum.map(fn x -> x["salario"] end)
      |> funcao.()

    Enum.filter(
      lista_funcionarios,
      fn x -> x["salario"] == maior_salario end
    )
  end

  def constroi_string_salarios(json) do
    "#{constroi_string_maiores_salarios(json)}#{constroi_string_menores_salarios(json)}global_avg|#{
      salario_medio(json)
    }"
  end

  defp constroi_string_maiores_salarios(json) do
    maiores_salarios(json)
    |> Enum.map(fn x ->
      """
      global_max|#{x["nome"]} #{x["sobrenome"]}|#{duas_casas_decimais(x["salario"])}
      """
    end)
  end

  defp constroi_string_menores_salarios(json) do
    menores_salarios(json)
    |> Enum.map(fn x ->
      """
      global_min|#{x["nome"]} #{x["sobrenome"]}|#{duas_casas_decimais(x["salario"])}
      """
    end)
  end
end
