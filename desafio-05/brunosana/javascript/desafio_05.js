/*
let funcionarios = {
    "funcionarios":[
        {
            "id":0,
            "nome":"Marcelo",
            "sobrenome":"Silva",
            "salario":3200.00,
            "area":"SM"
        },
        {
            "id":1,
            "nome":"Washington",
            "sobrenome":"Ramos",
            "salario":2700.00,
            "area":"UD"
        },
        {
            "id":2,
            "nome":"Sergio",
            "sobrenome":"Pinheiro",
            "salario":2450.00,
            "area":"SD"
        },
        {
            "id":3,
            "nome":"Bernardo",
            "sobrenome":"Costa",
            "salario":3700.00,
            "area":"SM"
        },
        {
            "id":4,
            "nome":"Cleverton",
            "sobrenome":"Farias",
            "salario":2750.00,
            "area":"SD"
        },
        {
            "id":5,
            "nome":"Abraão",
            "sobrenome":"Campos",
            "salario":2550.00,
            "area":"SD"
        },
        {
            "id":6,
            "nome":"Letícia",
            "sobrenome":"Farias",
            "salario":2450.00,
            "area":"UD"
        },
        {
            "id":7,
            "nome":"Fernando",
            "sobrenome":"Ramos",
            "salario":2450.00,
            "area":"SD"
        },
        {
            "id":8,
            "nome":"Marcelo",
            "sobrenome":"Farias",
            "salario":2550.00,
            "area":"UD"
        },
        {
            "id":9,
            "nome":"Fabio",
            "sobrenome":"Souza",
            "salario":2750.00,
            "area":"SD"
        },
        {
            "id":10,
            "nome":"Clederson",
            "sobrenome":"Oliveira",
            "salario":2500.00,
            "area":"SD"
        }
    ],
    "areas":[
        {
            "codigo":"SD",
            "nome":"Desenvolvimento de Software"
        },
        {
            "codigo":"SM",
            "nome":"Gerenciamento de Software"
        },
        {
            "codigo":"UD",
            "nome":"Designer de UI/UX"
        }
    ]
}
*/

let funcionarios = require(`./${process.argv[2]}`)

//Questão 1
const global_max = function (array) {
let array_max = [array[0]];
array.forEach(f => {
    if (f.salario > array_max[0].salario){
        array_max = [];
        array_max.push(f);
    }else{
        if (f.salario == array_max[0].salario && f.id != array_max[0].id){
            array_max.push(f);
        }
    }
});
return array_max;
}
const global_min = function (array) {
let array_min = [array[0]];
array.forEach(f => {
    if (f.salario < array_min[0].salario){
        array_min = [];
        array_min.push(f);
    }else{
        if (f.salario == array_min[0].salario){
            array_min.push(f);
        }
    }
});
return array_min;
}
const global_avg = function(array){
let avg = 0, n = 0;
array.forEach(f => {
    avg += f.salario;
    n++;
});
return (avg/n).toFixed(2);
}


let questao1_a = global_min(funcionarios.funcionarios).forEach(f=> {
console.log(`global_min | ${f.nome} ${f.sobrenome} | ${f.salario.toFixed(2)}`);
}) 

let questao1_b = global_max(funcionarios.funcionarios).forEach(f => {
console.log(`global_max | ${f.nome} ${f.sobrenome} | ${f.salario.toFixed(2)}`);
});

//Questao 1 - c
console.log(`global_avg | ${global_avg(funcionarios.funcionarios)}`);


//Questão 2
let areas_with_func_numbers = [];
funcionarios.areas.forEach(e=>{
let new_array = []
funcionarios.funcionarios.map(f => {
    f.area == e.codigo ? new_array.push(f) : null;
});
let questao2_a = global_min(new_array).forEach(f=> {
    console.log(`area_min | ${e.nome} | ${f.nome} ${f.sobrenome} | ${f.salario.toFixed(2)}`);
}) 

let questao2_b = global_max(new_array).forEach(f => {
    console.log(`area_max | ${e.nome} | ${f.nome} ${f.sobrenome} | ${f.salario.toFixed(2)}`);
});

console.log(`area_avg | ${e.nome} | ${global_avg(new_array)}`);
e.numero_funcionarios = new_array.length;
areas_with_func_numbers.push(e);
})

areas_with_func_numbers.sort(function (ex, ey){
if (ex.numero_funcionarios > ey.numero_funcionarios) return 1;
})

let initial_value = areas_with_func_numbers[0];
areas_with_func_numbers.forEach( e => {
initial_value.numero_funcionarios == e.numero_funcionarios ? console.log(`least_employeers | ${e.nome} | ${e.numero_funcionarios}`) : null;
})
initial_value = areas_with_func_numbers[areas_with_func_numbers.length-1];
areas_with_func_numbers.forEach( e => {
initial_value.numero_funcionarios == e.numero_funcionarios ? console.log(`most_employeers | ${e.nome} | ${e.numero_funcionarios}`) : null;
})


let sobrenomes = []
funcionarios.funcionarios.forEach(e => {
let have_sobrenome = false;
sobrenomes.forEach(f => {
    if ((e.sobrenome == f) && !have_sobrenome){
        have_sobrenome = true;
    } 
})
have_sobrenome ? null : sobrenomes.push(e.sobrenome);
})

sobrenomes.forEach(e => {
let vf = funcionarios.funcionarios.filter(avaliable = x => {
    return x.sobrenome == e;
})
if (vf.length > 1){
    global_max(vf).forEach(el => {
        console.log(`last_name_max | ${e} | ${el.nome} | ${el.salario}`);
    })
}
}) 