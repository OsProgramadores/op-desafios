"""
Author: Israel Matos
Date: 07/04/22,
Description: solution for challenge 02(https://osprogramadores.com/desafios/d02/)
"""

for n in range(2, 10000):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(n)
