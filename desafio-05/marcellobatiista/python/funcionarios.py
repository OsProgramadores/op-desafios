#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
#import time

class Empresa:

    dados = None
    
    #Funcionarios | Areas | Quantidade
    funcionarios = {'fun':None, 'area':None, 'quant':0}
    fun_por_area = {}
    
    def __init__(self, path = None):
        caminho = ''
        if (path == None):
            caminho = sys.argv[1].replace('\\', '/')
        else:
            caminho = path
        '''
        i = time.time()
        self.abrir(caminho)
        f = time.time() - i
        print('\nTempo: %.2f' % f)
        '''
        
    def abrir(self, caminho):
        print('[!] Abrindo arquivo...')
        with open(caminho, 'r', encoding='utf-8-sig') as arquivo:
            self.dados = json.load(arquivo)
        print('[!] Colentando funcionarios...')
        self.funcionarios['fun'] = self.dados['funcionarios']
        self.funcionarios['quant'] = len(self.funcionarios['fun'])
        print('[!] Caletando areas...')
        self.funcionarios['area'] = self.dados['areas']
        print('\n[!] Processamento iniciado. Aguarde...\n')
        self.quemMaisMenosRecebeMaisMedia(self.funcionarios['fun'], 1)
        self.agruparFuncionariosPorAreaEMaisMenosMaisMedia()
        #print('')
        self.AreaMaiorMenorFuncionarios()
        #print('')
        self.agruparFuncionariosSobrenome()
        print('\n[!] Processamento concluido com sucesso!')

    def agruparFuncionariosPorAreaEMaisMenosMaisMedia(self):
        for fun in self.funcionarios['fun']:
            for area in self.funcionarios['area']:
                if (fun['area'] == area['codigo']):
                    try:
                        self.fun_por_area[area['nome']].append(fun)
                    except:
                        self.fun_por_area[area['nome']] = [fun]

        for area in self.fun_por_area:
            #print('')
            self.quemMaisMenosRecebeMaisMedia(self.ordenarSalario(self.fun_por_area[area]), 2)
            
    def ordenarSalario(self, funcionarios):
        tmp = [funcionarios[0]]
        
        i = 0
        while (i < len(funcionarios)-1):
            if (funcionarios[i+1]['salario'] > tmp[0]['salario']):
                tmp.insert(0, funcionarios[i+1])
            else:
                existe = False
                for j in enumerate(tmp):
                    if (funcionarios[i+1]['salario'] >= j[1]['salario']):
                        tmp.insert(j[0], funcionarios[i+1])
                        existe = True
                        break
                if not(existe):
                    tmp.append(funcionarios[i+1])
            i += 1

        return tmp
    
    def quemMaisMenosRecebeMaisMedia(self, funcionarios, questao):
        ordem = self.ordenarSalario(funcionarios)
        
        MAX = ordem[0]['salario']
        for fun_max in ordem:
            if (fun_max['salario'] == MAX):
                if (questao == 1):
                    print('global_max|'+fun_max['nome']+' '+fun_max['sobrenome']+'|%.2f' % fun_max['salario'])
                elif (questao == 2):
                    for area in self.funcionarios['area']:
                        if (fun_max['area'] == area['codigo']):
                            print('global_max|'+area['nome']+'|'+fun_max['nome']+' '+fun_max['sobrenome']+'|%.2f' % fun_max['salario'])
                            break
                else:
                    print('last_name_max|'+fun_max['sobrenome']+'|'+fun_max['nome']+' '+fun_max['sobrenome']+'|%.2f' % fun_max['salario'])
            else:
                break

        MIN = ordem[len(ordem)-1]['salario']
        for f in range(len(ordem)-1,-1,-1):
            if (ordem[f]['salario'] == MIN):
                if (questao == 1):
                    print('global_min|'+ordem[f]['nome']+' '+ordem[f]['sobrenome']+'|%.2f' % ordem[f]['salario'])
                elif (questao == 2):
                    for area in self.funcionarios['area']:
                        if (fun_max['area'] == area['codigo']):
                            print('global_min|'+area['nome']+'|'+ordem[f]['nome']+' '+ordem[f]['sobrenome']+'|%.2f' % ordem[f]['salario'])
                            break
            else:
                break
            
        SOMA = 0
        for fun in ordem:
            SOMA += fun['salario']
        if (questao == 1):
            print('global_avg|%.2f' % (SOMA/len(ordem)))
        elif (questao == 2):
            for fun in ordem:
                for area in self.funcionarios['area']:
                    if (fun['area'] == area['codigo']):
                        print('global_avg|'+area['nome']+'|%.2f' % (SOMA/len(ordem)))
                        break
                break

    def AreaMaiorMenorFuncionarios(self):
        quant = {}
        for area in self.fun_por_area:
            quant[area] = len(self.fun_por_area[area])

        MINMAX = sorted(quant, key=quant.get)

        MAX = quant[MINMAX[len(MINMAX)-1]]
        for area in MINMAX:
            if (quant[area] == MAX):
                print('most_employees|'+area+'|'+str(quant[area]))

        
        MIN = quant[MINMAX[0]]
        for area in MINMAX:
            if (quant[area] == MIN):
                print('least_employees|'+area+'|'+str(quant[area]))

    def agruparFuncionariosSobrenome(self):
        fun = {}
        for funcio in self.funcionarios['fun']:
            try:
                fun[funcio['sobrenome']].append(funcio)
            except:
                fun[funcio['sobrenome']] = [funcio]

        for sobrenome in fun:
            if (len(fun[sobrenome]) > 1):
                ordem = self.ordenarSalario(fun[sobrenome])
                self.quemMaisMenosRecebeMaisMedia(ordem, 3)
        
Empresa()
