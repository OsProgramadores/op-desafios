# Desafio 6 - Anagramas
![Python](https://img.shields.io/badge/Python-512BD4?style=flat&logo=python&logoColor=yellow)
![VS Code](https://img.shields.io/badge/VScode-007ACC?style=flat&logo=visualstudiocode&logoColor=white)

## Descrição do Projeto:
Entende-se por anagrama uma reordenação de todos os caracteres contidos
em uma palavra ou frase, sem modificar a frequência de cada letra ou
acrescentar novas. Segue abaixo alguns exemplos de anagramas:

- A palavra _barco_ é um anagrama da palavra _cobra_ (todas as letras de “cobra” usadas em “barco”).
- A palavra _mar_ **não** é um anagrama da palavra _roma_ (a letra “o” em “roma” não foi usada).
- A palavra _sal_ **não** é um anagrama da palavra _mal_ (a letra “s” de “sal” não existe em “mal”).

Intenta-se, com este código, listar todas as combinações possíveis de palavras contidas no arquivo [`words.txt`](https://osprogramadores.com/desafios/d06/words.txt), disponível em [`OsProgramadores.com`](https://osprogramadores.com/), que juntas formem um anagrama da palavra originalmente forncida como argumento do programa.

## Algoritmo Implementado
Um _sub-anagrama_ de uma palavra $word_{1}$, denotado por $word_{2}$, é definido como um
anagrama que pode ser construído utilizando **no máximo** todas as letras que constituem a
palavra $word_{1}$, sem a necessidade de usar todas elas mandatoriamente.

O procedimento para varredura dos possíveis anagramas consiste primeiramente em definir um
procedimento, a princípio sem memoização, para verificar se uma string $word_{1}$ é
sub-anagrama de outra string $word_{2}$. Para isto, criamos a função `is_sub_anagram()`,
definida por:

```python
def is_sub_anagram(super_string: str, sub_string: str) → bool:
    if len(sub_string) > len(super_string):
        return False

    super_string_count = ctr(super_string)
    sub_string_count = ctr(sub_string)

    return all(super_string_count[key] ≥ value for key, value in sub_string_count.items())
```

Sua rotina resume-se em verificar se o tamanho do sub-anagrama é maior que o tamanho da
palavra original, retornando `False` em caso afirmativo. Se o teste anterior falhar, então
contamos todas as letras contidas em ambas as palavras e verificamos se, para ocorrência
dos caracteres contido na segunda palavra, se há pelo menos uma quantidade igual ou
superior de ocorrências dos mesmos caracteres na primeira paravra, retornando `True` em
caso afirmativo e `False` caso contrário.

Adiante, vamos percorrer o arquivo `words.txt` em busca de palavras que correspondam a
sub-anagramas do argumento fornecido pelo usuário através da linha de comando e armazenar
todos os sub-anagramas válidos na lista de strings `all_valid_words`.

Antes de iniciar a busca pelos anagramas da palavra fornecida como argumento, percorremos
a lista recém criado de todos os sub-anagramas da palavra argumento obtidos no arquivo
e relacionamos cada elemento com os outros elementos da mesma lista que são
sub-anagramas do elemento corrente analisado. Esta informação será utilizada para gerar um
dicionário de memoização na função alternativa `is_sub_anagram_memo()`.

Ademais, criamos o gerador auxiliar `check_word()` para iterar sobre a lista
`all_valid_words` e retornar todos os sub-anagramas identificados durante a iteração
atual, no qual sua assinatura é:

```python
def check_word(string_pattern: str) → Generator[tuple[str, str], None, None]:
    for current_word in all_valid_words:
        if len(current_word) > len(string_pattern):
            break
        if is_sub_anagram_memo(string_pattern, current_word):
            yield (remove_characters(string_pattern, current_word), current_word)
```

No qual esta realiza chamadas da função `remove_characters()`, responsável apenas por
eliminar todos os caracteres do parâmetro `string_pattern` que forem encontrados em um
sub-anagrama, definida por:

```python
def remove_characters(original_string: str, char_to_remove: str) -> str:
    return ''.join(sorted((ctr(original_string) - ctr(char_to_remove)).elements()))
```

E finalmente, executamos a função de busca dos palíndromos propriamente dita, no qual a
mesma busca recursivamente todos os palíndromos possíveis e adiciona cada anagrama obtido
no conjunto de strings `all_anagrams`.  Segue abaixo a assinatura da função supracitada:

```python
def search_palindromes(string_pattern: str,
                       palindrome_list: list[str]) -> None:
    if not string_pattern:
        all_anagrams.add(tuple(sorted(palindrome_list)))
        return

    if string_pattern in search_palindromes_memoization:
        all_check_words = search_palindromes_memoization[string_pattern]

        for word in all_check_words:
            search_palindromes(word[0], palindrome_list + [word[1]])

    else:
        if not palindrome_list:
            for current_word in all_valid_words[::]:
                if is_sub_anagram_memo(string_pattern, current_word):
                    search_palindromes(remove_characters(string_pattern, current_word),
                                       palindrome_list + [current_word])
                    all_valid_words.pop(0)
            return

        search_palindromes_memoization[string_pattern] = []

        for word in check_word(string_pattern):
            search_palindromes_memoization[string_pattern].append(word)
            search_palindromes(word[0], palindrome_list + [word[1]])
```

Por fim, populamos o conjunto de strings `all_anagrams` com todos os anagramas encontrados
durante a execução da função anterior e exibimos os resultados através do laço

```python
for anagramTuple in iter(all_anagrams):
    print(*anagramTuple)
```

## Requisitos para Execução
- Possuir um ambiente virtual Python instalado localmente em sua máquina com a
versão `3.10` ou superior.

    Para baixar esta e outras versões, visite o site
    <a target="_blank" href="https://www.python.org/downloads/" style="color: lightgreen">Python.org</a> e siga os procedimentos de instalação para o
    seu sistema operacional.

    Após a instalação, abra o terminal de comando em sua máquina e digite o comando
    `python --version`. O comando deverá informar a versão atual do interpretador de
    Python caso o download tenha sido feito corretamente. Certifique-se de possuir uma
    versão igual ou superior à `3.10`, caso contrário, o código não funcionará.

## Instruções para Executar o Código
- Certificando-se de ter instalado corretamente o `Python` em sua
máquina, abra o terminal de comando e navegue até o diretório contendo o arquivo
`"desafio06.py"`. Em seguida, digite `python desafio06.py`
e os resultados deverão ser impressos de maneira formatada na CLI.
