import {
  CodigoAreaEnum,
  Funcionario,
  FuncionariosDB,
  RetornoAreaComMaiorNumeroDeFuncionarios,
  ReturnListaMaioresSalariosPorSobrenome
} from "./interfaces";

export const funcionariosComMaiorSalario = (funcionarios: Funcionario[]): Funcionario[] => {
  let maiorSalario = 0;
  return funcionarios.map(funcionarios => {
    if (funcionarios.salario > maiorSalario) {
      maiorSalario = funcionarios.salario;
    }
    return funcionarios;
  }).filter(funcionarios => {
    return funcionarios.salario === maiorSalario;
  });
}

export const funcionariosComMenorSalario = (funcionarios: Funcionario[]): Funcionario[] => {
  let menorSalario = 999999999;
  return funcionarios.map(func => {
    if (func.salario < menorSalario) {
      menorSalario = func.salario;
    }
    return func;
  }).filter(func => {
    return func.salario === menorSalario;
  });
}

export const funcionariosComMaiorSalarioPorArea = (funcionarios: Funcionario[], codigo: CodigoAreaEnum): Funcionario[] => {
  const funcsDaArea = funcionarios.filter(func => func.area === codigo);
  return  funcionariosComMaiorSalario(funcsDaArea);
}

export const funcionariosComMenorSalarioPorArea = (funcionarios: Funcionario[], codigo: CodigoAreaEnum): Funcionario[] => {
  const funcsDaArea = funcionarios.filter(func => func.area === codigo);
  return  funcionariosComMenorSalario(funcsDaArea);
}

export const funcionariosMaiorSalarioPorSobrenome = (funcionarios: Funcionario[], sobrenome: string): Funcionario[] => {
  return funcionariosComMaiorSalario(funcionarios.filter(func => func.sobrenome === sobrenome));
}

export const calcularSalarioMedio = (funcionarios: Funcionario[]): string => {
  let soma = 0;
  let total = 0;
  funcionarios.forEach((func) => {
    soma += func.salario;
    total += 1;
  });

  const result = soma / total;

  return formataSalario(result);
}

export const calcularSalarioMedioPorArea = (funcionarios: Funcionario[], codigo: CodigoAreaEnum): string => {
  const funcs = funcionarios.filter(func => func.area === codigo)
  return calcularSalarioMedio(funcs);
}

export const areaComMaiorNumeroDeFuncionarios = (data: FuncionariosDB): RetornoAreaComMaiorNumeroDeFuncionarios[] => {

  let maiorNumeroFuncionarios = 0;

  const count = data.areas.map(area => {
    const funcs = data.funcionarios.filter(func => func.area === area.codigo);

    if (funcs.length > maiorNumeroFuncionarios) {
      maiorNumeroFuncionarios = funcs.length;
    }

    return {
      codigo: area.codigo,
      total: funcs.length
    };
  });

  return count.filter(c => c.total === maiorNumeroFuncionarios);
}

export const areaComMenorNumeroDeFuncionarios = (data: FuncionariosDB): RetornoAreaComMaiorNumeroDeFuncionarios[] => {

  let menoNumeroDeFuncionarios = 999999999;

  const count = data.areas.map(area => {
    const funcs = data.funcionarios.filter(func => func.area === area.codigo);

    if (funcs.length < menoNumeroDeFuncionarios) {
      menoNumeroDeFuncionarios = funcs.length;
    }

    return {
      codigo: area.codigo,
      total: funcs.length
    };
  });

  return count.filter(c => c.total === menoNumeroDeFuncionarios);
}

export const listarSobrenomes = (funcionarios: Funcionario[]): string[] => {
  const sobrenomes = [];

  funcionarios.forEach(func => {
    if (sobrenomes.findIndex(s => s === func.sobrenome) === -1) {
      sobrenomes.push(func.sobrenome);
    }
  });

  return sobrenomes;
}

export const totalDeFuncionariosPorSobrenome = (funcionarios: Funcionario[], sobrenome: string): number => {
  return funcionarios.filter(func => func.sobrenome === sobrenome).length;
}

export const listarMaioresSalariosPorSobrenome = (funcionarios: Funcionario[]): ReturnListaMaioresSalariosPorSobrenome[] => {
  const sobrenomes = listarSobrenomes(funcionarios);

  const maiores: ReturnListaMaioresSalariosPorSobrenome[] = [];

  sobrenomes.forEach(sobrenome => {
    if(totalDeFuncionariosPorSobrenome(funcionarios, sobrenome) >= 2) {
      maiores.push({
        sobrenome,
        funcionarios: funcionariosMaiorSalarioPorSobrenome(funcionarios, sobrenome)
      })
    }
  });  

  return maiores;
}

export const formataSalario = (salario: number):string => {
  return salario.toFixed(2);
}
