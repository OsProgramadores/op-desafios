defmodule FuncionariosTest do
  use ExUnit.Case
  doctest Funcionarios

  test "Teste do site" do
    json = """
    {
      "funcionarios":[
          {
              "id":0,
              "nome":"Marcelo",
              "sobrenome":"Silva",
              "salario":3200.00,
              "area":"SM"
          },
          {
              "id":1,
              "nome":"Washington",
              "sobrenome":"Ramos",
              "salario":2700.00,
              "area":"UD"
          },
          {
              "id":2,
              "nome":"Sergio",
              "sobrenome":"Pinheiro",
              "salario":2450.00,
              "area":"SD"
          },
          {
              "id":3,
              "nome":"Bernardo",
              "sobrenome":"Costa",
              "salario":3700.00,
              "area":"SM"
          },
          {
              "id":4,
              "nome":"Cleverton",
              "sobrenome":"Farias",
              "salario":2750.00,
              "area":"SD"
          },
          {
              "id":5,
              "nome":"Abraão",
              "sobrenome":"Campos",
              "salario":2550.00,
              "area":"SD"
          },
          {
              "id":6,
              "nome":"Letícia",
              "sobrenome":"Farias",
              "salario":2450.00,
              "area":"UD"
          },
          {
              "id":7,
              "nome":"Fernando",
              "sobrenome":"Ramos",
              "salario":2450.00,
              "area":"SD"
          },
          {
              "id":8,
              "nome":"Marcelo",
              "sobrenome":"Farias",
              "salario":2550.00,
              "area":"UD"
          },
          {
              "id":9,
              "nome":"Fabio",
              "sobrenome":"Souza",
              "salario":2750.00,
              "area":"SD"
          },
          {
              "id":10,
              "nome":"Clederson",
              "sobrenome":"Oliveira",
              "salario":2500.00,
              "area":"SD"
          }
      ],
      "areas":[
          {
              "codigo":"SD",
              "nome":"Desenvolvimento de Software"
          },
          {
              "codigo":"SM",
              "nome":"Gerenciamento de Software"
          },
          {
              "codigo":"UD",
              "nome":"Designer de UI/UX"
          }
      ]
    }
    """

    assert Funcionarios.constroi_string_salarios(json) ==
             String.trim("""
             global_max|Bernardo Costa|3700.00
             global_min|Sergio Pinheiro|2450.00
             global_min|Letícia Farias|2450.00
             global_min|Fernando Ramos|2450.00
             global_avg|2731.82
             """)
  end
end
