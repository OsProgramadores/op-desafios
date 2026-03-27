def processar_fracao(linha):
    linha = linha.strip()
    if not linha:
        return ""
    
    if '/' in linha:
        partes = linha.split('/')
        num = int(partes[0])
        den = int(partes[1])
    else:
        num = int(linha)
        den = 1

    if den == 0:
        return "ERR"

    def calcular_mdc(a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    divisor = calcular_mdc(num, den)
    num //= divisor
    den //= divisor

    inteiro = num // den
    resto = num % den

    if resto == 0:
        return str(inteiro)
    elif inteiro > 0:
        return f"{inteiro} {resto}/{den}"
    else:
        return f"{resto}/{den}"

def ler_arquivo(frac):
    try:
        with open(frac, 'r') as arq:
            for linha in arq:
                resultado = processar_fracao(linha)
                if resultado:
                    print(resultado)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
if __name__ == "__main__":
    ler_arquivo('frac.txt')