import {
  Funcionario,
  FuncionariosDB
} from './interfaces';

import {
  funcionariosComMaiorSalario,
  funcionariosComMenorSalario,
  calcularSalarioMedio,
  formataSalario,
  funcionariosComMaiorSalarioPorArea,
  funcionariosComMenorSalarioPorArea,
  calcularSalarioMedioPorArea,
  areaComMaiorNumeroDeFuncionarios,
  areaComMenorNumeroDeFuncionarios,
  listarMaioresSalariosPorSobrenome
} from './funcionario'

export const printNome = (funcionario: Funcionario) => {
  return `${funcionario.nome} ${funcionario.sobrenome}`;
}

export const printInfos = (funcs: Funcionario[]): string => {

  const maiores = funcionariosComMaiorSalario(funcs);
  const menores = funcionariosComMenorSalario(funcs);
  const media   = calcularSalarioMedio(funcs);

  const prints = [
    ...maiores.map(func => `global_max|${printNome(func)}|${formataSalario(func.salario)}`),
    ...menores.map(func => `global_min|${printNome(func)}|${formataSalario(func.salario)}`),
    `global_avg|${media}`
  ];

  return prints.join("\n");
}

export const printGeral = (data: FuncionariosDB): string => {

  const most_employees = areaComMaiorNumeroDeFuncionarios(data);
  const least_employees = areaComMenorNumeroDeFuncionarios(data);

  const area_most_employee = data.areas.filter(area => area.codigo === most_employees[0].codigo);
  const area_least_employee = data.areas.filter(area => area.codigo === least_employees[0].codigo);

  const funcionarios_por_sobrenome = listarMaioresSalariosPorSobrenome(data.funcionarios);

  const stringData: string[] = [

    printInfos(data.funcionarios),

    data.areas.map(area => {

      const maior_salario_por_area = funcionariosComMaiorSalarioPorArea(data.funcionarios, area.codigo);
      const menor_salario_por_area = funcionariosComMenorSalarioPorArea(data.funcionarios, area.codigo);
      const area_avg = calcularSalarioMedioPorArea(data.funcionarios, area.codigo);

      return [
        ...maior_salario_por_area.map(func => {
          return `area_max|${area.nome}|${printNome(func)}|${formataSalario(func.salario)}`;
        }),
        ...menor_salario_por_area.map(func => {
          return `area_min|${area.nome}|${printNome(func)}|${formataSalario(func.salario)}`;
        }),
        `area_avg|${area.nome}|${area_avg}`
      ].join("\n")

    }).join("\n"),

    `most_employees|${area_most_employee[0].nome}|${most_employees[0].total}`,

    `least_employees|${area_least_employee[0].nome}|${least_employees[0].total}`,

    funcionarios_por_sobrenome.map(nome => {
      return nome.funcionarios.map(func => {
        return `last_name_max|${nome.sobrenome}|${printNome(func)}|${formataSalario(func.salario)}`;
      });
    }).join("\n")
  ];
  return stringData.join("\n");
}