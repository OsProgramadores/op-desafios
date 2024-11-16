# Contabilizar Peças de Xadrez

## Apresentação

Olá! Meu nome é Fernando Jefferson e sou estudante de Ciência da Computação na Universidade Federal Fluminense - UFF. Neste projeto, desenvolvi um código em Python que conta o número de peças de cada tipo em um tabuleiro de xadrez representado como uma matriz 8x8.

## O Desafio

O xadrez é um jogo de tabuleiro estratégico, disputado por dois jogadores e que consiste em um tabuleiro com um arranjo de 8 linhas e colunas formando 64 posições diferentes como uma matriz [8 x 8]. Existem 6 diferentes tipos de peças no xadrez, e cada tipo possui uma quantidade para cada um dos jogadores (destacada por parênteses):

- **Peão (8)**
- **Bispo (2)**
- **Cavalo (2)**
- **Torre (2)**
- **Rainha (1)**
- **Rei (1)**

Um tabuleiro completo possui trinta e duas peças. Cada tipo de peça, segundo a ordem em que aparecem, recebe um código:
- `1`: Peão
- `2`: Bispo
- `3`: Cavalo
- `4`: Torre
- `5`: Rainha
- `6`: Rei
- `0`: Posição vazia

Neste desafio, você deverá contabilizar e exibir a quantidade de cada peça em um tabuleiro de xadrez **sem usar estruturas condicionais ou de múltipla escolha** (sem `if`, `else`, `switch case` ou operadores ternários).

## Lógica do Código

A solução implementada utiliza as seguintes ideias principais:

1. **Tabuleiro Representado por Números:**
   Cada posição do tabuleiro é representada por um número de 0 a 6, conforme os códigos das peças definidos no desafio.

2. **Dicionário para Contagem:**
   Um dicionário é inicializado para armazenar a contagem de cada tipo de peça.

3. **Iteração sobre o Tabuleiro:**
   O programa percorre toda a matriz 8x8, incrementando o contador correspondente para cada peça encontrada.

4. **Exibição do Resultado:**
   Após percorrer o tabuleiro, o programa exibe a quantidade de peças de cada tipo.

## Como Instalar o Python

Se você ainda não tem o Python instalado, siga estas instruções:

1. **Acesse o site oficial:** Vá para [python.org](https://www.python.org/downloads/).
2. **Baixe a versão mais recente:** Clique no botão de download que corresponde ao seu sistema operacional (Windows, macOS, Linux).
3. **Instale o Python:**
   - **Windows:** Execute o arquivo `.exe` baixado e marque a opção "Add Python to PATH" antes de clicar em "Install Now".
   - **macOS:** Abra o arquivo `.pkg` e siga as instruções do instalador.
   - **Linux:** A maioria das distribuições já vem com o Python instalado. Caso contrário, você pode instalá-lo através do terminal com o seguinte comando:
     ```bash
     sudo apt install python3
     ```

## Como Executar o Programa

1. **Baixe o arquivo contendo o código**.

2. **Navegue até o diretório onde o arquivo foi salvo**.

3. **Abra um terminal ou prompt de comando**.

4. **Execute o seguinte comando**:

   ```bash
   python seu_arquivo.py
   ```
