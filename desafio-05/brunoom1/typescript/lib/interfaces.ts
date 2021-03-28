export type CodigoAreaEnum = string[2];

export interface Funcionario {
  id: number,
  nome: string,
  sobrenome: string,
  salario: number,
  area: CodigoAreaEnum;
};

export interface Area {
  codigo: CodigoAreaEnum;
  nome: string;
};

export interface FuncionariosDB {
  funcionarios: Funcionario[],
  areas: Area[]
};

export interface RetornoAreaComMaiorNumeroDeFuncionarios {
  codigo: CodigoAreaEnum,
  total: number
}

export interface ReturnListaMaioresSalariosPorSobrenome {
  funcionarios: Funcionario[],
  sobrenome: string
};
