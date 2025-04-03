# Gerador de Anagramas

## Apresentação

Olá! Meu nome é Fernando Jefferson e sou estudante de Ciência da Computação na Universidade Federal Fluminense - UFF. Neste projeto, desenvolvi um código em Python que gera todos os anagramas válidos de uma palavra ou frase, utilizando um dicionário de palavras pré-definido.

## O Desafio

Um anagrama é uma palavra ou frase formada pelo rearranjo de todas as letras de uma outra palavra ou frase, sem sobra ou falta. Por exemplo:

- **"barco"** é um anagrama de **"cobra"**.
- **"amor"** é um anagrama de **"roma"**.

O desafio consiste em criar um programa que:

1. **Recebe uma palavra ou frase** e considera apenas as letras (ignorando espaços e convertendo para maiúsculas).
2. **Lê uma lista de palavras válidas** a partir do arquivo `words.txt`.
3. **Gera todas as combinações possíveis de anagramas** que contenham apenas palavras válidas.
4. **Imprime as combinações encontradas** em ordem alfabética.

## Lógica do Código

A solução implementada segue os seguintes passos:

1. **Carregamento do Dicionário:**
   - O programa lê o arquivo `words.txt` e armazena as palavras em um conjunto para busca eficiente.

2. **Tratamento da Entrada:**
   - A entrada do usuário é convertida para maiúsculas e todos os caracteres não alfabéticos são removidos.

3. **Geração de Anagramas:**
   - O código utiliza a biblioteca `itertools` para gerar todas as permutações possíveis das letras da expressão de entrada.
   - Apenas palavras que estejam no dicionário são consideradas.

4. **Exibição dos Anagramas:**
   - As palavras encontradas são exibidas ordenadas alfabeticamente.

## Como Instalar o Python

Se você ainda não tem o Python instalado, siga estas instruções:

1. **Acesse o site oficial:** Vá para [python.org](https://www.python.org/downloads/).
2. **Baixe a versão mais recente:** Escolha a versão compatível com seu sistema operacional.
3. **Instale o Python:**
   - **Windows:** Execute o instalador e marque a opção "Add Python to PATH".
   - **macOS:** Baixe e instale o pacote correspondente.
   - **Linux:** Instale via terminal com:
     ```bash
     sudo apt install python3
     ```

## Como Executar o Programa

1. **Baixe o arquivo contendo o código (`main.py`).**
2. **Coloque o arquivo `words.txt` no mesmo diretório do script.**
3. **Abra um terminal e navegue até o diretório do arquivo.**
4. **Execute o seguinte comando:**

   ```bash
   python main.py "sua expressão"
   ```

## Contribuições

Sinta-se à vontade para sugerir melhorias ou reportar problemas abrindo uma issue no repositório. 🚀