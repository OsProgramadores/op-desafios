""" Desafio 5 """

import json
import sys

class Empresa:
    """ Classe de processamento """
    dados = None

    #Funcionarios | Areas | Quantidade
    funcionarios = {'fun':None, 'area':None, 'quant':0}
    fun_por_area = {}

    def __init__(self, path=None):
        caminnho = ''
        if path is None:
            caminnho = sys.argv[1].replace('\\', '/')
        else:
            caminnho = path
        self.abrir(caminnho)

    def abrir(self, caminnho):
        ''' Inicia o script '''

        print('[!] Abrindo arquivo...')
        with open(caminnho, 'r', encoding='utf-8-sig') as arquivo:
            self.dados = json.load(arquivo)
        print('[!] Colentando funcionarios...')
        self.funcionarios['fun'] = self.dados['funcionarios']
        self.funcionarios['quant'] = len(self.funcionarios['fun'])
        print('[!] Caletando areas...')
        self.funcionarios['area'] = self.dados['areas']
        print('\n[!] Processamento iniciado. Aguarde...\n')
        self.quem_maismenos(self.funcionarios['fun'], 1)
        self.agrupa_funcionarios()
        #print('')
        self.area_maior_menor_funcionarios()
        #print('')
        self.agrupa_funcionarios_sobrenome()
        print('\n[!] Processamento concluido com sucesso!')

    def agrupa_funcionarios(self):
        ''' Agrupa funcionarios '''

        for fun in iter(self.funcionarios['fun']):
            for area in iter(self.funcionarios['area']):
                if fun['area'] == area['codigo']:
                    try:
                        self.fun_por_area[area['nome']].append(fun)
                    except KeyError:
                        self.fun_por_area[area['nome']] = [fun]

        for area in self.fun_por_area:
            #print('')
            self.quem_maismenos(self.ordenar_salario(self.fun_por_area[area]), 2)

    @classmethod
    def ordenar_salario(cls, funcionarios):
        ''' Ordena salario '''

        tmp = [funcionarios[0]]

        i = 0
        while i < len(funcionarios)-1:
            if funcionarios[i+1]['salario'] > tmp[0]['salario']:
                tmp.insert(0, funcionarios[i+1])
            else:
                existe = False
                for j in enumerate(tmp):
                    if funcionarios[i+1]['salario'] >= j[1]['salario']:
                        tmp.insert(j[0], funcionarios[i+1])
                        existe = True
                        break
                if not existe:
                    tmp.append(funcionarios[i+1])
            i += 1

        return tmp

    def salario_max(self, ordem, questao):
        ''' Salario maximo '''

        maxx = ordem[0]['salario']
        for fun_maxx in ordem:
            nome = fun_maxx['nome']
            sobrenome = fun_maxx['sobrenome']
            salario = fun_maxx['salario']
            if salario == maxx:
                if questao == 1:
                    print('global_max|'+nome+' '+sobrenome+'|%.2f' % salario)
                elif questao == 2:
                    for area in iter(self.funcionarios['area']):
                        if fun_maxx['area'] == area['codigo']:
                            narea = area['nome']
                            print('global_max|'+narea+'|'+nome+' '+sobrenome+'|%.2f' % salario)
                            break
                else:
                    print('last_name_maxx|'+sobrenome+'|'+nome+' '+sobrenome+'|%.2f' % salario)
            else:
                break

    def salario_min(self, ordem, questao):
        ''' Salario minimo '''

        minn = ordem[len(ordem)-1]['salario']
        for funcio in range(len(ordem)-1, -1, -1):
            nome = ordem[funcio]['nome']
            sobrenome = ordem[funcio]['sobrenome']
            salario = ordem[funcio]['salario']
            if ordem[funcio]['salario'] == minn:
                if questao == 1:
                    print('global_min|'+nome+' '+sobrenome+'|%.2f' % salario)
                elif questao == 2:
                    for area in iter(self.funcionarios['area']):
                        if ordem[funcio]['area'] == area['codigo']:
                            narea = area['nome']
                            print('global_min|'+narea+'|'+nome+' '+sobrenome+'|%.2f' % salario)
                            break
            else:
                break
    def media_salarial(self, ordem, questao):
        ''' Media salarial '''

        soma = 0
        for fun in ordem:
            soma += fun['salario']
        if questao == 1:
            print('global_avg|%.2f' % (soma/len(ordem)))
        elif questao == 2:
            for fun in ordem:
                for area in iter(self.funcionarios['area']):
                    if fun['area'] == area['codigo']:
                        print('global_avg|'+area['nome']+'|%.2f' % (soma/len(ordem)))
                        break
                break

    def quem_maismenos(self, funcionarios, questao):
        ''' Mais menos recebe '''

        ordem = self.ordenar_salario(funcionarios)

        self.salario_max(ordem, questao)
        self.salario_min(ordem, questao)
        self.media_salarial(ordem, questao)


    def area_maior_menor_funcionarios(self):
        ''' Area maior menor funcionarios '''

        quant = {}
        for area in self.fun_por_area:
            quant[area] = len(self.fun_por_area[area])

        minnmaxx = sorted(quant, key=quant.get)

        maxx = quant[minnmaxx[len(minnmaxx)-1]]
        for area in minnmaxx:
            if quant[area] == maxx:
                print('most_employees|'+area+'|'+str(quant[area]))


        minn = quant[minnmaxx[0]]
        for area in minnmaxx:
            if quant[area] == minn:
                print('least_employees|'+area+'|'+str(quant[area]))

    def agrupa_funcionarios_sobrenome(self):
        ''' Funcionarios sobrenome '''

        fun = {}
        for funcio in iter(self.funcionarios['fun']):
            try:
                fun[funcio['sobrenome']].append(funcio)
            except KeyError:
                fun[funcio['sobrenome']] = [funcio]

        for sobrenome in fun:
            if len(fun[sobrenome]) > 1:
                ordem = self.ordenar_salario(fun[sobrenome])
                self.quem_maismenos(ordem, 3)

Empresa()
