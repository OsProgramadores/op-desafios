
import sys
import json
from collections import Counter


def load(filename):
    with open(filename) as r:
        return json.loads(r.read())

def avg(values):
    return sum(values) / len(values)


def print_emps_for_area(empl_count):

    max_count = max(empl_count.values())
    min_count = min(empl_count.values())

    for k, v in empl_count.items():
        if v == max_count:
            print(f'most_employees|{k}|{v}')

        if v == min_count:
            print(f'least_employees|{k}|{v}')

def print_last_names(last_names, data):
    total = Counter(last_names)

    valid_names = [k for k, v in total.items() if v > 1]

    for current in valid_names:
        funcs = [f for f in data['funcionarios']
                  if f['sobrenome'] == current]

        max_salary = max([f['salario'] for f in funcs])

        for func in [f for f in funcs if f['salario'] == max_salary]:
            func_nome = func['nome'] + ' ' + current
            print (f'last_name_max|{current}|{func_nome}|{max_salary:.2f}')


def main():
    data = load(sys.argv[1])
    salaries = [func['salario'] for func in data['funcionarios']]

    last_names = list()
    max_sal = max(salaries)
    min_sal = min(salaries)
    avg_sal = avg(salaries)
    empl_count = dict()

    for area in data['areas']:
        nome = area['nome']
        area_funcs = [fun for fun in data['funcionarios']
                         if fun['area'] == area['codigo']]

        empl_count[nome] = len(area_funcs)
        area_salaries = [fun['salario'] for fun in area_funcs]
        max_area = max(area_salaries)
        min_area = min(area_salaries)
        avg_area = avg(area_salaries)

        for fun in area_funcs:
            func_nome = fun['nome'] + ' ' + fun['sobrenome']
            func_salario = fun['salario']
            last_names.append(fun['sobrenome'])

            if func_salario == max_area:
                print(f'area_max|{nome}|{func_nome}|{func_salario:.2f}')
            elif func_salario == min_area:
                print(f'area_min|{nome}|{func_nome}|{func_salario:.2f}')

        print(f'area_avg|{nome}|{avg_area:.2f}')

    for func in [f for f in data['funcionarios'] if f['salario'] == max_sal]:
        print('global_max|{} {}|{:.2f}'
              .format(func['nome'], func['sobrenome'], func['salario']))

    for func in [f for f in data['funcionarios'] if f['salario'] == min_sal]:
        print('global_min|{} {}|{:.2f}'
              .format(func['nome'], func['sobrenome'], func['salario']))

    print_emps_for_area(empl_count)
    print_last_names(last_names, data)
    print(f'global_avg|{avg_sal:.2f}')


if __name__ == '__main__':
    main()
