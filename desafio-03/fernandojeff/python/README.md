# Verificação de Números Palíndromos

## Apresentação

Olá! Meu nome é Fernando Jefferson e sou estudante de Ciência da Computação na Universidade Federal Fluminense - UFF. Neste projeto, desenvolvi uma função em Python para verificar se um número é palíndromo e, em seguida, gerar uma lista de números palíndromos dentro de um intervalo definido pelo usuário.

## Lógica do Código

A solução implementada utiliza um algoritmo que verifica se um número é palíndromo e exibe os palíndromos dentro de um intervalo específico. A lógica básica é:

1. **Verificação de Palíndromo**: Um número é considerado palíndromo se ele é igual a sua reversão. Para verificar isso, converti o número para uma string e comparei com seu reverso.
   
2. **Geração de Lista**: O programa solicita ao usuário um valor inicial e um valor final, então itera por todos os números dentro desse intervalo. Cada número é passado para a função de verificação, e, se for um palíndromo, ele é exibido na tela.

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
   ```

5. **Insira o intervalo**:
   - O programa pedirá um número inicial e um número final. Após fornecer esses valores, ele exibirá todos os números palíndromos encontrados no intervalo especificado.
