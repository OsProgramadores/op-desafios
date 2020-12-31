"use strict";

/**
 * @typedef Funcionario
 * @property {number} id - Identificação numérica do funcionario
 * @property {string} nome - Nome do funcionário
 * @property {string} sobrenome - Sobrenome do funcionário
 * @property {number} salario - Salário do funcionário
 * @property {string} area - Área do funcionário
 */

/**
 * @typedef Area
 * @property {string} codigo - Código da área
 * @property {string} nome - Nome da área
 */

/**
 * Classe responsável por coletar e armazenar as estatísticas dos funcionários.
 */
class Stats {
  constructor() {
    /**
     * Estatísticas globais dos funcionários.
     *
     * @type GlobalStats
     */
    this.global = new GlobalStats();
    /**
     * Estatísticas de funcionários por área.
     *
     * @type {object.<string, GlobalStats>}
     */
    this.by_area = {};
    /**
     * Estatísticas de funcionários por quantidade de empregados.
     *
     * @type {object.<string, number>}
     */
    this.by_employees = {};
    /**
     * Estatísticas de funcionários por sobrenome.
     *
     * @type {object.<string, MaxStats>}
     */
    this.by_lastname = {};
  }

  /**
   * Atualiza os dados a partir de um funcionário.
   * Esta função simplesmente chama as funções de cada estatística responsáveis
   * pela atualização de seus dados. Algumas destas são métodos da própria
   * classe pois precisam ser instanciadas por chave antes de serem atualizadas.
   *
   * @param {Funcionario} func - O funcionário a ser testado.
   */
  update(func) {
    this.global.update(func);
    this.byArea(func);
    this.byEmployees(func);
    this.byLastName(func);
  }

  /**
   * Atualiza as estatísticas por área.
   * Verifica se há uma entrada daquela área no objeto, instanciando uma
   * pra ele em caso negativo. Logo após, já tendo uma entrada, executa o
   * método responsável por atualizá-la.
   *
   * @param {Funcionario} func - O funcionário a ser testado.
   */
  byArea(func) {
    let a = func.area;

    if (this.by_area[a] == null) {
      this.by_area[a] = new GlobalStats();
    }
    this.by_area[a].update(func);
  }

  /**
   * Atualiza a estatística por quantidade de funcionários.
   * Caso não haja entrada, este funcionário é o primeiro dela: Insira uma
   contendo 1. Caso já haja, apenas incremente seu valor.
   *
   * @param {Funcionario} func - O funcionário a ser testado.
   */
  byEmployees(func) {
    let a = func.area;

    if (this.by_employees[a] == null) {
      this.by_employees[a] = 1;
    } else {
      this.by_employees[a] += 1;
    }
  }

  /**
   * Atualiza a estatística por sobrenome.
   * Verifica se há uma entrada daquela área no objeto, instanciando-a caso
   * negativo. Logo após, já tendo uma entrada, executa o método responsável por
   * atualizá-la.
   *
   * @param {Funcionario} func - O funcionário a ser testado.
   */
  byLastName(func) {
    let ln = func.sobrenome;

    if (this.by_lastname[ln] == null) {
      this.by_lastname[ln] = new MaxStats();
    }
    this.by_lastname[ln].update(func);
  }

