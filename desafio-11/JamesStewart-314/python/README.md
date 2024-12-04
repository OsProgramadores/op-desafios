# Desafio 11 - Primos em Pi
![Python](https://img.shields.io/badge/Python-512BD4?style=flat&logo=python&logoColor=yellow)
![VS Code](https://img.shields.io/badge/VScode-007ACC?style=flat&logo=visualstudiocode&logoColor=white)

## Descrição do Projeto:
Intenta-se com este projeto identificar a maior sequência de números primos consecutivos
compostos por até quatro dígitos no primeiro 1 milhão de casas decimais de pi. Os dígitos serão extraídos do arquivo `pi-1M.txt` disponível no site [OsProgramadores](https://osprogramadores.com/).

A estratégia utilizada consiste em empregar uma variante do
[Algorítmo de Kadane](https://pt.wikipedia.org/wiki/Sublista_cont%C3%ADgua_de_soma_m%C3%A1xima) para localizar, em complexidade
temporal linear, a maior subsequência possível de números primos.

Para a verificação de primalidade, utiliza-se o [Crivo de Eratóstenes](https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes#:~:text=O%20Crivo%20de%20Erat%C3%B3stenes%20%C3%A9,Biblioteca%20de%20Alexandria%20desde%20247)
para gerar todos os primos de até quatro dígitos e armazená-los em um conjunto, no qual
esta ação permite performar o teste de primalidade de cada número em tempo constante
$O(1)$ com uma simples operação de pertencimento ao conjunto produzido.

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
necessário, utilize o comando `cd ".\op-desafios\desafio-11\JamesStewart-314"`
4. Execute o script `"solution.py"` com o comando `python solution.py`
e os resultados deverão ser impressos de maneira formatada na CLI.
