import sys
def create(indice, j):
    n = indice
    result = indice

    if j % 2 != 0:
        n = n // 10

    while n > 0:
        result = result * 10 + (n % 10)
        n = n // 10
    return result
  
def print_next(ls, fim):
    ls.sort()
    while ls:
        val = ls.pop(0)
        if val > fim:
            break
        print(val)
        
def main():
    buffer = list()
    
    inicio = int(sys.argv[1])
    fim = int(sys.argv[2])
    max_buffer = fim // 100
    if max_buffer < 10000: 
        max_buffer = 10000
    finalizar = False
    faixas = ((i, (i+max_buffer)) for i in range(1,fim, max_buffer))
   
    for rng in faixas:
        for j in range(2):
            for sequencia in range(*rng):
        
                valor = create(sequencia, j)
                if valor > fim:
                    finalizar = True
                else:
                    buffer.append(valor)
        print_next(buffer, fim)
        if finalizar:
            break
       
    print_next(buffer, fim)
        
if __name__ == '__main__':

    main()
        

