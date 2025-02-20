# Desafio 08 - Frações Simples

## Descrição do desafio
Escreva um programa que leia um arquivo texto contendo uma lista de frações em ASCII (uma por linha) e produza na saída a versão simplificada de cada fração. Números simples assumem denominador 1 (apenas imprima o número). Divisões inteiras como 81/9 devem imprimir o número inteiro 9. Em caso de erros na entrada (como divisão por zero), imprima “ERR” em maíusculas.

## Como rodar
Para rodar, use Python na versão 3.12 ou superior e utilize o comando:

`python desafio-08.py`

O programa irá buscar o arquivo `frac.txt` no mesmo diretório. Caso não encontre o arquivo, irá pedir ao usuário que indique o caminho.

## Algoritmo
### Classe `Fraction`
Uma classe que representa frações com numerador e denominador inteiros.

Esta classe fornece funcionalidades para criar, simplificar e exibir frações, incluindo o tratamento de partes inteiras e casos de denominador zero.

Quando uma nova instância é criada, ela é automaticamente simplificada.

Possui também um método de repesentação que imprimirá na tela a fração especialmente formatada, de acordo com seus valores.

### Função `MDC`
Calcula o **Maior Divisor Comum** entre dois números utilizando o [Algoritmo de Euclides](https://pt.wikipedia.org/wiki/Algoritmo_de_Euclides).
```
def MDC(x, y):
    if y == 0:
        return x

    return MDC(y, (x % y))
```

### Função `read_file_lines` e `read_file`
Trabalham em conjunto.

Tentam ler o arquivo padrão `frac.txt` no diretório atual e, caso não o encontre, pede ao usuário que entre o endereço válido do arquivo.
```
def read_file_lines(file_path: str) -> list[str]:
    if path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()

    print("Arquivo não encontrado.")
    return None


def read_file(file_path: str) -> list[str]:
    while True:
        file_lines = read_file_lines(file_path)
        if file_lines:
            return file_lines

        file_path = input("Por favor, digite o endereço de arquivo válido ou 'S' para sair.\n> ")
        if file_path.upper() == "S":
            exit()
```

### Função `convertToInteger`
Recebe um argumento do tipo *string* e tenta converte-lo para `int`.
```
def convertToInteger(string: str) -> int:
    try:
        number = int(string)
        return number
    except ValueError as e:
        print(f'Uma entrada inválida encontrada: {string}')

    return None
```

### Função `parseFraction`
Recebe uma linha do lida do arquivo de frações e a converte em um objeto da classe `Fraction`.

* Se a linha estiver vazia, ele a ignora
* Se a linha contiver elementos inválidos, ele a ignora
* Se a linha possuir mais de três fatores, ele ignora os demais
```
def parseFraction(fractionString: str) -> Fraction:
    parts = fractionString.split("/")
    numerator = 0
    denominator = 1

    length = len(parts)

    if length < 1:
        return None

    if length >= 1:
        numerator = convertToInteger(parts[0])
        if not numerator:
            return None

    if length >= 2:
        denominator = convertToInteger(parts[1])
        if denominator == None:
            return None

    return Fraction(numerator, denominator)
```

### Função `parseFractions`
Recebe todas as linhas do arquivo lido e retorna uma lista de frações válidas utilizando a função `parseFraction`.

Forma mais legível do antigo comando:

`list(filter(lambda x: x != None, map(lambda x: parseFraction(x), file_lines)))`
```
def parseFractions(fractionList: list[str]) -> list[Fraction]:
    fractions = []

    for fractionString in fractionList:
        fraction = parseFraction(fractionString.strip())
        if fraction:
            fractions.append(fraction)

    return fractions
```
