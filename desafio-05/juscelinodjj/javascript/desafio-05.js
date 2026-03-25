const fs = require("fs");
const JSONStream = require("JSONStream");
const eventStream = require("event-stream");

const EMPLOYEES_LAST_NAME = {};
const SALARIES = [];
const AREAS = [];

const OUTPUT = {
    globalMax: [],
    globalMin: [],
    globalAvg: [],
    area: {},
    areaInfo: []
};

const startStream = file => {
    const stream = fs.createReadStream(file);
    stream.pipe(JSONStream.parse("funcionarios.*"))
        .pipe(eventStream.through(employee => manageData(employee, true)))
    stream.pipe(JSONStream.parse("areas.*"))
        .pipe(eventStream.through(area => manageData(area, false)))
    .on('end', () => end());
};

const manageData = (data, isEmployee) => {
    if (isEmployee) {
        saveDataByLastName(data);
        SALARIES.push(data.salario);
        setGlobal(data, "globalMax", greaterThan);
        setGlobal(data, "globalMin", lessThan);
        setArea(data, "max", greaterThan);
        setArea(data, "min", lessThan);
    } else {
        AREAS.push(data);
    }
};

const saveDataByLastName = employee => {
    const lastName = employee["sobrenome"];
    const lastNameExistIn = EMPLOYEES_LAST_NAME[lastName] ? true : false
    if (!lastNameExistIn) {
        EMPLOYEES_LAST_NAME[lastName] = [];
    }
    EMPLOYEES_LAST_NAME[lastName].push(employee);
};

const greaterThan = (a, b) => a > b;
const lessThan = (a, b) => a < b;

const setGlobal = (currentEmployee, target, fn) => {
    // target = globalMax ou globalMin, tambem representa a chave onde o resultado é armazenado
    const lastEmployee = OUTPUT[target][0];
    if (!lastEmployee) {
        OUTPUT[target] = [currentEmployee];
        return;
    }
    // fn = greaterThan ou lessThan
    const isFn = fn(currentEmployee.salario, lastEmployee.salario);
    const isSameSalary = currentEmployee.salario === lastEmployee.salario;
    if (isFn) {
        OUTPUT[target] = [currentEmployee];
    } else {
        if (isSameSalary) {
            OUTPUT[target].push(currentEmployee);
        }
    }
};

const getGlobal = (target, label) => {
    // target = globalMax ou globalMin, tambem representa a chave onde o resultado é armazenado
    let storage = [];
    let i = OUTPUT[target].length;
    for (i > 0; i--;) {
        const element = `${label}|${OUTPUT[target][i].nome} ${OUTPUT[target][i].sobrenome}|${OUTPUT[target][i].salario.toFixed(2)}`
        storage.push(element);
    }
    const string = storage.join("\n");
    return string;
};

const getGlobalAvg = () => {
    let initialValue = 0;
    let i = SALARIES.length;
    for (i > 0; i--;) {
        initialValue += SALARIES[i];
    }
    const avg = (initialValue / SALARIES.length).toFixed(2);
    const string = "global_avg|" + avg;
    return string;
};

const setArea = (currentEmployee, target, fn) => {
    // target = min ou max, tambem representa a chave onde o resultado é armazenado
    const areaCode = currentEmployee["area"];
    const areaCodeExist = OUTPUT.area[areaCode] ? true : false;
    if (!areaCodeExist) {
        OUTPUT.area[areaCode] = {};
    }
    const targetExist = OUTPUT.area[areaCode][target] ? true : false;
    if (!targetExist) {
        OUTPUT.area[areaCode][target] = [];
    }
    let lastEmployee = OUTPUT.area[areaCode][target][0];
    if (!lastEmployee) {
        OUTPUT.area[areaCode][target] = [currentEmployee];
    } else {
        // fn = greaterThan ou lessThan
        const isFn = fn(currentEmployee.salario, lastEmployee.salario);
        const isSameSalary = currentEmployee.salario === lastEmployee.salario;
        if (isFn) {
            OUTPUT.area[areaCode][target] = [currentEmployee];
        } else {
            if (isSameSalary) {
                OUTPUT.area[areaCode][target].push(currentEmployee);
            }
        }
    }
    // para não duplicar os salarios, esse trecho só é chamado com target min
    if (target === "max") return;
    const avgExist = OUTPUT.area[areaCode].salaries ? true : false;
    if (!avgExist) {
        OUTPUT.area[areaCode].salaries = [];
    }
    OUTPUT.area[areaCode].salaries.push(currentEmployee.salario);
};

const getOccupation = (code) => {
    return AREAS
        .reduce((str, area) => { return area.codigo === code ? area.nome : str; }, "");
};

