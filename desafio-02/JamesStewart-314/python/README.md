# Solução Desafio 02 - Primos
![Python](https://img.shields.io/badge/Python-512BD4?style=flat&logo=python&logoColor=yellow)
![VS Code](https://img.shields.io/badge/VScode-007ACC?style=flat&logo=visualstudiocode&logoColor=white)

## Descrição do Projeto:
Este código tem como objetivo listar todos os números primos entre 0 e 10.000,
extremos inclusos. O algorítmo projetado para solucionar este problema foi
desenvolvido em linguagem Python com o uso de otimizações matemáticas visando
aprimorar a eficácia da verificação de primalidade.

## Algoritmo Implementado
A função `check_primality()`, definida por

```python
def  check_primality(number:  int,  /)  →  bool:
    assert  isinstance(number,  int),  "\'number\' must be of type \'int\'."

    if  number  <=  1:
        return  False
    if  number  ==  2:
        return  True
    if  number  %  2  ==  0:
        return  False

    for  i  in  range(3,  int(number  **  0.5)  +  1,  2):
        if  not  number  %  i:
            return  False

    return  True
```

é responsável por empregar a lógica de verificação de primalidade para
cada número inteiro fornecido como argumento principal. Sua rotina consiste
em testar a divisibilidade do número que desejamos constatar a primalidade -
digamos, o número $"n"$ - por todos os números
<u style="font-weight: 500">ímpares</u> no intervalo
$[\space 3, \sqrt{n} \space]$. Caso o resto da divisão de $n$ por
$x \in [\space 3, \sqrt{n} \space]$ resulte em zero, ou seja, dê uma
divisão inteira, isto significa que o valor analisado não corresponde a um
número _Primo_ e a função retornará `False`, indicando que trata-se de um
número composto. Caso contrário, se $n$ não for divisível por nenhum dos
inteiros positivos contidos no intervalo supracitado, então $n$ certamente
será um _Primo_ e a função retornará `True`.

## Requisitos para Execução
- Possuir um ambiente virtual Python instalado localmente em sua máquina com a
versão `3.8` ou superior.

    Para baixar esta e outras versões, visite o site 
    <a target="_blank" href="https://www.python.org/downloads/" style="color: lightgreen">Python.org</a> e siga os procedimentos de instalação para o
    seu sistema operacional.

## Instruções para Executar o Código
- Certificando-se de ter instalado corretamente o <code>Python</code> em sua
máquina, abra o terminal de comando e navegue até o diretório contendo o arquivo
<code>"desafio02.py"</code>. Em seguida, digite <code>python desafio02.py</code>
e os resultados deverão ser impressos de maneira formatada na CLI.

## Formatação da Saída
Os números primos são exibidos no terminal utilizando _Códigos ANSI_ e _Sequências de Escape_ para aplicar cores e formatação.
