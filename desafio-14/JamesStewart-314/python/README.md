# Desafio 14 - Expressões Numéricas
![Python](https://img.shields.io/badge/Python-512BD4?style=flat&logo=python&logoColor=yellow)
![VS Code](https://img.shields.io/badge/VScode-007ACC?style=flat&logo=visualstudiocode&logoColor=white)

## Descrição do Projeto:
Expressões numéricas consistem numa sequências de operações aplicadas a um conjunto de
valores em ordem de precedência com base nas regras aritméticas preestabelecidas.
O objetivo deste projeto consiste em efetuar a leitura de um arquivo textual contendo uma
expresão numérica por linha e exibir seu respectivo resultado final. Se o programa
encontrar um divisão por zero deverá imprimir ERR DIVBYZERO. 
Se o programa encontrar um erro de sintaxe na expressão deverá imprimir ERR SYNTAX.

## Exemplo do Conteúdo Lido do Arquivo:
```
1 + 3
2 - 3 * 2
2 ^ 3 / 4
0 * 5 * (4 + 1)
5 + 5 / 0
5 + + 1
5 + ( 465 + 1
```
## Saídas Esperadas:
```
4
-4
2
0
ERR DIVBYZERO
ERR SYNTAX
ERR SYNTAX
```
## Requisitos para Execução
- Possuir um ambiente virtual Python instalado localmente em sua máquina com a
versão `3.10` ou superior.
    Para baixar esta e outras versões, visite o site
    <a target="_blank" href="https://www.python.org/downloads/" style="color: lightgreen">Python.org</a>
    e siga os procedimentos de instalação para o
    seu sistema operacional.
    Após a instalação, abra o terminal de comando em sua máquina e digite o comando
    `python --version`. O comando deverá informar a versão atual do interpretador de
    Python caso o download tenha sido feito corretamente. Certifique-se de possuir uma
    versão igual ou superior à `3.10`, caso contrário, o código não funcionará.

## Instruções para Executar o Código
- Certificando-se de ter instalado corretamente o `Python` em sua
máquina, execute os seguintes comandos:
1. Abra o terminal e navegue até a pasta em que deseja copiar este repositório com o
comando `cd <caminho_absoluto_do_diretótio>`;
2. Em seguida, copie e cole o seguinte código:
`git clone https://github.com/OsProgramadores/op-desafios.git`;
3. Navegue até a pasta contendo o arquivo `solution.py` na árvore do repositório - se
necessário, utilize o comando `cd ".\op-desafios\desafio-14\JamesStewart-314"`
4. Execute o script `"solution.py"` com o comando `python solution.py`
e os resultados deverão ser impressos de maneira formatada na CLI.
