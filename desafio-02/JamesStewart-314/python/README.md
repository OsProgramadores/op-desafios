# Solução Desafio 02 - Primos
![Python](https://img.shields.io/badge/Python-512BD4?style=flat&logo=python&logoColor=yellow)
![VS Code](https://img.shields.io/badge/VScode-007ACC?style=flat&logo=visualstudiocode&logoColor=white)

## Descrição do Projeto:
Este código tem como objetivo listar todos os números primos entre 0 e 10.000,
extremos inclusos. O algorítmo projetado para solucionar este problema foi
desenvolvido em linguagem Python com o uso de otimizações matemáticas visando
aprimorar a eficácia da verificação de primalidade.

## Algoritmo Implementado
O gerador `sieveofEratosthenesPrimeGenerator()`, definido por

```python
def sieveofEratosthenesPrimeGenerator() -> Generator[int, None, None]:

    yield 2

    sieveofEratosthenesDict: dict[int, int] = {}
    currentNumber: int = 3

    while True:
        if currentNumber not in sieveofEratosthenesDict:
            yield currentNumber
            sieveofEratosthenesDict[currentNumber * currentNumber] = currentNumber

        else:
            currentNumberKey: int = currentNumber + (sieveofEratosthenesDict[currentNumber] << 1)

            while sieveofEratosthenesDict.get(currentNumberKey):
                currentNumberKey += (sieveofEratosthenesDict[currentNumber] << 1)

            sieveofEratosthenesDict[currentNumberKey] = sieveofEratosthenesDict[currentNumber]
            del sieveofEratosthenesDict[currentNumber]

        currentNumber += 2
```

consiste em uma estrutura iterável responsável por empregar a lógica de geração dos
números primos. Inspirado pelo
<a href="https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes" target="_blank" style="font-style: italic; color: lightgreen">Crivo de Eratóstenes</a>,
esta função percorre todos os números $n \in \mathbb{N}$ e, caso $n \in \mathbb{P}$ -
ou seja, $n$ for primo - associa o valor de $n$ à $n^{2}$ e armazena esta informação no
dicionário `sieveofEratosthenesDict`. Em contrapartida, se $n \notin \mathbb{P}$, então
significa que há uma chave correspondente com o mesmo valor no dicionário `sieveofEratosthenesDict` que contém um primo $p'$ divisor de $n$. Dessa maneira,
substituímos portanto o valor de $n$ pelo próximo múltiplo de $p'$, digamos, $k$, tal que
$k > n$ e reiteramos sobre este procedimento indefinidamente. A condição de parada é
estabelecida com uma estrutura condional externa ao gerador, possibilitando uma
flexibilidade ao produzir uma quantidade arbitrária e virtualmente infinita de números
primos com altíssima eficiência.

## Requisitos para Execução
- Possuir um ambiente virtual Python instalado localmente em sua máquina com a
versão `3.8` ou superior.

    Para baixar esta e outras versões, visite o site
    <a target="_blank" href="https://www.python.org/downloads/" style="color: lightgreen">Python.org</a> e siga os procedimentos de instalação para o
    seu sistema operacional.

## Instruções para Executar o Código
- Certificando-se de ter instalado corretamente o `Python` em sua
máquina, abra o terminal de comando e navegue até o diretório contendo o arquivo
`"desafio02.py"`. Em seguida, digite `python desafio02.py`
e os resultados deverão ser impressos de maneira formatada na CLI.

## Formatação da Saída
Os números primos são exibidos no terminal utilizando _Códigos ANSI_ e _Sequências de Escape_ para aplicar cores e formatação.
