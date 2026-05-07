import sys


class ErroSintaxe(Exception):
    pass


class ErroDivisaoPorZero(Exception):
    pass


def mdc(a, b):
    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a


class Numero:
    def __init__(self, numerador, denominador=1):
        if denominador == 0:
            raise ErroDivisaoPorZero()

        if denominador < 0:
            numerador = -numerador
            denominador = -denominador

        divisor = mdc(numerador, denominador)

        self.numerador = numerador // divisor
        self.denominador = denominador // divisor

    def somar(self, outro):
        return Numero(
            self.numerador * outro.denominador + outro.numerador * self.denominador,
            self.denominador * outro.denominador
        )

    def subtrair(self, outro):
        return Numero(
            self.numerador * outro.denominador - outro.numerador * self.denominador,
            self.denominador * outro.denominador
        )

    def multiplicar(self, outro):
        return Numero(
            self.numerador * outro.numerador,
            self.denominador * outro.denominador
        )

    def dividir(self, outro):
        if outro.numerador == 0:
            raise ErroDivisaoPorZero()

        return Numero(
            self.numerador * outro.denominador,
            self.denominador * outro.numerador
        )

    def potenciar(self, outro):
        if outro.denominador != 1:
            raise ErroSintaxe()

        expoente = outro.numerador

        if expoente >= 0:
            return Numero(
                self.numerador ** expoente,
                self.denominador ** expoente
            )

        if self.numerador == 0:
            raise ErroDivisaoPorZero()

        expoente = -expoente

        return Numero(
            self.denominador ** expoente,
            self.numerador ** expoente
        )

    def texto(self):
        if self.denominador == 1:
            return str(self.numerador)

        sinal = ""
        numerador = self.numerador
        denominador = self.denominador

        if numerador < 0:
            sinal = "-"
            numerador = -numerador

        temp = denominador
        casas_2 = 0
        casas_5 = 0

        while temp % 2 == 0:
            casas_2 += 1
            temp //= 2

        while temp % 5 == 0:
            casas_5 += 1
            temp //= 5

        if temp == 1:
            casas = max(casas_2, casas_5)
            valor = numerador * (10 ** casas) // denominador
            inteiro = valor // (10 ** casas)
            decimal = str(valor % (10 ** casas)).zfill(casas).rstrip("0")

            if decimal == "":
                return sinal + str(inteiro)

            return sinal + str(inteiro) + "." + decimal

        return sinal + str(numerador) + "/" + str(denominador)


def tokenizar(linha):
    tokens = []
    i = 0

    while i < len(linha):
        caractere = linha[i]

        if caractere in " \t\r\n":
            i += 1

        elif caractere >= "0" and caractere <= "9":
            j = i

            while j < len(linha) and linha[j] >= "0" and linha[j] <= "9":
                j += 1

            tokens.append(("numero", int(linha[i:j])))
            i = j

        elif caractere in "+-*/^()":
            tokens.append((caractere, caractere))
            i += 1

        else:
            raise ErroSintaxe()

    return tokens


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicao = 0

    def atual(self):
        if self.posicao >= len(self.tokens):
            return None

        return self.tokens[self.posicao][0]

    def consumir(self, esperado=None):
        if self.posicao >= len(self.tokens):
            raise ErroSintaxe()

        token = self.tokens[self.posicao]

        if esperado is not None and token[0] != esperado:
            raise ErroSintaxe()

        self.posicao += 1

        return token

    def analisar(self):
        resultado = self.expressao()

        if self.atual() is not None:
            raise ErroSintaxe()

        return resultado

    def expressao(self):
        esquerda = self.termo()

        while self.atual() in ("+", "-"):
            operador = self.consumir()[0]
            direita = self.termo()
            esquerda = (operador, esquerda, direita)

        return esquerda

    def termo(self):
        esquerda = self.potencia()

        while self.atual() in ("*", "/"):
            operador = self.consumir()[0]
            direita = self.potencia()
            esquerda = (operador, esquerda, direita)

        return esquerda

    def potencia(self):
        esquerda = self.fator()

        if self.atual() == "^":
            operador = self.consumir()[0]
            direita = self.potencia()
            esquerda = (operador, esquerda, direita)

        return esquerda

    def fator(self):
        token = self.atual()

        if token == "numero":
            valor = self.consumir("numero")[1]
            return ("numero", valor)

        if token == "(":
            self.consumir("(")
            resultado = self.expressao()
            self.consumir(")")
            return resultado

        raise ErroSintaxe()


def calcular(no):
    if no[0] == "numero":
        return Numero(no[1])

    operador = no[0]
    esquerda = calcular(no[1])
    direita = calcular(no[2])

    if operador == "+":
        return esquerda.somar(direita)

    if operador == "-":
        return esquerda.subtrair(direita)

    if operador == "*":
        return esquerda.multiplicar(direita)

    if operador == "/":
        return esquerda.dividir(direita)

    if operador == "^":
        return esquerda.potenciar(direita)

    raise ErroSintaxe()


def resolver(linha):
    try:
        tokens = tokenizar(linha)
        arvore = Parser(tokens).analisar()
        resultado = calcular(arvore)
        return resultado.texto()
    except ErroDivisaoPorZero:
        return "ERR DIVBYZERO"
    except ErroSintaxe:
        return "ERR SYNTAX"


def main():
    if len(sys.argv) > 1:
        arquivo = open(sys.argv[1], "r")
    else:
        arquivo = sys.stdin

    for linha in arquivo:
        print(resolver(linha))

    if len(sys.argv) > 1:
        arquivo.close()


main()