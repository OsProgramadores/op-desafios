# Desafio 03 — Números Palíndromos

Este projeto contém um programa em Python que identifica e exibe todos os números palíndromos dentro de um intervalo informado pelo usuário.  
O código está de acordo com o padrão de estilo PEP 8.

## O que é um número palíndromo?

Um número palíndromo é aquele que permanece o mesmo quando seus dígitos são invertidos.  
Exemplo: 121, 1331, 44.

## Como executar

1. Certifique-se de ter o Python 3 instalado.
2. **(Recomendado)** Crie e ative um ambiente virtual para isolar as dependências do projeto:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    **Uma vez que tenha efetuado todos os testes, para sair do ambiente virtual, digite:**

    ```bash
    deactivate
    ```

3. No terminal, navegue até esta pasta.
4. Execute o programa:

    ```bash
    python numeros_palindromicos.py
    ```

5. Informe o número mínimo e o número máximo quando solicitado.

## Exemplo de uso

```python
Digite o número mínimo: 10
Digite o número máximo: 150
11
22
33
44
55
66
77
88
99
101
111
121
131
141
```

## Estrutura do código

- `is_palindromo(num)`: Verifica se um número é palíndromo.
- `palindromos_entre(inicio, fim)`: Retorna uma lista de palíndromos no intervalo.
- O programa solicita ao usuário o intervalo e imprime cada palíndromo encontrado.

## Teste automatizado

Este projeto inclui testes automatizados utilizando o framework `pytest`.

### Como rodar os testes

1. Instale o pytest (caso ainda não tenha):

    ```bash
    pip install pytest
    ```

2. Execute os testes na pasta do projeto:

    ```bash
    pytest teste_palindromicos.py
    ```

Os testes verificam o funcionamento das funções principais do programa.
