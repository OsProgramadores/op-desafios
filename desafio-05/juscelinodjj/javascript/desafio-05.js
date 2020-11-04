// Utilize a linguagem de programação de sua preferência (e quaisquer bibliotecas que sejam necessárias)
// e escreva um programa que leia o nome de um arquivo JSON como parâmetro
// e imprima as informações solicitadas a seguir, baseado no conteúdo do arquivo lido.
//
// 1. Quem mais recebe e quem menos recebe na empresa e a média salarial da empresa.
// 2. Quem mais recebe e quem menos recebe em cada área e a média salarial em cada área.
// 3. Área(s) com o maior e menor número de funcionários
// 4. Maiores salários para funcionários com o mesmo sobrenome
//
// Para obter o MD5 do resultado (no Linux), execute o seu programa da seguinte forma:
// <PROGRAMA> <ARQUIVO DE TESTE> | sort | md5sum
//
// modo de execução: node desafio-05.js Funcionarios-10K.json | sort | md5sum
const fs = require("fs");

const run = target => {
    const readJSON = file => fs.readFileSync(`${__dirname}/${file}`, "utf8");
    const _employees = (function(){return Object.values(JSON.parse(readJSON(target)))[0]})(target);
    const _areas = (function(){return Object.values(JSON.parse(readJSON(target)))[1]})(target);

    const rearrangeEmployeeList = (employeeList, value) => {
        return Object.values(employeeList.reduce((obj, employee) => {
            !obj[employee[value]] ? obj[employee[value]] = [] : null;
            obj[employee[value]].push(employee);
            return obj;
        }, {}))
    };

    const getOccupation = (code) => {
        return _areas
            .reduce((str, area) => { return area.codigo === code ? area.nome : str; }, "");
    };

    const lessThan = (a, b) => a < b;
    const greaterThan = (a, b) => a > b;

    const getGlobal = (employeeList, label, fn) => {
        return employeeList.reduce((arr, employee, index) => {
            return !index
                ? [employee]
                : (fn(employee.salario, arr[0].salario)
                    ? [employee]
                    : (employee.salario === arr[0].salario ? [...arr, ...[employee]] : arr)
                );
        }, [])
        .map(employee => `${label}|${employee.nome} ${employee.sobrenome}|${(employee.salario).toFixed(2)}`)
        .join("\n");
    };

    const getGlobalAvg = (employeeList, label) => {
        return employeeList
            .reduce( (arr, employee, index) => { return [arr[0] + employee.salario, index] }, [0, 0])
            .map((element, index, array) => index === 0 ? `${label}` : (array[0] / (element + 1)).toFixed(2))
            .join("");
    };

    const getGlobalByArea = (employeeList, fns) => {
        const [fn1, fn2, fn3, fn4, fn5] = fns;
        return rearrangeEmployeeList(employeeList, "area")
            .map(arr => {
                const area = arr[0].area;
                const occupation = fn1(area);
                const max = fn2(arr, `area_max|${occupation}`, fn3);
                const min = fn2(arr, `area_min|${occupation}`, fn4);
                const avg = fn5(arr, `area_avg|${occupation}|`);
                return [max, min, avg];
            })
            .reduce((arr, element) => {
                return [...arr, ...element];
            })
            .join("\n");
    };

    const getNumberOfEmployees = (employeeList, label, fns) => {
        const [fn1, fn2] = fns;
        return rearrangeEmployeeList(employeeList, "area")
            .reduce((arr, element, index) => {
                return !index
                    ? [element]
                    : (fn1(element.length, arr[0].length)
                        ? [element]
                        : (element.length === arr[0].length ? [...arr, element] : arr)
                    )
            }, [])
            .map(arr => {
                const area = arr[0].area;
                const occupation = fn2(area);
                const amount = arr.length;
                return `${label}|${occupation}|${amount}`;
            })
            .join("\n");
    };

    const getLastNameWithHigherSalary = employeeList => {
        return rearrangeEmployeeList(employeeList, "sobrenome")
            .filter( element => element.length > 1)
            .map(array => {
                return array.reduce((arr, employee, index) => {
                    const currentSalary = employee.salario;
                    const lastSalary = arr[0].salario;
                    return !index
                        ? [employee]
                        : (currentSalary > lastSalary
                            ? [employee]
                            : (currentSalary === lastSalary ? [...arr, employee] : arr)
                        )
                }, [{}]);
            })
            .map(array => {
                return array.map(employee => {
                    const name = employee.nome;
                    const lastName = employee.sobrenome;
                    const salary = (employee.salario).toFixed(2);
                    return `last_name_max|${lastName}|${name} ${lastName}|${salary}`;
                })
                .join("\n");
            })
            .join("\n");
    };

    const globalMax = getGlobal(_employees, "global_max", greaterThan);
    const globalMin = getGlobal(_employees, "global_min", lessThan);
    const globalAvg = getGlobalAvg(_employees, "global_avg|");
    const globalByArea = getGlobalByArea(_employees, [getOccupation, getGlobal, greaterThan, lessThan, getGlobalAvg]);
    const withMostEmployees = getNumberOfEmployees(_employees, "most_employees", [greaterThan, getOccupation]);
    const withLeastEmployees = getNumberOfEmployees(_employees, "least_employees", [lessThan, getOccupation]);
    const lastNameWithHigherSalary = getLastNameWithHigherSalary(_employees);

    console.log(globalMax);
    console.log(globalMin);
    console.log(globalAvg);
    console.log(globalByArea);
    console.log(withMostEmployees);
    console.log(withLeastEmployees);
    console.log(lastNameWithHigherSalary);
};

(function start(){
    const target = process.argv[2];
    run(target);
})();