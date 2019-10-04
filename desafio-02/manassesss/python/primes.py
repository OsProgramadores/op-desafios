def isPrime(k):
	c = 1
	for i in range(2, k-1):
		if k%2 != 0 or i == 2:
			if k%i == 0 :
				c = c+1
			if c > 2:
				break
	if c+1 == 2 :
		print(k)

for i in range(2, 10):
    isPrime(i)
