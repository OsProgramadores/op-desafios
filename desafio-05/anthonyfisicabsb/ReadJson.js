var obj = JSON.parse(funcionarios);
var areas = JSON.parse(areas);
var i = 0;
var j = 0;
var max = [];
var min = [];
var salMax = -9999990;
var salMin = 99999999999;
var count = 0;
var len = obj.length;
var len2 = areas.length;

function getMaiorMenorSalario() {
    salMax = -9999990;
    salMin = 99999999999;
    max = [];
    min = [];

    for (i = 0; i < len; i++) {
        if (obj[i].salario == salMax) {
            max.push(obj[i]);
        } else if (obj[i].salario > salMax) {
            max = [];
            salMax = obj[i].salario;
            max.push(obj[i]);
        }

        if (obj[i].salario == salMin) {
            min.push(obj[i]);
        } else if (obj[i].salario < salMin) {
            min = [];
            salMin = obj[i].salario;
            min.push(obj[i]);
        }
    }
    for (i = 0; i < max.length; i++) {
        console.log("global_max|" + max[i].nome + " " + max[i].sobrenome + "|" + max[i].salario.toFixed(2));
    }

    for (i = 0; i < min.length; i++) {
        console.log("global_min|" + min[i].nome + " " + min[i].sobrenome + "|" + min[i].salario.toFixed(2));
    }
}

function getMedia() {
    var tot = 0.0;
    for (i = 0; i < len; i++) {
        tot += obj[i].salario;
    }

    tot /= obj.length;

    console.log("global_avg|" + tot.toFixed(2));
}

function getMediaMaxArea() {
    var salMax = -99999999.00;
    var salMin = +99999999999.0;
    max = [];
    min = [];
    var tot = 0.0;

    for (i = 0; i < len2; i++) {
        salMax = -0;
        salMin = +99999999;
        max = [];
        min = [];
        tot = 0.0;
        count = 0;

        for (j = 0; j < len; j++) {
            if (areas[i].codigo === obj[j].area) {
                count++;
                tot += obj[j].salario;
                if (obj[j].salario === salMax) {
                    max.push(obj[j]);
                } else if (obj[j].salario > salMax) {
                    salMax = obj[j].salario;
                    max = [];
                    max.push(obj[j]);
                }

                if (obj[j].salario == salMin) {
                    min.push(obj[j]);
                } else if (obj[j].salario < salMin) {
                    salMin = obj[j].salario;
                    min = [];
                    min.push(obj[j]);
                }
            }
        }
        tot /= count;

        for (j = 0; j < max.length; j++) {
            console.log("area_max|" + areas[i].nome + "|" + max[j].nome + " " + max[j].sobrenome + "|" + max[j].salario.toFixed(2));
        }

        for (j = 0; j < min.length; j++) {
            console.log("area_min|" + areas[i].nome + "|" + min[j].nome + " " + min[j].sobrenome + "|" + min[j].salario.toFixed(2));
        }

        console.log("area_avg|" + areas[i].nome + "|" + tot.toFixed(2));
    }
}

function getAreas() {
    var countMax = 0;
    var countMin = 15;
    var count = 0;
    max = [];
    min = [];

    for (i = 0; i < len2; i++) {
        count = 0;
        for (j = 0; j < len; j++) {
            if (areas[i].codigo == obj[j].area) {
                count++;
            }
        }

        if (count == countMax) {
            max.push(areas[i]);
        } else if (count > countMax) {
            countMax = count;
            max = [];
            max.push(areas[i]);
        }

        if (count == countMin) {
            min.push(areas[i]);
        } else if (count < countMin) {
            countMin = count;
            min = [];
            min.push(areas[i]);
        }
    }

    for (i = 0; i < max.length; i++) {
        console.log("most_employees|" + max[i].nome + "|" + countMax);
    }
    for (i = 0; i < min.length; i++) {
        console.log("least_employees|" + min[i].nome + "|" + countMin);
    }
}

function salariosSobrenome() {
    var listaSobrenome = [];
    var possui = false;
    for(i=0; i<len;i++){
        possui = true;
        for(j=0; j<listaSobrenome.length; j++){
            if(obj[i].sobrenome == listaSobrenome[j])
                possui = false;
        }
        
        if(possui){
            listaSobrenome.push(obj[i].sobrenome);
        }
    }

    for(i=0; i<listaSobrenome.length; i++){
        count = 0;
        salMax = -9999999.0;
        max = [];

        for(j=0; j<len; j++){
            
            if(obj[j].sobrenome === listaSobrenome[i]){
                count++;
                if(obj[j].salario == salMax){
                    max.push(obj[j]);
                }else if(obj[j].salario > salMax){
                    salMax = obj[j].salario;
                    max = [];
                    max.push(obj[j]);
                }
            }
        }

        if(count > 1){
            for(j=0; j<max.length; j++){
                console.log("last_name_max|"+listaSobrenome[i]+"|"+max[j].nome + " " + max[j].sobrenome + "|" + max[j].salario.toFixed(2));
            }
        }
    }
}