# Solução Desafio 03 - Palíndromos

![Python](https://img.shields.io/badge/Python-512BD4?style=flat&logo=python&logoColor=yellow)
![VS Code](https://img.shields.io/badge/VScode-007ACC?style=flat&logo=visualstudiocode&logoColor=white)

## Descrição do Projeto:
Este código tem como objetivo listar todos os números inteiros palindrômicos $x
\in [\space a, b \space]$, onde $"a"$ e $"b"$ são dois números inteiros positivos definidos em
tempo de execução, com $b \geq a$.

## Algoritmo Implementado
A função responsável por verificar se um determinado número inteiro é palindrômico, cujo nome é `number_is_palindromic()`, definida por:

```python
def number_is_palindromic(number: int):
    return (strNumber := str(number)) == strNumber[::-1]
```

converte o parâmetro de entrada, neste caso, um inteiro, para uma string e efetua a
comparação com sua respectiva versão invertida. Em caso de igualdade, a função retorna um
valor booleano `True` a fim de sinalizar a igualdade, e retorna `False` caso contrário.

O código também dispõe de funções auxiliares para isolar a obtenção e validação das
entradas, realizar a limpeza do terminal e afins.

## Requisitos para Execução
- Possuir um ambiente virtual Python instalado localmente em sua máquina com a
versão `3.10` ou superior.

    Para baixar esta e outras versões, visite o site
    <a target="_blank" href="https://www.python.org/downloads/" style="color: lightgreen">Python.org</a> e siga os procedimentos de instalação para o
    seu sistema operacional.

    Após a instalação, abra o terminal de comando em sua máquina e digite o comando
    `python --version`. O comando deverá informar a versão atual do interpretador de
    Python caso o download tenha sido feito corretamente. Certifique-se de possuir uma
    versão igual ou superior à `3.10`, caso contrário, o código não funcionará.

## Instruções para Executar o Código
- Certificando-se de ter instalado corretamente o `Python` em sua
máquina, abra o terminal de comando e navegue até o diretório contendo o arquivo
`"desafio02.py"`. Em seguida, digite `python desafio02.py`
e os resultados deverão ser impressos de maneira formatada na CLI.
