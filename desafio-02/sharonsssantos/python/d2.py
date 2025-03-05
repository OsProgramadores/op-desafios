def isqrt(num):
	""" Função que recebe 'num' e retorna a raiz quadrada inteira de 'num' """
	return int(num ** 0.5)

def crivo(limit):
	""" Implementação do Crivo de Eratóstenes """
	if limit < 2:
		return []
	
	primos = [1] * (limit + 1)
	primos[0], primos[1] = 0, 0
	
	for i in range(2, (isqrt(limit)+1)):
		for j in range(i*i, (limit+1), i):
			if primos[j]:
				primos[j] = 0
	
	primos = [num for num in range(limit+1) if primos[num]]
	return primos

print(crivo(10000))
