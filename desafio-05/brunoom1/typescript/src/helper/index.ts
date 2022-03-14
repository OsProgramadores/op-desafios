import { createReadStream } from "fs";



export const read_input_file_name = (): string => {
  const argv: string[] = process.argv;
  const file_name = argv[argv.length - 1];
  return file_name;
}

interface Area {
  codigo: string;
  nome: string;
}

interface Funcionario {
  id: number;
  nome: string;
  sobrenome: string;
  salario: number;
  area: string;
}

interface Result {
  funcionarios: Funcionario[],
  areas: Area[]
}

interface global_max { sobrenome?: string, nome: string; salario: number };
interface global_min { nome: string; salario: number };
interface global_avg { media: number };
interface area_max { area: string; nome: string; salario: number };
interface area_min { area: string; nome: string; salario: number };
interface area_avg { area: string; salario: number };
interface most_employees { area: string; totalFuncionarios: number };
interface least_employees { area: string; totalFuncionarios: number };
interface last_name_max { sobrenome: string; nome: string; salario: number };

export const openFile = (filename: string): Promise<Result> => {
  return new Promise<Result> ((resolve, reject) => {
    let buffer: string = "";
    createReadStream(filename, {
      autoClose: true,
      emitClose: true,
      encoding: 'utf-8'
    }).on('data', (data) => {
      buffer += data;
    }).on('close', () => {
      resolve(JSON.parse(buffer));
    }).on('error', err => {
      reject(err);
    })
  });
}

const numberFormat = new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'REA' });

const contar_total = (funcionarios: Funcionario[]) => {
  return funcionarios.length;
}

const somar_todos = (funcionarios: Funcionario[]) => {
  let soma: number = 0;
  funcionarios.forEach(funcionario => {
    soma += funcionario.salario;
  });
  return soma;
}

const media_salarial = (funcionarios: Funcionario[]): global_avg => {
  const total = contar_total(funcionarios);
  const soma = somar_todos(funcionarios);

  if (!total) {
    return {
      media: 0
    }
  };

  return {
    media: soma / total
  }
}

const formatNumber = (num: number) => {
  return num.toFixed(2);
}

const buscar_quem_mais_recebe = (funcionarios: Funcionario[]): global_max[] => {
  let maiorSalario = 0;
  funcionarios.forEach(funcionario => {
    if (funcionario.salario > maiorSalario) {
      maiorSalario = funcionario.salario
    }
  })

  return funcionarios
    .filter(funcionario => funcionario.salario === maiorSalario)
    .map(funcionario => ({
      nome: `${funcionario.nome} ${funcionario.sobrenome}`,
      salario: funcionario.salario
    }));
}

const buscar_quem_mais_recebe_2 = (funcionarios: Funcionario[]): Funcionario[] => {
  let maiorSalario = 0;
  funcionarios.forEach(funcionario => {
    if (funcionario.salario > maiorSalario) {
      maiorSalario = funcionario.salario
    }
  })

  return funcionarios
    .filter(funcionario => funcionario.salario === maiorSalario);
}

const buscar_quem_menos_recebe = (funcionarios: Funcionario[]): global_min[] => {
  let menor_salario:number = 9999999;

  funcionarios.forEach(funcionario=> {
    if (funcionario.salario < menor_salario) {
      menor_salario = funcionario.salario;
    }
  });

  return funcionarios.filter(funcionario => {
    return funcionario.salario === menor_salario;
  }).map(funcionario => ({
    nome: `${funcionario.nome} ${funcionario.sobrenome}`,
    salario: funcionario.salario
  }));
}

const buscar_maiores_salarios_por_area = (areas: Area[], funcionarios: Funcionario[]): area_max[] => {
  const areas_result: area_max[] = [];

  areas.forEach(area => {
    const area_funcionarios = funcionarios.filter(funcionario => funcionario.area === area.codigo);
    buscar_quem_mais_recebe(area_funcionarios)
      .map(funcionario => {
        areas_result.push({
          area: area.nome,
          nome: funcionario.nome,
          salario: funcionario.salario
        });
      });
 });

  return areas_result;
}

const buscar_menores_salarios_por_area = (areas: Area[], funcionarios: Funcionario[]): area_min[] => {
  const menores_salarios: area_min[] = [];

  areas.map(area => {
    const funcionarios_da_area = funcionarios.filter(func => func.area === area.codigo);
    buscar_quem_menos_recebe(funcionarios_da_area).map(funcionario => {
      menores_salarios.push({
        area: area.nome,
        nome: funcionario.nome,
        salario: funcionario.salario
      });
    })
  });

  return menores_salarios;
}

