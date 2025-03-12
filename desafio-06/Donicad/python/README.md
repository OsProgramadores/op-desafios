# Script para exibir Anagramas.

## Requisitos

- Ter Python instalado em seu computador

    Faça o download da versão mais atual do Python para seu sistema operacional no site oficial da linguagem [python.org](https://www.python.org/downloads/).

## Funcionamento

Ao executar o arquivo anagramas.py no terminal usando linha de comando uma frase ou palavra será requisitado no terminal.
Após preencher uma lista com as possíveis combinações validas da palavra ou frase será impressa no terminal.

## Explicação do Código

```python
    from collections import Counter
    import re

    def validar_entrada(expressao):
        expressao = expressao.upper().replace(" ", "")
        if not re.match("^[A-Z]+$", expressao):
            raise ValueError("Use apenas letras de A-Z.")
        return expressao
```

- Primeiramente eu faço o importe da lib "re", responsável por percorrer pela expressão colocada no input e verificar se é uma string. Caso não for um erro será exibido no terminal.

- O importe "Counter" é responsável por contar as letras, essa lib será usada mais à frente.

---

```python
    def ler_palavras_validas(caminho_arquivo):
        with open(caminho_arquivo, 'r') as file:
            palavras = [linha.strip().upper() for linha in file if linha.strip().isalpha()]
        return palavras
```

- Nessa função estou apenas lendo todas as palavras que estão no words.txt, retirando os espaços, deixando em maiúsculas e adicionando elas em uma outra lista que usarei para gerar os anagramas.

---

```python
    def filtrar_palavras(palavras, expressao):
        letras_expressao = Counter(expressao)
        palavras_filtradas = []
        for palavra in palavras:
            letras_palavra = Counter(palavra)
            if all(letras_palavra[letra] <= letras_expressao.get(letra, 0)
                for letra in letras_palavra):
                palavras_filtradas.append(palavra)
        return palavras_filtradas
```

- Essa função começa contando quantas vezes cada palavra aparece na expressão usando o "Counter", armazenando os dados em letras_expressao.
- Em seguida, percorre cada palavra na lista de palavras, e para cada palavra é contado a ocorrência de suas letras.
- Utiliza a função all() para verificar se todas as letras da palavra podem ser formadas a partir das letras disponíveis na expressão. Isso significa que a palavra não pode ter mais ocorrências de uma letra do que aquelas disponíveis na expressão.
- Se a palavra atender aos critérios, ela é adicionada na lista "palavras_filtradas", e pôr fim a função retorna a lista com as palavras que passaram na verificação.

---

```python
    def gerar_anagramas(expressao, palavras, anagrama_atual=None, resultados=None):
        if anagrama_atual is None:
            anagrama_atual = []
        if resultados is None:
            resultados = set()
        if not expressao:
            resultados.add(" ".join(sorted(anagrama_atual)))
            return
        for palavra in palavras:
            letras_palavra = Counter(palavra)
            if all(letras_palavra[letra] <= Counter(expressao).get(letra, 0)
                for letra in letras_palavra):
                nova_expressao = subtrair_letras(expressao, palavra)
                gerar_anagramas(nova_expressao, palavras, anagrama_atual + [palavra], resultados)

    def subtrair_letras(expressao, palavra):
        expressao_contador = Counter(expressao) - Counter(palavra)
        return ''.join([letra * expressao_contador[letra] for letra in expressao_contador])
```

- Aqui temos duas funções que trabalham juntas para encontrar e armazenar todos os anagramas possíveis a partir da lista de palavras, utilizando uma abordagem recursiva para explorar combinações de letras.

- gerar_anagramas: Gera anagramas combinando palavras válidas a partir de uma expressão.

- subtrair_letras: Remove letras de uma palavra da expressão original, retornando as letras restantes para a próxima iteração da busca de anagramas.

---

```python
    def exibir_resultados(resultados):
        for anagrama in sorted(resultados):
            print(anagrama)
```

- Por fim temos um for para exibir todos os resultados de anagramas da expressão colocada no input, ordenando o resultado em ordem alfabética.
