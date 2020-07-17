"""
    Resolucao Desafio 4
    por: Gabriel Rocha
    github: G4BR13LR0CH4

"""
tabuleiro = []
peca = {"Peao" : 1, "Bispo" : 2, "Cavalo" : 3, "Torre": 4, "Rainha" : 5, "Rei" : 6}

def criacao():
    """Posiciona as pecas do tabuleiro"""
    print("Por favor preencha o Tabuleiro, lembre-se que voce esta preenchendo da esquerda para direita da parte inferior")
    print("obs: caso nao queira colocar nenhum peca naquela coordenada adicionar valor 0")

    for x in range(64):
        aux = int(input("Digite o id da peca: "))
        tabuleiro.append(aux)

def cont(aux, clone):
    while aux in clone:
        clone.remove(aux)
    return len(clone)

criacao()
for key in peca:
    aux = cont(peca[key], tabuleiro[:])
    peca[key] = 64 - int(aux)

print("\nPeão: " + str(peca['Peao']) + " peça(s)")
print("Bispo: " + str(peca['Bispo']) + " peça(s)")
print("Cavalo: " + str(peca['Cavalo']) + " peça(s)")
print("Torre: " + str(peca['Torre']) + " peça(s)")
print("Rainha: " + str(peca['Rainha']) + " peça(s)")
print("Rei: " + str(peca['Rei']) + " peça(s)")
