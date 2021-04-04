"""
Resolução do desafio 5 do site OsProgramadores, baseada na solucao
original do Roger Demetrescu, que se encontra disponivel no seguinte
link: https://github.com/rdemetrescu/OsProgramadores/blob/master/desafio-5/d05.py

Para consultar os resultados dos benchmarks dos desafios, acesse o seguinte
link: http://bcampos.com/Graphs.php
"""

import sys
import orjson


def processar(filename):
    """
    Este metodo ira parsear o arquivo json recebido e ira extrair as informacoes acerca dos
    funcionarios que ganham mais e menos para as respectivas areas e sobrenomes, alem de recuperar
    informacoes do total de salarios e quantidades de funcionarios.

    :param filename: nome do arquivo json contendo as informações dos funcionarios e areas
    :return: descricoes das areas e os funcionarios que ganham mais e menos para cada area e
             sobrenome
    """
    with open(filename, 'rb') as file:
        doc = orjson.loads(file.read())

    funcionarios = doc['funcionarios']
    areas = doc['areas']

    areas_descr = {x['codigo']: x['nome'] for x in areas}
    gmaior, gmenor, gsoma, gqtde = None, None, 0, 0
    fmais, fmenos = [], []
    ais = {}  # área info's
    sis = {}  # sobrenome info's

    for func in funcionarios:
        sob = func['sobrenome']
        sal = func['salario']

        try:
            if sal > gmaior:
                gmaior = sal
                fmais.clear()
                fmais.append(func)
            elif sal == gmaior:
                fmais.append(func)
        except KeyError:
            gmaior = sal
            fmais.append(func)

        try:
            if sal < gmenor:
                gmenor = sal
                fmenos.clear()
                fmenos.append(func)
            elif sal == gmenor:
                fmenos.append(func)
        except KeyError:
            gmenor = sal
            fmenos.append(func)

        gsoma += sal
        gqtde += 1

        area = func['area']
        try:
            ai = ais[area]
            if sal > ai[0]:
                ai[0] = sal
                ai[4].clear()
                ai[4].append(func)
            elif sal == ai[0]:
                ai[4].append(func)

            if sal < ai[1]:
                ai[1] = sal
                ai[5].clear()
                ai[5].append(func)
            elif sal == ai[1]:
                ai[5].append(func)

            ai[2] += sal
            ai[3] += 1
        except KeyError:
            # maior, menor, soma, qtde, funcs que ganham mais, funcs que ganham menos
            ais[area] = [sal, sal, sal, 1, [func], [func]]

        try:
            si = sis[sob]
            _sal = si[0]
            si[1] += 1
            if sal > _sal:
                si[0] = sal
                si[2].clear()
                si[2].append(func)
            elif sal == _sal:
                si[2].append(func)
        except KeyError:
            # maior, qtde, funcs que ganham mais
            sis[sob] = [sal, 1, [func]]

    gmedia = (gsoma / gqtde)

    return areas_descr, gmedia, fmais, fmenos, ais, sis


def gerar_saida(areas_descr, gmedia, fmais, fmenos,
                ais, sis):
    """
    Este metodo, a partir das informacoes recuperadas do metodo anterior, ira processar a saida
    do programa, separada por cada questao do desafio.
    """
    output = []
    out = output.append

    # QUESTÃO 1
    for func in fmais:
        out(f'global_max|{func["nome"]} {func["sobrenome"]}|{func["salario"]:.2f}')
    for func in fmenos:
        out(f'global_min|{func["nome"]} {func["sobrenome"]}|{func["salario"]:.2f}')

    out(f'global_avg|{gmedia:.2f}')

    for area, (_, _, asoma, aqtde, afuncsmais, afuncsmenos) in ais.items():
        area_descr = areas_descr[area]
        for func in afuncsmais:
            out(f'area_max|{area_descr}|{func["nome"]} {func["sobrenome"]}|{func["salario"]:.2f}')
        for func in afuncsmenos:
            out(f'area_min|{area_descr}|{func["nome"]} {func["sobrenome"]}|{func["salario"]:.2f}')

        out(f'area_avg|{area_descr}|{(asoma / aqtde):.2f}')

    # QUESTÃO 3
    max_area_qtde = max(a[3] for a in ais.values())
    min_area_qtde = min(a[3] for a in ais.values())

    for area, info in ais.items():
        if info[3] == max_area_qtde:
            out(f'most_employees|{areas_descr[area]}|{max_area_qtde}')
        if info[3] == min_area_qtde:
            out(f'least_employees|{areas_descr[area]}|{min_area_qtde}')

    # QUESTÃO 4
    for info in sis.values():
        if info[1] > 1:
            for func in info[2]:
                sob = func['sobrenome']
                out(f'last_name_max|{sob}|{func["nome"]} {sob}|{func["salario"]:.2f}')

    print("\n".join(output))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]}  filename.json')
        sys.exit(2)

    gerar_saida(*processar(sys.argv[1]))
