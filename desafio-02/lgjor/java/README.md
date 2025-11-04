# 2 - Primos

## Desafio

Listar todos os números primos entre 1 e 10000, na linguagem de sua preferência.

## Tecnologias utilizadas

- Linguagem: Java
- Versão: 17

## Lógica utilizada

Na primeira versão do programa fiz um programa simples que percorria todo o intervalo de números e verificava se um número era primo ou não. Utilizando a seguinte estrutura de controle:

```Java
    // Itera de 2 até o número
    for (int i = 2; i < numero; i++) {
        // Se encontrar um divisor, o número não é primo
        if (numero % i == 0) {
            return false;
        }
    }
```

Após testar, pesquisei se havia alguma solução mais eficiente que essa. Descobri que havia outra solução baseada na Teorema Fundamental da Aritmética e na simetria dos fatores. Segundo essa teoria, se um número não for primo, pelo ou menos um de seus fatores deve ser menor ou igual a raiz quadrada desse número.

Portanto, optei por enviar a solução mais otimizada após a pesquisa.

Nova estrutura de controle:

`for (int i = 2; i * i <= numero; i++)`

## Como Rodar o Desafio

Siga os passos abaixo no seu terminal para compilar e executar o projeto:

### 1\. Navegue até a pasta do projeto

Entre no diretório onde o arquivo principal (`Main.java`) se encontra:

```bash
cd desafio-02/lgjor/java
```

### 2\. Execute o Programa

Utilize o comando `java`:

```bash
java Main.java
```

### Licença de uso

Este projeto está licenciado sob a **[MIT License](https://opensource.org/licenses/MIT)**.

A licença MIT é uma licença permissiva que permite a reutilização, cópia, modificação, fusão, publicação, distribuição, sublicenciamento e/ou venda do software.

Autor: Lucas Godoy

- Sinta-se à vontade para copiar e reutilizar este exercício, ou partes dele, em qualquer ambiente de aprendizado, aula, material didático ou projeto educacional. Ao utilizar o código, fortaleça a comunidade e referencie os autores do desafio.

## Site de referência e repositório original

- [Site: Os programadores](https://osprogramadores.com/desafios/d02/)
- [Repositório oficial: Os Programadores - Desafios](https://github.com/OsProgramadores/op-desafios)

