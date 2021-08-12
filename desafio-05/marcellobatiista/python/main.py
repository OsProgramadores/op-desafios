'''Resolução do Desafio 5'''

from operator import itemgetter
import sys
import json

class Company:
    '''Classe empresa'''
    data = None
    group = None

    def __init__(self):
        path = sys.argv[1].replace('\\', '/')
        with open(path, 'r', encoding='utf-8-sig') as file:
            self.data = json.load(file)

        order = self.order(self.data['funcionarios'])

        self.showfor('global_max', self.global_max(order))
        self.showfor('global_min', self.global_min(order))
        print('global_avg|'+str(self.global_avg(order)))

        self.group = self.areas()
        self.area_main()
        self.most_employees()
        self.name_max()

    @classmethod
    def order(cls, emp_list, key='salario'):
        '''idem'''
        return sorted(emp_list, key=itemgetter(key), reverse=True)

    def showfor(self, label, employee_list, label_area=''):
        '''format out'''
        label_area = self.adbar(label_area)

        for emp in employee_list:
            if not 'quant' in emp.keys():
                nome = emp['nome']+' '+emp['sobrenome']
                print(label+label_area+'|'+nome+'|%.2f' % emp['salario'])
            else:
                print(label+label_area+'|'+str(emp['quant']))
    @classmethod
    def adbar(cls, label):
        '''add bar'''
        return '|'+label if label != '' else label

    @classmethod
    def global_max(cls, order, key='salario'):
        '''higher payouts'''
        maxrs = []
        last = order[0]
        for pay_max in order:
            if pay_max[key] != last[key]:
                break
            last = pay_max
            maxrs.append(last)
        return maxrs

    @classmethod
    def global_min(cls, order, key='salario'):
        '''lower payment'''
        mins = []
        last = order[len(order)-1]
        for pay_min in range(len(order)-1, 0, -1):
            if order[pay_min][key] != last[key]:
                break
            last = order[pay_min]
            mins.append(last)
        return mins

    @classmethod
    def global_avg(cls, order, key='salario'):
        '''pay average'''
        avg = round((sum([x[key] for x in order]))/len(order), 2)
        return avg

    def areas(self):
        '''invert areas and add employee'''
        union = {}
        for cod in self.data['areas']:
            valueslist = list(cod.values())
            union[valueslist[0]] = {'nome':valueslist[1], 'F':[]}

        for fun in self.data['funcionarios']:
            union[fun['area']]['F'].append(fun)
        return union

    def area_main(self):
        '''areas payouts'''
        areas = self.group
        for area in areas:
            order = self.order(areas[area]['F'])

            if len(order) <= 0: #Area not found
                continue

            self.showfor('area_max', self.global_max(order), areas[area]['nome'])
            self.showfor('area_min', self.global_min(order), areas[area]['nome'])
            print('area_avg|'+areas[area]['nome']+'|'+str(self.global_avg(order)))

    def most(self):
        '''cont_employees'''
        areas = self.group
        area_list = []
        for area in areas:
            if len(areas[area]['F']) < 1: #Area not found
                continue
            area_list.append({'area':areas[area]['nome'], 'quant':len(areas[area]['F'])})
        return area_list

    def most_employees(self):
        '''most and least'''
        order = self.order(self.most(), 'quant')
        most = self.global_max(order, 'quant')
        least = self.global_min(order, 'quant')
        for area_most, area_least in zip(most, least):
            self.showfor('most_employees', most, area_most['area'])
            self.showfor('least_employees', least, area_least['area'])

    def name_max(self):
        '''name pay'''
        fun = self.data['funcionarios']
        sobrenomes = {f['sobrenome']:[] for f in fun}
        for ifun in fun:
            sobrenomes[ifun['sobrenome']].append(ifun)

        for ifun in list(sobrenomes):
            if len(sobrenomes[ifun]) < 2:
                sobrenomes.__delitem__(ifun)

        for sobn in list(sobrenomes):
            order = self.order(sobrenomes[sobn])
            self.showfor('last_name_max', self.global_max(order), sobn)

if __name__ == "__main__":
    Company()
