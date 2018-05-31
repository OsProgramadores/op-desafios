function obj(func, ar) {
    this.funcionarios = func;
    this.area = ar;
    this.i = 0;
    this.j = 0;
    this.max = [];
    this.min = [];
    this.salMax = -9999990;
    this.salMin = 99999999999;
    this.count = 0;
    this.d = 0;
    this.t = 0;
    this.tot = 0.0;
    this.len = this.funcionarios.length;
    this.len2 = this.area.length;
}

obj.prototype.getMaiorMenorSalario = function () {
    salMax = -9999990;
    salMin = 99999999999;
    max = [];
    min = [];

    for (i = 0; i < this.len; i++) {
        if (this.funcionarios[i].salario == salMax) {
            max.push(funcionarios[i]);
        } else if (this.funcionarios[i].salario > salMax) {
            max = [];
            salMax = this.funcionarios[i].salario;
            max.push(this.funcionarios[i]);
        }

        if (this.funcionarios[i].salario == salMin) {
            min.push(this.funcionarios[i]);
        } else if (this.funcionarios[i].salario < salMin) {
            min = [];
            salMin = this.funcionarios[i].salario;
            min.push(this.funcionarios[i]);
        }
    }
    for (i = 0; i < max.length; i++) {
        d = document.createElement("P");
        t = document.createTextNode("global_max|" + max[i].nome + " " + max[i].sobrenome + "|" + max[i].salario.toFixed(2));
        d.appendChild(t);
        document.body.appendChild(d);
    }

    for (i = 0; i < min.length; i++) {
        d = document.createElement("P");
        t = document.createTextNode("global_min|" + min[i].nome + " " + min[i].sobrenome + "|" + min[i].salario.toFixed(2));
        d.appendChild(t);
        document.body.appendChild(d);
    }
};

obj.prototype.getMedia = function () {
    tot = 0.0;
    for (i = 0; i < this.len; i++) {
        tot += this.funcionarios[i].salario;
    }

    tot /= this.len;

    d = document.createElement("P");
    t = document.createTextNode("global_avg|" + tot.toFixed(2));
    d.appendChild(t);
    document.body.appendChild(d);
};

obj.prototype.getMediaMaxArea = function () {
    salMax = -99999999.00;
    salMin = +99999999999.0;
    max = [];
    min = [];

    for (i = 0; i < this.len2; i++) {
        salMax = -0;
        salMin = +99999999;
        max = [];
        min = [];
        tot = 0.0;
        count = 0;

        for (j = 0; j < this.len; j++) {
            if (this.area[i].codigo === this.funcionarios[j].area) {
                count++;
                tot += this.funcionarios[j].salario;
                if (this.funcionarios[j].salario === salMax) {
                    max.push(this.funcionarios[j]);
                } else if (this.funcionarios[j].salario > salMax) {
                    salMax = this.funcionarios[j].salario;
                    max = [];
                    max.push(this.funcionarios[j]);
                }

                if (this.funcionarios[j].salario == salMin) {
                    min.push(this.funcionarios[j]);
                } else if (this.funcionarios[j].salario < salMin) {
                    salMin = this.funcionarios[j].salario;
                    min = [];
                    min.push(this.funcionarios[j]);
                }
            }
        }
        tot /= count;

        for (j = 0; j < max.length; j++) {
            d = document.createElement("P");
            t = document.createTextNode("area_max|" + this.area[i].nome + "|" + max[j].nome + " " + max[j].sobrenome + "|" + max[j].salario.toFixed(2));
            d.appendChild(t);
            document.body.appendChild(d);
        }

        for (j = 0; j < min.length; j++) {
            d = document.createElement("P");
            t = document.createTextNode("area_min|" + this.area[i].nome + "|" + min[j].nome + " " + min[j].sobrenome + "|" + min[j].salario.toFixed(2));
            d.appendChild(t);
            document.body.appendChild(d);
        }

        d = document.createElement("P");
        t = document.createTextNode("area_avg|" + this.area[i].nome + "|" + tot.toFixed(2));
        d.appendChild(t);
        document.body.appendChild(t);
    }
};

obj.prototype.getAreas = function () {
    var countMax = 0;
    var countMin = 15;
    var count = 0;
    max = [];
    min = [];

    for (i = 0; i < this.len2; i++) {
        count = 0;
        for (j = 0; j < this.len; j++) {
            if (this.area[i].codigo == this.funcionarios[j].area) {
                count++;
            }
        }

        if (count == countMax) {
            max.push(this.area[i]);
        } else if (count > countMax) {
            countMax = count;
            max = [];
            max.push(this.area[i]);
        }

        if (count == countMin) {
            min.push(areas[i]);
        } else if (count < countMin) {
            countMin = count;
            min = [];
            min.push(this.area[i]);
        }
    }

    for (i = 0; i < max.length; i++) {
        d = document.createElement("P");
        t = document.createTextNode("most_employees|" + max[i].nome + "|" + countMax);
        d.appendChild(t);
        document.body.appendChild(d);
    }
    for (i = 0; i < min.length; i++) {
        d = document.createElement("P");
        t = document.createTextNode("least_employees|" + min[i].nome + "|" + countMin);
        d.appendChild(t);
        document.body.appendChild(d);
    }
};

obj.prototype.salariosSobrenome = function () {
    var listaSobrenome = [];
    var possui = false;
    for (i = 0; i < this.len; i++) {
        possui = true;
        for (j = 0; j < listaSobrenome.length; j++) {
            if (this.funcionarios[i].sobrenome == listaSobrenome[j])
                possui = false;
        }

        if (possui) {
            listaSobrenome.push(this.funcionarios[i].sobrenome);
        }
    }

    for (i = 0; i < listaSobrenome.length; i++) {
        count = 0;
        salMax = -9999999.0;
        max = [];

        for (j = 0; j < this.len; j++) {

            if (this.funcionarios[j].sobrenome === listaSobrenome[i]) {
                count++;
                if (this.funcionarios[j].salario == salMax) {
                    max.push(funcionarios[j]);
                } else if (this.funcionarios[j].salario > salMax) {
                    salMax = this.funcionarios[j].salario;
                    max = [];
                    max.push(this.funcionarios[j]);
                }
            }
        }

        if (count > 1) {
            for (j = 0; j < max.length; j++) {
                d = document.createElement("P");
                t = document.createTextNode("last_name_max|" + listaSobrenome[i] + "|" + max[j].nome + " " + max[j].sobrenome + "|" + max[j].salario.toFixed(2));
                d.appendChild(t);
                document.body.appendChild(d);
            }
        }
    }
};