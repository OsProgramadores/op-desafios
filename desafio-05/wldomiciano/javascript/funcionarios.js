if (!process.argv[2]) return;

const fs = require('fs');
const data = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));

function getMenorEMenorSalario(funcionarios) {
  const { menor, maior } = funcionarios.reduce(
    (acc, e) => {
      acc.maior = acc.maior > e.salario ? acc.maior : e.salario;
      acc.menor = acc.menor < e.salario ? acc.menor : e.salario;
      return acc;
    },
    { maior: undefined, menor: undefined }
  );

  const temp = {};
  temp.menor = funcionarios.filter(e => e.salario === menor);
  temp.maior = funcionarios.filter(e => e.salario === maior);
  temp.media =
    funcionarios.reduce((acc, e) => acc + e.salario, 0) / funcionarios.length;
  return temp;
}

function print(dados, prefix = '', infix = '') {
  if (infix !== '') {
    const nomeArea = data.areas.filter(e => dados.maior[0].area === e.codigo)[0]
      .nome;
    infix = `${nomeArea}|`;
  }

  dados.menor.forEach(e =>
    console.log(`${prefix}_min|${infix}${e.nome} ${e.sobrenome}|${e.salario}`)
  );
  dados.maior.forEach(e =>
    console.log(`${prefix}_max|${infix}${e.nome} ${e.sobrenome}|${e.salario}`)
  );
  console.log(`${prefix}_avg|${infix}${dados.media.toFixed(2)}`);
}

const geral = getMenorEMenorSalario(data.funcionarios);
print(geral, 'global');

const funcPorArea = data.areas.map(area => ({
  area: area.nome,
  funcionarios: data.funcionarios.filter(func => func.area === area.codigo)
}));
funcPorArea.forEach(e =>
  print(getMenorEMenorSalario(e.funcionarios), 'area', 'area')
);

const maxFuncPorArea = Math.max(...funcPorArea.map(e => e.funcionarios.length));
const minFuncPorArea = Math.min(...funcPorArea.map(e => e.funcionarios.length));
const areasComMenosFuncs = funcPorArea
  .filter(e => e.funcionarios.length === minFuncPorArea)
  .map(e => e.area);
const areasComMaisFuncs = funcPorArea
  .filter(e => e.funcionarios.length === maxFuncPorArea)
  .map(e => e.area);

areasComMenosFuncs.forEach(e =>
  console.log(`least_employees|${e}|${minFuncPorArea}`)
);
areasComMaisFuncs.forEach(e =>
  console.log(`most_employees|${e}|${maxFuncPorArea}`)
);

let sobrenomes = [...new Set(data.funcionarios.map(e => e.sobrenome))];
const funcPorSobrenome = sobrenomes.map(sobrenome => ({
  sobrenome: sobrenome,
  funcionarios: data.funcionarios.filter(func => func.sobrenome === sobrenome)
}));

funcPorSobrenome.forEach(e =>
  getMenorEMenorSalario(e.funcionarios).maior.forEach(f =>
    console.log(
      `last_name_max|${e.sobrenome}|${f.nome} ${f.sobrenome}|${f.salario}`
    )
  )
);
