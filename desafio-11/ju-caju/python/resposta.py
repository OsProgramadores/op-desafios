import sys

def gerar_primos():
    limite = 9973
    eh_primo = [True] * (limite + 1)

    eh_primo[0] = False
    eh_primo[1] = False

    for x in range(2, int(limite ** 0.5) + 1):
        if eh_primo[x]:
            for multiplo in range(x * x, limite + 1, x):
                eh_primo[multiplo] = False

    primos = set()

    for x in range(2, limite + 1):
        if eh_primo[x]:
            primos.add(str(x))

    return primos


def ler_pi():
    if len(sys.argv) > 1:
        arquivo = open(sys.argv[1], "r")
        texto = arquivo.read()
        arquivo.close()
    else:
        texto = sys.stdin.read()

    texto = texto.strip()
    texto = texto.replace("\n", "")
    texto = texto.replace("\r", "")
    texto = texto.replace(" ", "")
    texto = texto.replace("\t", "")

    if "." in texto:
        texto = texto.split(".", 1)[1]

    elif len(texto) > 1 and texto[0] == "3" and texto[1] == "1":
        texto = texto[1:]

    return texto


def encontrar_maior_sequencia(digitos, primos):
    tamanho = len(digitos)

    dp = [0] * (tamanho + 5)

    melhor_inicio = 0
    melhor_tamanho = 0

    for i in range(tamanho - 1, -1, -1):
        melhor_aqui = 0

        for qtd in range(1, 5):
            fim = i + qtd

            if fim <= tamanho:
                pedaco = digitos[i:fim]

                if pedaco in primos:
                    total = qtd + dp[fim]

                    if total > melhor_aqui:
                        melhor_aqui = total

        dp[i] = melhor_aqui

        if melhor_aqui >= melhor_tamanho:
            melhor_tamanho = melhor_aqui
            melhor_inicio = i

    return digitos[melhor_inicio:melhor_inicio + melhor_tamanho]


primos = gerar_primos()
digitos_pi = ler_pi()

resposta = encontrar_maior_sequencia(digitos_pi, primos)

print(resposta)