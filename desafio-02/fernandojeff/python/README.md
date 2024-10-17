# Verificação de Números Primos

## Apresentação

Olá! Meu nome é Fernando Jefferson e sou estudante de Ciência da Computação na Universidade Federal Fluminense - UFF. Neste projeto, desenvolvi uma função em Python para verificar se um número é primo e gerar uma lista de números primos entre 1 e 10.000.

## Lógica do Código

A solução implementada utiliza um algoritmo que verifica se um número é primo. A lógica básica é:

1. **Verificação Inicial**: O número deve ser maior que 1 para ser considerado primo.
2. **Divisibilidade**: Para determinar se um número `n` é primo, ele é dividido por todos os números inteiros a partir de 2 até a raiz quadrada de `n`. Se `n` for divisível por qualquer um desses números, ele não é primo.
3. **Geração de Lista**: O programa itera através dos números de 1 a 10.000 e utiliza a função de verificação para compilar uma lista de todos os números primos nesse intervalo.

## Como Instalar o Python

Se você ainda não tem o Python instalado, siga estas instruções:

1. **Acesse o site oficial**: Vá para [python.org](https://www.python.org/downloads/).
2. **Baixe a versão mais recente**: Clique no botão de download que corresponde ao seu sistema operacional (Windows, macOS, Linux).
3. **Instale o Python**:
   - **Windows**: Execute o arquivo `.exe` baixado e marque a opção "Add Python to PATH" antes de clicar em "Install Now".
   - **macOS**: Abra o arquivo `.pkg` e siga as instruções do instalador.
   - **Linux**: A maioria das distribuições já vem com o Python instalado. Caso contrário, você pode instalá-lo através do terminal com o seguinte comando:
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