const buscar_media_por_area = (areas: Area[], funcionarios: Funcionario[]): area_avg[] => {
  const areas_result: area_avg[] = [];

  areas.map(area => {
    const funcionarios_da_area = funcionarios.filter(funcionario => funcionario.area === area.codigo);

    areas_result.push({
      area: area.nome,
      salario: media_salarial(funcionarios_da_area).media
    });
  });

  return areas_result;
}

const buscar_area_com_mais_funcionarios = (areas: Area[], funcionarios: Funcionario[]): most_employees[] => {
  let result: most_employees[] = [];

  let maxFuncionarios = 0;

  areas.forEach(area => {
    const numeros_funcionarios = funcionarios.filter(funcionario => funcionario.area === area.codigo).length;
    if (numeros_funcionarios > maxFuncionarios) {
      maxFuncionarios = numeros_funcionarios;
      result = [];
      result.push({
        area: area.nome,
        totalFuncionarios: maxFuncionarios
      });
    } else if( numeros_funcionarios === maxFuncionarios) {
      result.push({
        area: area.nome,
        totalFuncionarios: maxFuncionarios
      });
    }
  });

  return result;
}

const buscar_area_com_menos_funcionarios = (areas: Area[], funcionarios: Funcionario[]): least_employees[] => {
  let result:least_employees[] = [];

  let menor_funcionarios:number = 999999;

  areas.map(area => {
    const total_funcionarios = funcionarios.filter(funcionario => funcionario.area === area.codigo).length;
    if (total_funcionarios < menor_funcionarios) {
      menor_funcionarios = total_funcionarios;
      result = []
      result.push({
        area: area.nome,
        totalFuncionarios: menor_funcionarios
      });
    } else if (total_funcionarios === menor_funcionarios) {
      result.push({
        area: area.nome,
        totalFuncionarios: menor_funcionarios
      });
    }
  });

  return result;
}


const buscar_maiores_salarios_mesmo_sobrenome = (funcionarios: Funcionario[]): last_name_max[] => {
  const result: last_name_max[] = [];

  const funcionariosPorNomes:{ [key: string]:Funcionario[] } = {};

  funcionarios.forEach(funcionario => {
    if (funcionario.sobrenome === '') {
      return;
    }

    if (!funcionariosPorNomes[funcionario.sobrenome]) {
      funcionariosPorNomes[funcionario.sobrenome] = [];
    }
    funcionariosPorNomes[funcionario.sobrenome].push(funcionario);
  });

  for(const sobrenome in funcionariosPorNomes) {
    if (funcionariosPorNomes[sobrenome].length > 1) {
      const funcionarios = funcionariosPorNomes[sobrenome];

      buscar_quem_mais_recebe_2(funcionarios)
        .map(func => {
          result.push({
            sobrenome: func.sobrenome,
            nome: func.nome,
            salario: func.salario
          })
        })
    }
  }

  return result;
}

export const mensure = (data: Result) => {

  buscar_quem_mais_recebe(data.funcionarios).map(result => {
    console.log(`global_max|${result.nome}|${formatNumber(result.salario)}`);
  });

  buscar_quem_menos_recebe(data.funcionarios).map(result => {
    console.log(`global_min|${result.nome}|${formatNumber(result.salario)}`);
  });

  console.log(`media_avg|${formatNumber(media_salarial(data.funcionarios).media)}`);

  buscar_maiores_salarios_por_area(data.areas, data.funcionarios).map(result => {
    console.log(`area_max|${result.area}|${result.nome}|${formatNumber(result.salario)}`);
  });

  buscar_menores_salarios_por_area(data.areas, data.funcionarios).map(result => {
    console.log(`area_min|${result.area}|${result.nome}|${formatNumber(result.salario)}`);
  });

  buscar_media_por_area(data.areas, data.funcionarios).map(result => {
    console.log(`area_avg|${result.area}|${formatNumber(result.salario)}`);
  });

  buscar_area_com_mais_funcionarios(data.areas, data.funcionarios).map(result => {
    console.log(`most_employees|${result.area}|${result.totalFuncionarios}`);
  });

  buscar_area_com_menos_funcionarios(data.areas, data.funcionarios).map(result => {
    console.log(`least_employees|${result.area}|${result.totalFuncionarios}`);
  });

  buscar_maiores_salarios_mesmo_sobrenome(data.funcionarios).map(result => {
    console.log(`last_name_max|${result.sobrenome}|${result.nome}|${formatNumber(result.salario)}`);
  });

}