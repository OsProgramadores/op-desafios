# Desafio 7 - UNIX TAC
![Python](https://img.shields.io/badge/Python-512BD4?style=flat&logo=python&logoColor=yellow)
![VS Code](https://img.shields.io/badge/VScode-007ACC?style=flat&logo=visualstudiocode&logoColor=white)

## Descrição do Projeto:
Existem diversos comandos presentes em sistemas Unix-Like para realizar diversos
procedimentos no computador, seja para consultar informações ou manusear arquivos. Dentre
eles, temos o comando TAC, cuja finalidade consiste em exibir o conteúdo de um arquivo com
a ordem decrescente das linhas - ou seja, a leitura ocorrerá desde a última linha até a
primeira.

Para fins de exemplificação, considere o arquivo `meuarquivo.txt` contendo as seguintes
linhas de texto, respectivamente:

```bash
Essa é a primeira linha
Essa é a segunda linha
Essa é a terceira linha
Essa é a última linha
```

Portanto, o comando `tac meuarquivo.txt` deverá exibir a saída:

```bash
$ tac arquivo
Essa é a última linha
Essa é a terceira linha
Essa é a segunda linha
Essa é a primeira linha
```

O objetivo deste programa consiste em reproduzir o comando TAC na linguagem de programação `Python`, conforme veremos a seguir.

Primeiro, especificamos três constantes que representam a quantidades de _bytes_ existente
em um _megabyte_, a quantidade de _megabytes_ a ser lida a cada iteração de leitura e a
quantidade total de _bytes_ a ser lida do arquivo em cada loop, respectivamente:

```python
MEGABYTE_IN_BYTES: Final[int] = 1_048_576
CHUNK_SIZE: int = 100
CHUNK_SIZE_IN_BYTES: int = CHUNK_SIZE * MEGABYTE_IN_BYTES
```

Em seguida, definimos a função responsável por percorrer o arquivo e exibir suas linhas na
ordem invertida:

```python
def tac_python(file_path: str) -> None:
    try:
        with open(file_path, "rb") as bin_file:
            bin_file.seek(0, 2)
            bin_file.seek(bin_file.tell() - 1)
            file_cursor_position: int = bin_file.tell()
            string_buffer: str = b""

            while file_cursor_position != 0:
                old_file_cursor_position: int = bin_file.tell()
                file_cursor_position = max(0, file_cursor_position - CHUNK_SIZE)

                bin_file.seek(file_cursor_position)
                string_buffer = bin_file.read(old_file_cursor_position - file_cursor_position)\
                      + string_buffer
                bin_file.seek(file_cursor_position)

                str_gen: Generator[str | bool, None, str] = process_buffer(string_buffer)

                try:
                    while True:
                        print(next(str_gen).decode("utf-8"))
                except StopIteration as return_value:
                    string_buffer = return_value.value

            print(string_buffer.decode("utf-8"))

    except FileNotFoundError:
        print("Error: File path is invalid or doesn\'t exist.")
```

No qual suas operações consistem basicamente em avançar até o final do arquivo com o
comando `bin_file.seek(0, io.SEEK_END)` e efetuar concomitantemente uma leitura
retrógrada, onde o resultado da leitura é armazenado no buffer `string_buffer` e
processado pela função `process_buffer` a cada iteração. A definição desta função
encontra-se explicitada logo abaixo:

```python
def process_buffer(bin_string_buffer: str) -> Generator[str | bool, None, str]:
    bin_string_buffer_list: list[str] = bin_string_buffer.split(b"\n")
    for idx in range(len(bin_string_buffer_list) - 1, 0, -1):
        yield bin_string_buffer_list[idx]

    return bin_string_buffer_list[0]
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
`"desafio07.py"`. Em seguida, digite `python desafio07.py`
e os resultados deverão ser impressos de maneira formatada na CLI.
