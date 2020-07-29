"""
    Resolucao Desafio 4
    por: Gabriel Rocha
    github: G4BR13LR0CH4

"""
tabuleiro = []
peca = {"Peao" : 1, "Bispo" : 2, "Cavalo" : 3, "Torre": 4, "Rainha" : 5, "Rei" : 6}

def criacao():
    """Posiciona as pecas do tabuleiro"""
    for x in range(64):
        print("Casa: " + str(x))
        arm_peca = int(input("Digite o id da peca: "))
        tabuleiro.append(arm_peca)

def cont(flag, clone):
    """Faz a contagem das pecas"""
    while flag in clone:
        clone.remove(flag)
    return len(clone)

criacao()
for key in peca:
    aux = cont(peca[key], tabuleiro[:])
    peca[key] = 64 - int(aux)

for key in peca:
    print(key + ": " + str(peca[key]) + " peças")
