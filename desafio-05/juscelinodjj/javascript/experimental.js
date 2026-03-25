// versão experimental
// modo de execução:
// $ node --expose_gc --max-old-space-size=16384 experimental Funcionarios-5M.json  | sort | md5sum
// obs: o arquivo .JSON deve está na mesma pasta do .JS
//
const fs = require("fs");
// external package
const JSONStream = require("JSONStream");
const eventStream = require("event-stream");

// ------------

const _areas = [];
const _ = {
    globalMax: [],
    globalMin: [],
    globalAvg: [],
    area: {},
    areaAvg: []
};
const data = {};

// ------------

const read = file => {
    const fileStream = fs.createReadStream(file);
    fileStream.pipe(JSONStream.parse("funcionarios.*"))
    .pipe(eventStream.through(data => parse(data)))
    fileStream.pipe(JSONStream.parse("areas.*"))
    .pipe(eventStream.through(data => _areas.push(data)))
    .on('end', () => end());
};

const end = () => {
    const globalMax = _.globalMax
        .map(employee => `global_max|${employee.nome} ${employee.sobrenome}|${employee.salario.toFixed(2)}`)
        .join("\n");
    const globalMin = _.globalMin
        .map(employee => `global_min|${employee.nome} ${employee.sobrenome}|${employee.salario.toFixed(2)}`)
        .join("\n");

    const globalAvg = getGlobalAvg();
    const area = getArea();
    const most = getAreaCount("most_employees", greaterThan);
    const least = getAreaCount("least_employees", lessThan);
    const lastNameMax = getLastNameMax();

    console.log(globalMax);
    console.log(globalMin);
    console.log(globalAvg);
    console.log(area);
    console.log(most);
    console.log(least);
    console.log(lastNameMax);
};


// ------------

const greaterThan = (a, b) => a > b;
const lessThan = (a, b) => a < b;
const getGlobal = (employee, target, fn) => {
    !_[target][0]
        ? _[target] = [employee]
        : (fn(employee.salario, _[target][0]["salario"])
            ? _[target] = [employee]
            : (employee.salario === _[target][0]["salario"] ? _[target].push(employee) : null)
        );
};

// ------------

const setGlobalAvg = employee => _["globalAvg"].push(employee["salario"]);
const getGlobalAvg = () => {
    return _["globalAvg"]
        .reduce((iArray, value, index) => { return [iArray[0] + value, index] }, [0, 0])
        .map((element, index, array) => index === 0 ? "global_avg|" : (array[0] / (element + 1)).toFixed(2))
        .join("");
};

// ------------

const addInGlobalArea = (employee, target, fn) => {
    const code = employee["area"];
    !_["area"][code] ? _["area"][code] = {} : null;
    !_["area"][code][target] ? _["area"][code][target] = [] : null;
    !_["area"][code][target][0]
        ? _["area"][code][target] = [employee]
        : (fn(employee.salario, _["area"][code][target][0]["salario"])
            ? _["area"][code][target] = [employee]
            : (employee.salario === _["area"][code][target][0]["salario"]
                ? _["area"][code][target].push(employee)
                : null
            )
        );
    // para não duplicar os salarios, esse trecho só é chamado com target max
    if (target === "max") return;
    !_["area"][code]["avg"] ? _["area"][code]["avg"] = [] : null;
    _["area"][code]["avg"].push(employee["salario"]);
};

// ------------

const getOccupation = (code) => {
    return _areas
        .reduce((str, area) => { return area.codigo === code ? area.nome : str; }, "");
};

const getArea = () => {
    return Object.entries(_["area"])
        .reduce((iArray, array) => {
            const area = array[0];
            const obj = array[1];
            const max = obj["max"].map(employee => `area_max|${getOccupation(area)}|`
                + `${employee.nome} ${employee.sobrenome}|${employee.salario.toFixed(2)}`
            );
            const min = obj["min"].map(employee => `area_min|${getOccupation(area)}|`
                + `${employee.nome} ${employee.sobrenome}|${employee.salario.toFixed(2)}`
            );
            const avg = obj["avg"].reduce((iArray, value, index) => { return [iArray[0] + value, index] }, [0, 0])
                .map((element, index, array) => index === 0 ? `area_avg|${getOccupation(area)}|` : (array[0] / (element + 1)).toFixed(2))
                .join("");
            // setando agora para usar posteriomente em getAreaCount
            // evitando a re-leitura de _["area"]
            setAreaCount([area, (obj["avg"].length)]);
            iArray = [...iArray, ...max, ...min, avg];
            return iArray;
        }, [])
        .join("\n");
};

// ------------

const setAreaCount = array => _["areaAvg"].push(array);

const getAreaCount = (label, fn) => {
    return _["areaAvg"].reduce((iArray, array) => {
        const employeeAmount = array[1];
        return !iArray[0]
            ? [array]
            : (fn(employeeAmount, (iArray[0])[1])
                ? [array]
                : (employeeAmount === (iArray[0])[1] ? [...iArray, array] : iArray)
            )
    },[])
    .map((array) => `${label}|${getOccupation(array[0])}|${array[1]}`)
    .join("\n");
};

// ------------


const saveData = employee => {
    const lastName = employee["sobrenome"];
    !data[lastName] ? data[lastName] = [] : null;
    const newObj = {
        nome: employee.nome,
        sobrenome: employee.sobrenome,
        salario: employee.salario
    };
    data[lastName].push(newObj);
};

const getLastNameMax = () => {
    return Object.values(data)
        .filter(element => element.length > 1)
        .reduce((iArray, arrayEmployee) => {
            const max = arrayEmployee.reduce((iArray, employee) => {
                const salary = employee["salario"];
                return !iArray[0]
                    ? [employee]
                    : (salary > iArray[0]["salario"]
                        ? [employee]
                        : (salary === iArray[0]["salario"] ? [...iArray, employee] : iArray)
                    )
            }, []);
            return [...iArray, ...max];
        }, [])
        .map(employee =>
            `last_name_max|${employee["sobrenome"]}|${employee["nome"]} `
            + `${employee["sobrenome"]}|${employee["salario"].toFixed(2)}`
        )
        .join("\n");
};

// ------------

const parse = employee => {
    saveData(employee);
    getGlobal(employee, "globalMax", greaterThan);
    getGlobal(employee, "globalMin", lessThan);
    setGlobalAvg(employee);
    addInGlobalArea(employee, "max", greaterThan);
    addInGlobalArea(employee, "min", lessThan);
};

// ------------

(function start(){
    const target = process.argv[2];
    read(target);
})();

// ------------