  /**
   * Obtém as áreas com a maior e menor quantidade de funcionários.
   *
   * @returns {object} MinMax
   * @returns {number} MinMax.min - Menor quantidade de empregados
   * @returns {number} MinMax.max - Maior quantidade de empregados
   * @returns {array.<string>} MinMax.list_min - Áreas contendo a menor quantidade
   * @returns {array.<string>} MinMax.list_max - Áreas contendo a maior quantidade
   */
  byEmployeesMinMax() {
    // Declara todas as variáveis responsáveis pelos valores mínimos, máximos
    // e a lista de áreas contendo cada.
    let min = Math.min();
    let max = Math.max();
    let listMin = [];
    let listMax = [];

    // Pra fins de praticidade, declara uma variável apontando pro objeto
    // contendo os funcionários.
    let e = this.by_employees;

    // Itera por cada área (chave) no objeto previamente apontado.
    for (let area in e) {
      // Tendo a área, obtém a quantidade (valor).
      let ac = e[area];

      if (ac < min) {
        // Se a quantidade for menor que a mínima:
        // - Faça a mínima ser a quantidade desta área.
        min = ac;
        // - Todas as áreas anteriores tinham menor quantidade de funcionários,
        //   portanto apenas sobrescreva a lista com uma array contendo apenas
        //   esta área.
        listMin = [area];
      } else if (ac > max) {
        // O mesmo pro anterior, apenas com o valor máximo e comparação
        // invertida (duh).
        max = ac;
        listMax = [area];
      } else if (ac === min) {
        // Se a quantidade for idêntica à mínima:
        // - Insira a área na lista.
        listMin.push(area);
      } else if (ac === max) {
        // Mesma regra pro máximo.
        listMax.push(area);
      }
    }

    // Retorna um objeto contendo os valores máximos, mínimos e as áreas
    // contendo tais quantidades. Retorno um objeto ao invés de uma array pra
    // fins de legibilidade.
    return {
      min: min,
      max: max,
      list_min: listMin,
      list_max: listMax
    };
  }
}

/**
 * Classe responsável por coletar e armazenar as estatísticas globais dos
 * funcionários, como funcionários com menores e maiores salários, a soma
 * destes e sua quantidade total. Por serem os mesmos dados coletados nas
 * estatísticas por área, esta classe também é utilizada como valor nesta.
 */
class GlobalStats {
  constructor() {
    /**
     * O menor salário.
     *
     * @type number
     */
    this.min = Math.min();
    /**
     * O maior salário.
     *
     * @type number
     */
    this.max = Math.max();
    /**
     * A lista de funcionários com o menor salário.
     *
     * @type array.<Funcionario>
     */
    this.list_min = [];
    /**
     * A lista de funcionários com o maior salário.
     *
     * @type array.<Funcionario>
     */
    this.list_max = [];
    /**
     * A soma de todos os salários.
     *
     * @type number
     */
    this.sum = 0;
    /**
     * A quantidade de funcionários.
     *
     * @type number
     */
    this.count = 0;
  }

  /**
   * Atualiza os dados a partir de um funcionário.
   *
   * @param {Funcionario} func - O funcionário a ser testado.
   */
  update(func) {
    // Soma seu salário à soma.
    this.sum += func.salario;
    // Incrementa a quantidade de funcionários.
    this.count += 1;

    if (func.salario < this.min) {
      // Se o salário for menor que o mínimo:
      // - Faça o mínimo ser o salário deste funcionário.
      this.min = func.salario;
      // - Todos os funcionários anteriores tinham salários maiores que
      //   este, portanto apenas sobrescreva a lista com uma array contendo
      //   apenas este funcionário.
      this.list_min = [func];
    } else if (func.salario > this.max) {
      // O mesmo pro anterior, apenas com o salário máximo e comparação
      // invertida.
      this.max = func.salario;
      this.list_max = [func];
    } else if (func.salario === this.min) {
      // Se o salário for idêntico ao menor:
      // - Insira-o na lista.
      this.list_min.push(func);
    } else if (func.salario === this.max) {
      // Mesma regra pro maior.
      this.list_max.push(func);
    }
  }

  /**
   * Obtém o salário médio dos funcionários.
   *
   * @returns {number} O salário médio dos funcionários
   */
  average() {
    return (this.sum / this.count).toFixed(2);
  }
}

/**
 * Classe responsável por coletar e armazenar as estatísticas por sobrenome dos
 * funcionários. Coleta apenas as estatísticas acerca do maior salário.
 */
class MaxStats {
  constructor() {
    /**
     * O maior salário.
     *
     * @type number
     */
    this.max = Math.max();
    /**
     * A lista de funcionários com o maior salário.
     *
     * @type array.<Funcionario>
     */
    this.list = [];
    /**
     * A quantidade de funcionários.
     *
     * @type number
     */
    this.count = 0;
  }

