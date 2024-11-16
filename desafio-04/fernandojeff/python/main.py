def contabilizar_pecas(tabuleiro):
    # Dicionário para associar o código ao nome da peça
    pecas = {
        1: "Peão",
        2: "Bispo",
        3: "Cavalo",
        4: "Torre",
        5: "Rainha",
        6: "Rei"
    }
    
    # Inicializa o contador de peças
    contagem = {i: 0 for i in range(7)}
    
    # Conta cada peça no tabuleiro
    for linha in tabuleiro:
        for valor in linha:
            contagem[valor] += 1
    
    # Exibe o resultado
    for codigo, nome in pecas.items():
        print(f"{nome}: {contagem[codigo]} peça(s)")

#ENTRADAS NO TABULEIRO
# Exemplo 1
tabuleiro1 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Exemplo 2
tabuleiro2 = [
    [4, 3, 2, 5, 6, 2, 3, 4],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [4, 3, 2, 5, 6, 2, 3, 4]
]

# Chamando a função para os exemplos
print("Exemplo 1:")
contabilizar_pecas(tabuleiro1)

print("\nExemplo 2:")
contabilizar_pecas(tabuleiro2)
