"programa que conta peças do tabuleiro de xadrez "
def le_peao(matriz):
    "conta peao"
    count = 0
    for i in matriz:
        while i == 1:
            count +=1
            break
    return count

def le_rei(matriz):
    "conta rei"
    count =0
    for i in matriz:
        while i == 6:
            count += 1
            break
    return count

def le_rainha(matriz):
    "conta rainha"
    count = 0
    for i in matriz:
        while i == 5:
            count += 1
            break
    return count

def le_torre(matriz):
    "conta torre"
    count = 0
    for i in matriz:
        while i == 4:
            count +=1
            break
    return count

def le_bispo(matriz):
    "conta bispo"
    count =0
    for i in matriz:
        while i == 2:
            count += 1
            break
    return count

def le_cavalo(matriz):
    "conta cavalo"
    count = 0
    for i in matriz:
        while i == 3:
            count += 1
            break
    return count

def main():
    "Função main do programa"
    tabuleiro= [4, 3, 2, 5, 6, 2, 3, 4,
    1,1, 1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    1,1, 1, 1, 1, 1, 1, 1,
    4, 3, 2, 5, 6, 2, 3, 4]

    print(f'Peão:  {le_peao(tabuleiro)} peças(s)')
    print(f'Bispo:  {le_bispo(tabuleiro)} peças(s)')
    print(f'Cavalo:  {le_cavalo(tabuleiro)} peças(s)')
    print(f'Torre:  {le_torre(tabuleiro)} peças(s)')
    print(f'Rainha:  {le_rainha(tabuleiro)} peças(s)')
    print(f'Rei:  {le_rei(tabuleiro)} peças(s)')

if __name__ == "__main__":
    main()
