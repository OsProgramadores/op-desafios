"""Função que captura os dados dos funcionários de um
arquivo .json e apresenta os seguintes dados:
- Funcionário com maior salário;
- Funcionário com menor salário;
- Média salarial dos funcionários;
- Funcionário com maior salário dentro de uma área;
- Funcionário com menor salário dentro de uma área;
- Média salarial dos funcionários por área;
- Área com maior número de funcionários;
- Área com menor número de funcionários;
- Maior salário dentre os sobrenomes repetidos."""
import sys
import json

def salariomaximo(func):
    """Função para identificar o(s) maior(es) salário(s)
    em um array de funcionários
    @func: list"""
    maximo = []
    lenfunc = len(func)
    for indice in range(0, lenfunc):
        salariomax = func[indice]["salario"]
        nomemax = func[indice]["nome"] + " " + func[indice]["sobrenome"]
        if indice == 0:
            maximo.append({"salario": salariomax, "nome": nomemax})
        elif maximo[0]["salario"] == salariomax:
            maximo.append({"salario": salariomax, "nome": nomemax})
        elif maximo[0]["salario"] < salariomax:
            maximo.clear()
            maximo.append({"salario": salariomax, "nome": nomemax})
    return maximo


def salariominimo(func):
    """Função para identificar o(s) menor(es) salário(s)
    em um array de funcionários
    @func: list"""
    minimo = []
    lenfunc = len(func)
    for indice in range(0, lenfunc):
        salariomin = func[indice]["salario"]
        nomemin = func[indice]["nome"] + " " + func[indice]["sobrenome"]
        if indice == 0:
            minimo.append({"salario": salariomin, "nome": nomemin})
        elif minimo[0]["salario"] == salariomin:
            minimo.append({"salario": salariomin, "nome": nomemin})
        elif minimo[0]["salario"] > salariomin:
            minimo.clear()
            minimo.append({"salario": salariomin, "nome": nomemin})
    return minimo


def mediasalarial(func):
    """Função para calcular a média salarial
    em um array de funcionários
    @func: list"""
    total = 0.0
    lenfunc = len(func)
    for indice in range(0, lenfunc):
        total += func[indice]["salario"]
    return total/len(func)


def separarfuncionarioporarea(func, areafunc):
    """Função para dividir o(s) funcionário(s) por área
    em um array de funcionários
    @func: list
    @areafunc: list"""
    resultado = []
    lenarea = len(areafunc)
    lenfunc = len(func)
    for a in range(0, lenarea):
        dadosfunc = []
        for f in range(0, lenfunc):
            if func[f]["area"] == areafunc[a]["codigo"]:
                func[f]["area"] = areafunc[a]["nome"]
                dadosfunc.append(func[f])
        if len(dadosfunc) > 0:
            resultado.append(dadosfunc)
    return resultado


def areamaiornumfunc(func):
    """Função para identificar a área que possui um maior
    número de funcionários em um array
    @func: list"""
    maiorarea = []
    lenfunc = len(func)
    for indice in range(0, lenfunc):
        areamaiornum = func[indice][0]["area"]
        qtdmaiornum = len(func[indice])
        if indice == 0:
            maiorarea.append({"area": areamaiornum, "qtd": qtdmaiornum})
        elif maiorarea[0]["qtd"] == qtdmaiornum:
            maiorarea.append({"area": areamaiornum, "qtd": qtdmaiornum})
        elif maiorarea[0]["qtd"] < qtdmaiornum:
            maiorarea.clear()
            maiorarea.append({"area": areamaiornum, "qtd": qtdmaiornum})
    return maiorarea


def areamenornumfunc(func):
    """Função para identificar o(s) menor(es) salário(s)
    em um array de funcionários
    @func: list"""
    menorarea = []
    lenfunc = len(func)
    for indice in range(0, lenfunc):
        areamenornum = func[indice][0]["area"]
        qtdmenornum = len(func[indice])
        if indice == 0:
            menorarea.append({"area": areamenornum, "qtd": qtdmenornum})
        elif menorarea[0]["qtd"] == qtdmenornum:
            menorarea.append({"area": areamenornum, "qtd": qtdmenornum})
        elif menorarea[0]["qtd"] > qtdmenornum:
            menorarea.clear()
            menorarea.append({"area": areamenornum, "qtd": qtdmenornum})
    return menorarea


def pesquisarsobrenomearray(sobrenome, arrayfunc):
    """Função para identificar se o sobrenome existe
    em um array de funcionários
    @sobrenome: string
    @arrayfunc: list"""
    lenarrayfunc = len(arrayfunc)
    for indicelastname in range(0, lenarrayfunc):
        for indicefuncionario in range(0, len(arrayfunc[indicelastname])):
            sobrenomearray = arrayfunc[indicelastname][indicefuncionario]["sobrenome"]
            if sobrenome == sobrenomearray:
                return False
    return True


