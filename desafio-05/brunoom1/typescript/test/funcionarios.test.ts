import { join } from 'path';

import {
  Funcionario,
  FuncionariosDB
} from './../lib/interfaces';

import {
  lerArquivoFuncionarios
} from './../lib/arquivos';

import {
  funcionariosComMaiorSalario,
  funcionariosComMenorSalario,
  funcionariosComMaiorSalarioPorArea,
  funcionariosComMenorSalarioPorArea,
  funcionariosMaiorSalarioPorSobrenome,
  calcularSalarioMedio,
  calcularSalarioMedioPorArea,
  areaComMaiorNumeroDeFuncionarios,
  areaComMenorNumeroDeFuncionarios,
  listarSobrenomes,
  listarMaioresSalariosPorSobrenome,
  totalDeFuncionariosPorSobrenome,
  formataSalario,
} from './../lib/funcionario';

import {
  printGeral,
  printInfos,
  printNome
} from './../lib/print';


const getListaFuncionarios = (): Funcionario[] => {
  return getDb().funcionarios;
}

const getDb = (): FuncionariosDB  => {
  return lerArquivoFuncionarios(join(__dirname, '..', 'funcionarios.json'))
}

describe("Função funcionario com maior salário", () => {

  test('Testar calculo do salário médio', () => {
    expect(calcularSalarioMedio(getListaFuncionarios())).toEqual("2731.82");
  });

  test('Testar um funcionario com menor salario', () => {
    expect<Funcionario>(
      funcionariosComMenorSalario(getListaFuncionarios())[0]
    ).toMatchObject({
      "id":2,
      "nome":"Sergio",
      "sobrenome":"Pinheiro",
      "salario":2450.00,
      "area":"SD"
    })
  });

  test('Testar mais de um funcionario com menor salario igual', () => {
    const _funcionarios = getListaFuncionarios();
    expect(funcionariosComMenorSalario(_funcionarios).length).toEqual(3)
  });

  test('Testar mais de um funcionario com maior salario igual', () => {
    const _funcionarios = getListaFuncionarios();

    _funcionarios.push({
      area: 'SM',
      id: 4,
      nome: 'Ana',
      sobrenome: 'Maria',
      salario: 3700
    });

    expect(funcionariosComMaiorSalario(_funcionarios).length).toEqual(2);
  });

  test('Testar um funcionario com maior salario', () => {
    expect<Funcionario>(
      {
        "id":3,
        "nome":"Bernardo",
        "sobrenome":"Costa",
        "salario":3700.00,
        "area":"SM"
    }).toMatchObject(funcionariosComMaiorSalario(getListaFuncionarios())[0])
  });

});

test("Testar função de imprimir nome", () => {
  const nome = 'Gabriel';
  const sobrenome = 'Mendonça';

  expect(printNome({id: 1, area: 'SD', salario: 0, nome, sobrenome}))
    .toEqual(`${nome} ${sobrenome}`);
});

test("Testar formatação do salário", () => {
  const salario: number = 10.234;
  expect(formataSalario(salario)).toEqual("10.23");
});

describe("Testar funcao de filtro por área", () => {

  test('Testar maior salario por área', () => {
    const listaFuncionarios = getListaFuncionarios();
    const funcionarios = funcionariosComMaiorSalarioPorArea(listaFuncionarios, 'SD');

    expect(funcionarios.length).toEqual(2);
    expect(funcionarios[0].nome).toEqual('Cleverton');
    expect(funcionarios[0].salario).toEqual(2750);
  });

  test('Testar menor salario por área', () => {
    const listaFuncionarios = getListaFuncionarios();
    const funcionarios = funcionariosComMenorSalarioPorArea(listaFuncionarios, 'SM');

    expect(funcionarios.length).toEqual(1);
    expect(funcionarios[0].nome).toEqual('Marcelo');
    expect(funcionarios[0].salario).toEqual(3200);
  });

  test("Testar area com maior numero de funcionarios", () => {
    const db = getDb();
    expect(areaComMaiorNumeroDeFuncionarios(db))
    .toEqual(
      [
        {
          codigo: 'SD',
          total: 6
        }
      ]
    );
  });

  test("Testar area com menor numero de funcionarios", () => {
    const db = getDb();
    expect(areaComMenorNumeroDeFuncionarios(db))
      .toEqual([
        {
          codigo: 'SM',
          total: 2
        }
      ]);
  });

  test("Testar media por area", () => {
    const _funcionarios = getListaFuncionarios();

    const result = calcularSalarioMedioPorArea(_funcionarios, 'SD');
    expect(parseInt(result.toString()))
      .toEqual(2575);
  })

});

