# Desafio-04 - Anagramas

## Descrição

Este algoritmo é capaz de encontrar anagramas de uma palavra a partir de uma lista de palavras armazenada no arquivo `words.txt`.

Um anagrama é uma palavra formada pela reorganização das letras de outra palavra, utilizando a mesma quantidade de ocorrências de cada letra.

Por exemplo, as palavras `AMOR` e `ROMA` são anagramas, pois possuem as mesmas letras, embora estejam organizadas de maneiras diferentes.

Neste programa, as palavras são comparadas sem diferenciar letras maiúsculas de minúsculas.

## Instruções

Para que este algoritmo execute adequadamente, é necessário seguir todas as instruções e os requisitos apresentados neste documento.

## Requisitos

- Sistema operacional compatível com o compilador GCC.
- Compilador GCC instalado e configurado corretamente.
- Arquivo `words.txt` contendo a lista de palavras que serão utilizadas na busca.
- Arquivos `desafio-06.c` e `words.txt` localizados no mesmo diretório durante a execução do programa.

## Requisitos Para Executar O Programa No Windows

1. Faça um **fork** deste repositório para obter uma cópia na sua conta do GitHub.

2. Execute o comando `git clone` para baixar o repositório do seu fork para sua máquina.

3. Instale o compilador [GCC](https://sourceforge.net/projects/mingw-w64/) em seu sistema operacional.

4. Verifique se o GCC foi instalado corretamente com o comando:

```bash
gcc --version
```

## Como Executar O Arquivo desafio-06.c

1. Compile o programa com o comando:

```bash
gcc desafio-06.c -o desafio6
```

2. Execute o programa passando uma palavra como argumento.

No Linux:

```bash
./desafio4 amor
```

No Windows:

```bash
desafio4.exe amor
```

O programa utilizará a palavra informada como entrada e exibirá as palavras encontradas no arquivo `words.txt` que sejam anagramas da palavra fornecida.

**Importante:** o arquivo `words.txt` deve estar no diretório de execução do programa.

## Lógica Do Algoritmo

- O programa recebe uma palavra por meio dos argumentos da linha de comando.
- A palavra recebida é convertida para letras maiúsculas, permitindo que a comparação desconsidere diferenças entre letras maiúsculas e minúsculas.
- A palavra de entrada é ordenada em ordem crescente dos caracteres. Dessa forma, palavras que possuem as mesmas letras terão a mesma sequência de caracteres após a ordenação.
- Antes de realizar a comparação, o programa verifica se a palavra lida possui o mesmo tamanho da palavra de entrada. Caso contrário, ela é ignorada.
- A palavra lida é copiada para o vetor `anagramaOrdenado`, preservando a palavra original no vetor `anagrama`.
- A função `comparar_string()` compara os caracteres das duas palavras ordenadas:
  - Se todos os caracteres forem iguais, a função retorna `0`, indicando que as palavras são anagramas.
  - Se algum caractere for diferente, a função retorna `1`, indicando que as palavras não são anagramas.

- Quando um anagrama é encontrado, a palavra original armazenada no vetor `anagrama` é exibida na saída.
