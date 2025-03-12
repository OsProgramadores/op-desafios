# Desafio 12 - Potências de 2
![Python](https://img.shields.io/badge/Python-512BD4?style=flat&logo=python&logoColor=yellow)
![VS Code](https://img.shields.io/badge/VScode-007ACC?style=flat&logo=visualstudiocode&logoColor=white)

## Descrição do Projeto:
O objetivo deste projeto consiste em ler números representados em base decimal presentes
no arquivo `d12.txt`, no qual está disponível para download no site [OsProgramadores](https://osprogramadores.com/), e exibir na saída, para cada número, o seu valor decimal,
`true` caso o número seja uma potência de $2$ ou `false` caso contrário e um terceiro valor que corresponde ao logarítmo na base $2$ do número avaliado se ele constituir uma potência de $2$.

## Exemplo do Conteúdo Lido do Arquivo:
```
1
140
128
137
65535
65536
17179869184
```

## Saídas Esperadas:
```
1 true 0
140 false
128 true 7
137 false
65535 false
65536 true 16
17179869184 true 34
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
necessário, utilize o comando `cd ".\op-desafios\desafio-12\JamesStewart-314"`
4. Execute o script `"solution.py"` com o comando `python solution.py`
e os resultados deverão ser impressos de maneira formatada na CLI.