const getArea = () => {
    const arrayOfObj = Object.entries(OUTPUT.area);
    // 0 = código da area | 1 = objeto contendo max, min e avg da area
    let i = arrayOfObj.length;
    let max = [];
    let min = [];
    let avg = [];
    for (i > 0; i--;) {
        const areaCode = arrayOfObj[i][0];
        const obj = arrayOfObj[i][1]; // max, min e avg
        const employeesMax = obj.max;
        const employeesMin = obj.min;
        const salaries = obj.salaries;
        let iMax = employeesMax.length;
        for (iMax > 0; iMax--;) {
            const employee = employeesMax[iMax];
            const element = `area_max|${getOccupation(areaCode)}|`
                + `${employee.nome} ${employee.sobrenome}|${employee.salario.toFixed(2)}`
            max.push(element);
        }
        let iMin = employeesMin.length;
        for (iMin > 0; iMin--;) {
            const employee = employeesMin[iMin];
            const element = `area_min|${getOccupation(areaCode)}|`
                + `${employee.nome} ${employee.sobrenome}|${employee.salario.toFixed(2)}`
            min.push(element);
        }
        let iSalaries = salaries.length;
        let total = 0;
        for (iSalaries > 0; iSalaries--;) {
            total += salaries[iSalaries]
        }
        const thisAvg = (total / salaries.length).toFixed(2)
        const element = `area_avg|${getOccupation(areaCode)}|${thisAvg}`
        avg.push(element);
        // setando agora para usar posteriomente em getAreaAmount
        // evitando a releitura de OUTPUT.area
        const areaInfo = {areaCode: areaCode, employeeAmount: salaries.length}; // SD, 6 - por exemplo
        OUTPUT.areaInfo.push(areaInfo);

    }
    const string = max.concat(min, avg).join("\n");
    return string;
};

// função getAreaAmount só funciona após a execução da função getArea
// atrelei as duas funções por questão de desempenho
const getAreaAmount = (label, fn) => {
    let area = [];
    let i = OUTPUT.areaInfo.length;
    for (i > 0; i--;) {
        const currentArea = OUTPUT.areaInfo[i];
        const lastArea = area[0];
        if (!lastArea) {
            area = [currentArea];
            continue;
        }
        const isFn = fn(currentArea.employeeAmount, lastArea.employeeAmount);
        const isSameAmount = currentArea.employeeAmount === lastArea.employeeAmount;
        if (isFn) {
            area = [currentArea];
        } else {
            if (isSameAmount) {
                area.push(currentArea);
            }
        }
    }
    const array = area.map(element => `${label}|${getOccupation(element.areaCode)}|${element.employeeAmount}`)
        .join("\n");
    return array;
};

const getLastNameMax = () => {
    const storage = [];
    const arrayOfObj = Object.entries(EMPLOYEES_LAST_NAME);
    // 0 = sobrenome | 1 = array de obj > empregado
    let i = arrayOfObj.length;
    let currentLastName = [];
    for (i > 0; i--;) {
        const amount = arrayOfObj[i][1].length;
        if (amount > 1) {
            const employees = arrayOfObj[i][1];
            let j = employees.length;
            for (j > 0; j--;) {
                const currentEmployee = employees[j];
                const lastEmployee = currentLastName[0];
                if (!lastEmployee) {
                    currentLastName = [currentEmployee];
                    continue;
                }
                const greaterThan = currentEmployee.salario > lastEmployee.salario;
                const isSameSalary = currentEmployee.salario === lastEmployee.salario;
                if (greaterThan) {
                    currentLastName = [currentEmployee];
                } else {
                    if (isSameSalary) {
                        currentLastName.push(currentEmployee);
                    }
                }
            }
            for (const element of currentLastName) {
                storage.push(element);
            }
            currentLastName = [];
        }
    }
    i = storage.length;
    let array = [];
    for (i > 0; i--;) {
        const employee = storage[i];
        const element = `last_name_max|${employee["sobrenome"]}|${employee["nome"]} `
        + `${employee["sobrenome"]}|${employee["salario"].toFixed(2)}`
        array.push(element);
    }
    const string = array.join("\n");
    return string;
};

const end = () => {
    const globalMax = getGlobal("globalMax", "global_max");
    const globalMin = getGlobal("globalMin", "global_min");
    const globalAvg = getGlobalAvg();
    const area = getArea();
    const most = getAreaAmount("most_employees", greaterThan);
    const least = getAreaAmount("least_employees", lessThan);
    console.log(globalMax);
    console.log(globalMin);
    console.log(globalAvg);
    console.log(area);
    console.log(most);
    console.log(least);
    const lastNameMax = getLastNameMax();
    console.log(lastNameMax);
};

(function start(){
    const file = process.argv[2];
    startStream(file);
})();