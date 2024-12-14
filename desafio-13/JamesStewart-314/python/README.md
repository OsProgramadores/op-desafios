# Desafio 13 - Passeio do Cavalo
![Python](https://img.shields.io/badge/Python-512BD4?style=flat&logo=python&logoColor=yellow)
![VS Code](https://img.shields.io/badge/VScode-007ACC?style=flat&logo=visualstudiocode&logoColor=white)
## Descrição do Projeto:
No famigerado jogo de [Xadrez](https://pt.wikipedia.org/wiki/Xadrez), existe uma peça
chamada Cavalo que realiza movimentos em formato de "L" em todas as direções cardinais
numa malha quadriculada 8x8 que compõe o tabuleiro do jogo. O objetivo deste projeto
consiste em exibir a sequência de movimentos do cavalo, partindo de uma casa arbitrária
qualquer do tabuleiro, que passe uma única vez por todas as 64 casas.

Para alcançar este objetivo, este programa utiliza a
[Heurística de Warnsdorff](https://en.wikipedia.org/wiki/Knight%27s_tour#:~:text=Warnsdorf's%20rule%20is%20a%20heuristic,revisit%20any%20square%20already%20visited.)
para otimizar as buscas recursivas pelo primeiro caminho válido que soluciona o problema.

## Exemplo de Uso:
```bash
python ./solution.py a1
```

## Saída Esperada:
```bash
a1
c2
e1
g2
.
.
.
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
necessário, utilize o comando `cd ".\op-desafios\desafio-13\JamesStewart-314"`
4. Execute o script `"solution.py"` com o comando `python solution.py`
e os resultados deverão ser impressos de maneira formatada na CLI.