def qtdsobrenomearray(func, sobrenomemaior):
    """Função para identificar a quantidade de um
    determinado sobrenome em um array de funcionários
    @func: list
    @sobrenomemaior: string"""
    qtdsobrenome = 0
    nomes = []
    lenf = len(func)
    for indicearea in range(0, lenf):
        for indicefunc in range(0, len(func[indicearea])):
            sobrenomefunc = func[indicearea][indicefunc]["sobrenome"]
            if sobrenomemaior == sobrenomefunc:
                qtdsobrenome += 1
                nomesobrenomemaior = func[indicearea][indicefunc]["nome"]
                salariosobrenomemaior = func[indicearea][indicefunc]["salario"]
                nomes.append({"nome": nomesobrenomemaior, "salario": salariosobrenomemaior})
    return qtdsobrenome, nomes


def sobrenomemaiorsalario(func):
    """Função para identificar o sobrenome ao qual possui
    o maior salário em um array de funcionários
    @func: list"""
    lastnamemaior = []
    lenfunc = len(func)
    for indicearea in range(0, lenfunc):
        for indicefunc in range(0, len(func[indicearea])):
            sobrenomefunc = func[indicearea][indicefunc]["sobrenome"]
            qtd, nomecompleto = qtdsobrenomearray(func, sobrenomefunc)
            if qtd > 1 and pesquisarsobrenomearray(sobrenomefunc, lastnamemaior):
                aux = []
                for indicenome in range(0, qtd):
                    sbr = nomecompleto[indicenome]["nome"]
                    sal = nomecompleto[indicenome]["salario"]
                    aux.append({"sobrenome": sobrenomefunc, "nome": sbr, "salario": sal})
                lastnamemaior.append(aux)
    return lastnamemaior


with open(sys.argv[1], 'r', encoding='utf-8') as dados:
    arquivo = json.load(dados)

areas = arquivo.get("areas")
funcionarios = arquivo.get("funcionarios")

globalmax = salariomaximo(funcionarios)
globalmin = salariominimo(funcionarios)
globalavg = mediasalarial(funcionarios)
funcporarea = separarfuncionarioporarea(funcionarios, areas)
mostemployees = areamaiornumfunc(funcporarea)
leastemployees = areamenornumfunc(funcporarea)
lastnamemax = sobrenomemaiorsalario(funcporarea)

lenglobalmax = len(globalmax)
for imax in range(0, lenglobalmax):
    nomemaior = globalmax[imax]["nome"]
    salariomaior = globalmax[imax]["salario"]
    print("global_max|{}|{}".format(nomemaior, salariomaior))

lenglobalmin = len(globalmin)
for imin in range(0, lenglobalmin):
    nomemenor = globalmin[imin]["nome"]
    salariomenor = globalmin[imin]["salario"]
    print("global_min|{}|{}".format(nomemenor, salariomenor))

print("global_avg|{0:.2f}".format(globalavg))

lenfuncporarea = len(funcporarea)
for iporarea in range(0, lenfuncporarea):
    areamax = salariomaximo(funcporarea[iporarea])
    areamin = salariominimo(funcporarea[iporarea])
    areaavg = mediasalarial(funcporarea[iporarea])

    lenareamax = len(areamax)
    for imax in range(0, lenareamax):
        area = funcporarea[iporarea][0]["area"]
        nome = areamax[imax]["nome"]
        salario = areamax[imax]["salario"]
        print("area_max|{}|{}|{}".format(area, nome, salario))

    lenareamin = len(areamin)
    for imin in range(0, lenareamin):
        area = funcporarea[iporarea][0]["area"]
        nome = areamin[imin]["nome"]
        salario = areamin[imin]["salario"]
        print("area_min|{}|{}|{}".format(area, nome, salario))

    area = funcporarea[iporarea][0]["area"]
    print("area_avg|{}|{:.2f}".format(area, areaavg))

lenmostemployees = len(mostemployees)
for maior in range(0, lenmostemployees):
    areamaior = mostemployees[maior]["area"]
    qtdmaior = mostemployees[maior]["qtd"]
    print("most_employees|{}|{}".format(areamaior, qtdmaior))

lenleastemployees = len(leastemployees)
for menor in range(0, lenleastemployees):
    areamenor = leastemployees[menor]["area"]
    qtdmenor = leastemployees[menor]["qtd"]
    print("least_employees|{}|{}".format(areamenor, qtdmenor))

lenlastnamemax = len(lastnamemax)
for indicelastnamemax in range(0, lenlastnamemax):
    salariomaxlastname = salariomaximo(lastnamemax[indicelastnamemax])
    lensalariomaxlastname = len(salariomaxlastname)
    for indicesalariosmaiores in range(0, lensalariomaxlastname):
        sobrenomelastname = lastnamemax[indicelastnamemax][0]["sobrenome"]
        nomelastname = salariomaxlastname[indicesalariosmaiores]["nome"]
        salariolastname = salariomaxlastname[indicesalariosmaiores]["salario"]
        print("last_name_max|{}|{}|{}".format(sobrenomelastname, nomelastname, salariolastname))
