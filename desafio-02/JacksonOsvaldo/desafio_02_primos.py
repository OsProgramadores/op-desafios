#!/usr/bin/env python3
#-*- ecoding: utf-8 -*-

"""
Resposta de Jackson Osvaldo da Silva Braga
GitHub: https://github.com/JacksonOsvaldo
E-mail: jacksonosvaldo@live.com
"""


def primo(numero):
	a = 0
	for i in range(numero):
		if i == 0:
			continue
		else:
			resto = numero%i
			if resto == 0:
				a = a + 1
			if a > 2:
				break
	if a == 2:
		return True
	else:
		return False

for i in range(10001):
	testeprimo = primo(i)
	if testeprimo == True or i == 2:
		print('O número primo é: {}'.format(i))
	# if i >= 0 and i%2 == 0:
	# 	print('O número par é: {}'.format(i))