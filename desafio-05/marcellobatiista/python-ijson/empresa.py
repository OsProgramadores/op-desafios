"""
##!------------------------------+"
##!                              !"
##!          Mano Tchelo         !"
##!                              !"
##!------------------------------+"
##
##
##
##
##
##
##
"""

from operator import itemgetter
from collections import deque
import sys
import ijson


class Stream:
    """Classe Stream"""

    queue = deque(maxlen=40)
    queue_area = {}
    queue_sobre = {}

    dic = {}
    company = None

    def __init__(self):

        self.company = Empresa()

        path = sys.argv[1].replace('\\', '/')
        with open(path, 'r', encoding='utf-8-sig') as file:
            self.stream_json(file)

    def stream_json(self, file):
        """Stream json"""

        for prefix, the_type, value in ijson.parse(file):
            if 'funcionarios' in prefix:
                self.run_tasks(prefix, the_type, value)
            elif 'areas' in prefix:
                self.run_tasks(prefix, the_type, value)

        values = self.company.ctsum_area.values()
        most_least = sorted(values, key=itemgetter('cont_fun'), reverse=True)
        self.company.show(self.queue, self.queue_area, most_least, self.queue_sobre)

    def run_tasks(self, prefix, the_type, value):
        """Faz o processo de criar chaves e valores"""

        self.set_key(the_type, value)
        self.set_value(prefix, the_type, value)
        self.process_dict(prefix, the_type)

    def set_key(self, the_type, value):
        """Cria a chave da iteração atual"""

        if the_type == 'map_key':
            self.dic[value] = None

    @classmethod
    def get_key(cls, prefix):
        """Splita o prefixo e retorna a chave da iteração anterior"""

        return prefix.split('.')[-1]

    def set_value(self, prefix, the_type, value):
        """Seta o valor na chave da iteração anterior"""

        if self.get_key(prefix) in self.dic.keys():
            value = value if the_type != 'number' else float(value)
            self.dic[self.get_key(prefix)] = value

    def process_dict(self, prefix, the_type):
        """Dispacha o dicionário depois de formado"""

        if the_type == 'end_map':
            dic = self.dic.copy()
            self.company.set_prefix(prefix)
            self.company.queue_walk(self.queue, self.queue_area, self.queue_sobre, dic)
            self.dic.clear()


class Empresa:
    """Classe Empresa"""

    sum_avg = 0
    cont_fun = 0
    areas = {}
    ctsum_area = {}

    prefix = None

    def set_prefix(self, prefix):
        """Só pra diminuir a qt de argumentos"""

        self.prefix = prefix

    def queue_walk(self, queue, queue_area, queue_sobre, dic):
        """Faz a fila andar"""

        if 'areas' in self.prefix:  # bag
            self.areas[dic['codigo']] = dic['nome']
        else:
            self.queue_global(queue, dic)
            self.queue_walk_area(queue_area, dic)
            self.queue_walk_sobre(queue_sobre, dic)

    def queue_global(self, queue, dic):
        """Questão 1"""

        self.global_sum(dic)
        self.init_queue(queue, dic)

    def queue_walk_area(self, queue_area, dic):
        """Questões 2 & 3"""

        if dic['area'] in queue_area.keys():
            self.global_sum(dic, question=2)
            self.init_queue(queue_area[dic['area']], dic)
        else:
            queue_area[dic['area']] = deque(maxlen=40)
            queue_area[dic['area']].append(dic)
            value = {'cod': dic['area'], 'sum_avg': dic['salario'], 'cont_fun': 1}
            self.ctsum_area[dic['area']] = value

    def queue_walk_sobre(self, queue_sobre, dic):
        """Questão 4"""

        if dic['sobrenome'] in queue_sobre.keys():
            self.init_queue(queue_sobre[dic['sobrenome']], dic)
        else:
            queue_sobre[dic['sobrenome']] = deque(maxlen=40)
            queue_sobre[dic['sobrenome']].append(dic)

    def init_queue(self, queue, dic):
        """Add primeiro dic na fila e processa após o else"""

        if queue.__len__() != 0:
            self.max_map(queue, dic)
        else:
            queue.append(dic)

    @classmethod
    def max_map(cls, queue, dic):
        """Pega o salário máximo/mínimo e adiciona
           na frente ou no final da fila.
        """

        if dic['salario'] >= max(map(lambda x: x['salario'], queue)):
            queue.appendleft(dic)
        elif dic['salario'] <= min(map(lambda x: x['salario'], queue)):
            queue.append(dic)

    def global_sum(self, dic, question=1):
        """Soma salário e funcionários"""

        if question == 1:
            self.sum_avg += dic['salario']
            self.cont_fun += 1
        elif question == 2:
            self.ctsum_area[dic['area']]['sum_avg'] += dic['salario']
            self.ctsum_area[dic['area']]['cont_fun'] += 1

    def global_avg(self, area=None):
        """Média salarial dos funcionários"""

        if area is None:
            return '%.2f' % (self.sum_avg / self.cont_fun)
        return '%.2f' % (self.ctsum_area[area]['sum_avg'] / self.ctsum_area[area]['cont_fun'])

    @classmethod
    def global_all(cls, queue, gmax=0, key='salario'):
        """Retorna os funcionários com o maior e/ou menor salário
           gmax: 0 --> Primeiro funcionário da fila
           gmax: -1 --> Último funcionário da fila
        """

        biglesser = [x for x in queue if x[key] == queue[gmax][key]]

        return biglesser

    def show(self, queue, queue_area, most_least, queue_sobre):
        """Show main"""

        args1 = {'avg': 'global_avg', 'area': None, 'key': 'salario'}
        self.show_global(queue, ['global_max', 'global_min'], args1)
        for area in queue_area:
            args2 = {'avg': 'area_avg', 'area': area, 'key': 'salario'}
            self.show_global(queue_area[area], ['area_max', 'area_min'], args2)

        args3 = {'avg': None, 'area': None, 'key': 'cont_fun'}
        self.show_global(most_least, ['most_employees', 'least_employees'], args3)
        for sobre in queue_sobre:
            for value in self.global_all(queue_sobre[sobre]):
                if len(queue_sobre[sobre]) > 1:
                    self.view_four(value)

    def show_global(self, queue, label, args):
        """Método gambiarrento por causa do pylint,
           mas tudo bem, é só esse e o view() - refactor dps
        """

        avg = args['avg']
        area = args['area']
        key = args['key']

        nar = '|' + self.areas[area] if area is not None else ''
        args['area'] = nar

        for direc in [0, -1]:
            for value in self.global_all(queue, gmax=direc, key=key):
                self.view(direc, label, value, args)

        if key == 'salario':
            print(avg + nar + '|' + str(self.global_avg(area)))

    def view(self, direc, label, value, args):
        """Views questões 1,2 e 3"""

        area = args['area']
        key = args['key']

        if key == 'salario':
            lbl = label[direc * -1] + area
            nome = value['nome'] + ' ' + value['sobrenome']
            print(lbl + '|' + nome + '|%.2f' % value['salario'])
        else:
            print(label[direc * -1] + '|' + self.areas[value['cod']] + '|' + str(value['cont_fun']))

    @classmethod
    def view_four(cls, value):
        """View questão 4"""

        nome = value['nome']
        sobrenome = value['sobrenome']
        salario = '|%.2f' % value['salario']
        print('last_name_max|' + sobrenome + '|' + nome + ' ' + sobrenome + salario)


if __name__ == "__main__":
    Stream()
