import sys
import json
import mmap
from collections import defaultdict

class Funcionario:
    __slots__ = ['nome', 'sobrenome', 'salario', 'area']

    def __init__(self, func: dict):
        self.nome = func['nome']
        self.sobrenome = func['sobrenome']
        self.salario = func['salario']
        self.area = func['area']


class ByEmployeesMinMax:
    __slots__ = ['min', 'max', 'list_min', 'list_max']

    def __init__(self, min, max, list_min, list_max):
        self.min = min
        self.max = max
        self.list_min = list_min
        self.list_max = list_max


class Stats:
    __slots__ = ['globally', 'by_area', 'by_employees', 'by_lastname']

    def __init__(self):
        self.globally = GlobalStats()
        self.by_area = defaultdict(GlobalStats)
        self.by_employees = defaultdict(lambda: 0)
        self.by_lastname = defaultdict(MaxStats)

    def update(self, func: Funcionario):
        # Global
        self.globally.update(func)

        # By Area
        area = func.area
        self.by_area[area].update(func)

        # By Employees
        self.by_employees[area] += 1

        # By Lastname
        self.by_lastname[func.sobrenome].update(func)


class GlobalStats:
    __slots__ = ['min', 'max', 'list_min', 'list_max', 'salary_sum', 'count']

    def __init__(self):
        self.min = float('inf')
        self.max = float('-inf')
        self.list_min = []
        self.list_max = []
        self.salary_sum = 0.0
        self.count = 0

    def update(self, func: Funcionario):
        self.salary_sum += func.salario
        self.count += 1

        salario = func.salario

        if salario < self.min:
            self.min = salario
            self.list_min.clear()
            self.list_min.append(func)
        elif salario == self.min:
            self.list_min.append(func)

        if salario > self.max:
            self.max = salario
            self.list_max.clear()
            self.list_max.append(func)
        elif salario == self.max:
            self.list_max.append(func)

    def average(self):
        return self.salary_sum / self.count


class MaxStats:
    __slots__ = ['max', 'list', 'count']

    def __init__(self):
        self.max = float('-inf')
        self.list = []
        self.count = 0

    def update(self, func: Funcionario):
        self.count += 1

        salario = func.salario

        if salario > self.max:
            self.max = salario
            self.list.clear()
            self.list.append(func)
        elif salario == self.max:
            self.list.append(func)


def by_employees_min_max(by_employees):
    size_min = float('inf')
    size_max = float('-inf')
    list_min = []
    list_max = []

    for area, employees in by_employees.items():
        if employees < size_min:
            size_min = employees
            list_min.clear()
            list_min.append(area)
        elif employees == size_min:
            list_min.append(area)

        if employees > size_max:
            size_max = employees
            list_max.clear()
            list_max.append(area)
        elif employees == size_max:
            list_max.append(area)

    return ByEmployeesMinMax(size_min, size_max, list_min, list_max)


def main(file: str):
    # Read file
    with open(file) as f:
        data = json.load(f)

    funcionarios = data['funcionarios']
    areas = {area['codigo']: area['nome'] for area in data['areas']}
    del data

    # Calculate stats
    stats = Stats()

    for func in funcionarios:
        stats.update(Funcionario(func))

    # Stats: Destructure
    globally = stats.globally
    by_area = stats.by_area
    by_employees = stats.by_employees
    by_lastname = stats.by_lastname
    del stats

    # Print stats: Global
    salary_min = globally.min
    for func in globally.list_min:
        print(f'global_min|{func.nome} {func.sobrenome}|{salary_min:.2f}')

    salary_max = globally.max
    for func in globally.list_max:
        print(f'global_max|{func.nome} {func.sobrenome}|{salary_max:.2f}')

    print(f"global_avg|{globally.average():.2f}")
    del globally

    # Print stats: By area
    for area_code, area_stats in by_area.items():
        area_name = areas[area_code]

        area_min = area_stats.min
        for func in area_stats.list_min:
            print(
                f'area_min|{area_name}|{func.nome} {func.sobrenome}|{area_min:.2f}')

        area_max = area_stats.max
        for func in area_stats.list_max:
            print(
                f'area_max|{area_name}|{func.nome} {func.sobrenome}|{area_max:.2f}')

        print(f'area_avg|{area_name}|{area_stats.average():.2f}')

    del by_area

    # Print stats: By employees
    employees_min_max = by_employees_min_max(by_employees)

    employees_min = employees_min_max.min
    for area_code in employees_min_max.list_min:
        area_name = areas[area_code]
        print(f'least_employees|{area_name}|{employees_min}')

    employees_max = employees_min_max.max
    for area_code in employees_min_max.list_max:
        area_name = areas[area_code]
        print(f'most_employees|{area_name}|{employees_max}')

    del by_employees
    del employees_min_max

    # Print stats: By lastname
    for lastname, lastname_stats in by_lastname.items():
        if lastname_stats.count < 2:
            continue

        lastname_max = lastname_stats.max
        for func in lastname_stats.list:
            print(
                f'last_name_max|{lastname}|{func.nome} {lastname}|{lastname_max:.2f}')

    del by_lastname


if __name__ == "__main__":
    main(sys.argv[1])
