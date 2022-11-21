'''
Diga se um número é potência de 2 ou não e quantas vezes se deve elevar 2 para alcança-lo.
'''
with open('d12.txt', encoding='utf-8') as archive_for_d12:
    BASES = archive_for_d12.readlines()


def base_function(result_of_elevation, counter=0):
    """Osprogramadores.com"""

    while result_of_elevation >= 1:

        if result_of_elevation == 1:
            return ' '.join(['true', str(counter)])
        if (result_of_elevation % 2) != 0:
            return 'false'

        result_of_elevation = result_of_elevation // 2
        counter += 1
    return 'false'

for base in BASES:
    base = int(base)
    calling_function = base_function(base)
    print(base, calling_function)
