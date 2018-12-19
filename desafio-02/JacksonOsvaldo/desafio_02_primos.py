#!/usr/bin/env python3
#-*- ecoding: utf-8 -*-

"""
Resposta de Jackson Osvaldo da Silva Braga
GitHub: https://github.com/JacksonOsvaldo
E-mail: jacksonosvaldo@live.com
"""


def primo(numero):
	num = 0
	for i in range(numero):
		resto = numero%(i+1)
		if resto == 0:
			num = num + 1
		if num > 2:
			break
	if num == 2:
		return True
	else:
		return False

for i in range(10000):
	testeprimo = primo(i)
	if testeprimo == True:
		print('O número primo é: {}'.format(i))