  /**
   * Atualiza os dados a partir de um funcionário.
   *
   * @param {Funcionario} func - O funcionário a ser testado.
   */
  update(func) {
    // Pra fins de praticidade, declara uma variável contendo o salário do
    // funcionário.
    let s = func.salario;
    // Incrementa a quantidade de funcionários.
    this.count += 1;

    if (s > this.max) {
      // Se o salário for maior que o máximo:
      // - Faça a mínima ser a quantidade desta área.
      this.max = s;
      // - Todos os funcionários anteriores tinham salários menores que
      //   este, portanto apenas sobrescreva a lista com uma array contendo
      //   apenas este funcionário.
      this.list = [func];
    } else if (s === this.max) {
      // Se o salário for idêntico ao maior:
      // - Insira-o na lista.
      this.list.push(func);
    }
  }
}

/**
 * Lê o arquivo cujo caminho é o primeiro argumento do script. É uma função
 * distinta para fins de compatibilidade.
 *
 * @returns {string} O conteúdo do arquivo lido
 */
function getFile() {
  if (typeof snarf === "function") {
    return snarf(scriptArgs[0]);
  } else {
    return require("fs").readFileSync(process.argv[2]);
  }
}

/**
 * Obtém o nome da área a partir de seu código.
 *
 * @param {Area[]} areas - Lista de áreas
 * @param {string} code - Código da área
 * @returns {string} Nome da área
 */
function areaNameByCode(areas, code) {
  return areas.find(it => it.codigo === code).nome;
}

// Lê o arquivo JSON
let res = JSON.parse(getFile());
// Instancia a classe responsável pelas estatísticas
let stats = new Stats();

// Para cada funcionário, atualiza as estatísticas
for (let func of res.funcionarios) {
  stats.update(func);
}

// === Global ===
// Obtém e arrendonda o salário máximo
let max = stats.global.max.toFixed(2);

// Imprime cada funcionário na lista de máximos
for (let func of stats.global.list_max)
  console.log(`global_max|${func.nome} ${func.sobrenome}|${max}`);

// Obtém e arrendonda o salário mínimo
let min = stats.global.min.toFixed(2);

// Imprime cada funcionário na lista de mínimo
for (let func of stats.global.list_min)
  console.log(`global_min|${func.nome} ${func.sobrenome}|${min}`);

// Imprime o salário médio dos funcionários
console.log(`global_avg|${stats.global.average()}`);

// === Area ===
// Itera por cada área, obtendo seu código
for (let areaCode in stats.by_area) {
  // Obtém nome da área
  let areaName = areaNameByCode(res.areas, areaCode);
  // Obtém estatísticas da área
  let area = stats.by_area[areaCode];

  // Obtém e arrendonda o salário máximo
  let max = area.max.toFixed(2);

  // Imprime cada funcionário na lista de máximos
  for (let func of area.list_max)
    console.log(`area_max|${areaName}|${func.nome} ${func.sobrenome}|${max}`);

  // Obtém e arrendonda o salário mínimo
  let min = area.min.toFixed(2);

  // Imprime cada funcionário na lista de mínimo
  for (let func of area.list_min)
    console.log(`area_min|${areaName}|${func.nome} ${func.sobrenome}|${min}`);

  // Imprime salário médio dos funcionários
  console.log(`area_avg|${areaName}|${area.average()}`);
}

// === Empregados ===
// Obtém minmax das estatísticas por quantidade de empregados
let minmax = stats.byEmployeesMinMax();

// Itera por cada área com quantidade máxima de funcionários
for (let area of minmax.list_max) {
  // Obtém nome da área
  let areaName = areaNameByCode(res.areas, area);

  // Imprime área
  console.log(`most_employees|${areaName}|${minmax.max}`);
}

// Itera por cada área com quantidade mínima de funcionários
for (let area of minmax.list_min) {
  // Obtém nome da área
  let areaName = areaNameByCode(res.areas, area);

  // Imprime área
  console.log(`least_employees|${areaName}|${minmax.min}`);
}

// === Sobrenome ===
// Itera por cada sobrenome
for (let lastname in stats.by_lastname) {
  // Obtém estatísticas
  let st = stats.by_lastname[lastname];

  // Obtém e arredonda o salário máximo
  let max = st.max.toFixed(2);

  // Se houver mais de um funcionário...
  if (st.count > 1)
    // Imprima cada funcionário.
    for (let func of st.list)
      console.log(
        `last_name_max|${lastname}|${func.nome} ${func.sobrenome}|${max}`
      );
}