describe ("Sobrenomes", () => {
  test('Testar funcação maior salário com o mesmo sobrenome', () => {
    const funcs = getListaFuncionarios();
    const maiores = funcionariosMaiorSalarioPorSobrenome(funcs, 'Oliveira');

    expect(maiores.length).toBe(1);
    expect(maiores[0].nome).toEqual("Clederson");
  });

  test("Testar funcao de busca dos sobrenomes", () => {
    const sobrenomes = [
      "Silva",
      "Ramos",
      "Pinheiro",
      "Costa",
      "Farias",
      "Campos",
      "Souza",
      "Oliveira"
    ];

    expect(listarSobrenomes(getListaFuncionarios()))
      .toEqual(sobrenomes);
  });

  test("Testar contagem de funcionários por sobrenome", () => {
    expect(totalDeFuncionariosPorSobrenome(getListaFuncionarios(), 'Farias'))
      .toEqual(3);
  });

  test("Testar maiores valores por sobrenome", () => {

    const sobreNomes = listarMaioresSalariosPorSobrenome(getListaFuncionarios());

    expect(sobreNomes)
    .toMatchObject([
      {
        sobrenome: 'Ramos',
        funcionarios: [
          {
            id:1,
            nome:"Washington",
            sobrenome:"Ramos",
            salario:2700.00,
            area:"UD"
          }
        ]
      },
      {
        sobrenome: 'Farias',
        funcionarios: [
          {
            id:4,
            nome:"Cleverton",
            sobrenome:"Farias",
            salario:2750.00,
            area:"SD"
          }
        ]
      }
    ]);
  })
});

describe ("Testar banco de funcionarios", () => {

  const file_name = join(__dirname, '..', 'funcionarios.json');
  const funcionarios = lerArquivoFuncionarios(file_name);

  test("Testar se o objeto contém areas", () => {
    expect(funcionarios.areas).toBeInstanceOf(Array);
  });

  test("Testar se o objeto contém funcionarios", () => {
    expect(funcionarios.funcionarios).toBeInstanceOf(Array);
  });

});

test('Testar prints dos dados de usuários', () => {
  const result =
`global_max|Bernardo Costa|3700.00
global_min|Sergio Pinheiro|2450.00
global_min|Letícia Farias|2450.00
global_min|Fernando Ramos|2450.00
global_avg|2731.82`;

  expect(printInfos(getListaFuncionarios())).toEqual(result);
});

test('Testar prints de dados gerais', () => {
  const templ =
`global_max|Bernardo Costa|3700.00
global_min|Sergio Pinheiro|2450.00
global_min|Letícia Farias|2450.00
global_min|Fernando Ramos|2450.00
global_avg|2731.82
area_max|Gerenciamento de Software|Bernardo Costa|3700.00
area_min|Gerenciamento de Software|Marcelo Silva|3200.00
area_avg|Gerenciamento de Software|3450.00
area_max|Designer de UI/UX|Washington Ramos|2700.00
area_min|Designer de UI/UX|Letícia Farias|2450.00
area_avg|Designer de UI/UX|2566.67
area_max|Desenvolvimento de Software|Cleverton Farias|2750.00
area_max|Desenvolvimento de Software|Fabio Souza|2750.00
area_min|Desenvolvimento de Software|Sergio Pinheiro|2450.00
area_min|Desenvolvimento de Software|Fernando Ramos|2450.00
area_avg|Desenvolvimento de Software|2575.00
most_employees|Desenvolvimento de Software|6
least_employees|Gerenciamento de Software|2
last_name_max|Ramos|Washington Ramos|2700.00
last_name_max|Farias|Cleverton Farias|2750.00`;

const printed = printGeral(getDb());
  expect(printed).toContain(templ);
});