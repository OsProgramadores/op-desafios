# Desafio 8 - Frações Simples
![Python](https://img.shields.io/badge/Python-512BD4?style=flat&logo=python&logoColor=yellow)
![VS Code](https://img.shields.io/badge/VScode-007ACC?style=flat&logo=visualstudiocode&logoColor=white)

## Descrição do Projeto:
Este código efetua a leitura de frações simples contidas em um arquivo e retorna a fração
simplificada correspondente para cada fração lida. Para calcular as simplificações, o
programa utiliza o (algorítmo de euclídes)[https://pt.wikipedia.org/wiki/Algoritmo_de_Euclides], visando obter eficientemente o(MDC)[https://pt.wikipedia.org/wiki/M%C3%A1ximo_divisor_comum]
entre o numerador e denomidador de cada fração.
Segue abaixo um exemplo de arquivo utilizado para testar o programa contendo frações válidas e, em sequência, suas respectivas saídas:

**Conteúdo do Arquivo:**
```bash
14/3
1/2
3/8
237/122
10492/6637
5/25
152/776
917/1008
2/1
120
942/227
197/199
283791739/113312387
13/13
15/0
```

**Saídas Esperadas:**
```bash
4 2/3
1/2
3/8
1 115/122
1 3855/6637
1/5
19/97
131/144
2
120
4 34/227
197/199
2 57166965/113312387
1
ERR
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
máquina, abra o terminal de comando e navegue até o diretório contendo o arquivo
`"solution.py"`. Em seguida, digite `python solution.py`
e os resultados deverão ser impressos de maneira formatada na CLI.
