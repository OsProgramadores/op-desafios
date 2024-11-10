Claro! Aqui está o **README** atualizado com o autor:

---

# Anagrama

Este programa em Java gera anagramas válidos de uma expressão fornecida pelo usuário, utilizando um arquivo de palavras válidas. O programa pode ser utilizado para gerar anagramas tanto de uma palavra quanto de uma frase. Ele ignora os espaços e converte todas as letras para maiúsculas.

## Funcionalidade

O programa recebe uma expressão do usuário, valida a entrada, gera todas as combinações possíveis de anagramas válidos (palavras existentes no arquivo de palavras válidas) e exibe esses anagramas ordenados. A busca por anagramas é feita utilizando permutações das letras da expressão.

### Como Funciona

1. **Carregamento de Palavras Válidas**: O programa carrega as palavras válidas a partir de um arquivo chamado `words.txt`. Esse arquivo deve conter uma lista de palavras, com uma palavra por linha.
   
2. **Validação da Entrada**: A expressão fornecida pelo usuário é validada para garantir que ela contenha apenas caracteres alfabéticos e espaços. Se a entrada for inválida, o programa exibirá uma mensagem de erro e encerrará a execução.

3. **Geração de Anagramas**: O programa gera as permutações possíveis da expressão, removendo letras à medida que as palavras válidas forem formadas. Apenas as combinações que formam palavras presentes no arquivo de palavras válidas são consideradas.

4. **Exibição dos Resultados**: Todos os anagramas válidos encontrados são exibidos ao usuário, ordenados em ordem alfabética.

## Requisitos

- Java Runtime Environment (JRE) 8 ou superior.
- Arquivo `words.txt` com uma lista de palavras válidas, que pode ser obtido [aqui](https://osprogramadores.com/desafios/d06/words.txt).

## Como Executar

1. Compile o código:

   ```bash
   javac Anagrama.java
   ```

2. Execute o programa, passando a expressão desejada como argumento:

   ```bash
   java Anagrama
   ```

   O programa pedirá para que você digite a expressão (uma palavra ou frase).

3. O programa gerará e exibirá os anagramas encontrados.

### Exemplo 1 - Expressão: uma palavra

Entrada:

```bash
Digite a expressão (palavra ou frase): vermelho
```

Saída:

```bash
Anagramas encontrados:
ELM HO REV
ELM HOVER
ELM OH REV
HELM OVER
HELM ROVE
HOLM VEER
LEVER OHM
OHM REVEL
```

### Exemplo 2 - Expressão: uma frase

Entrada:

```bash
Digite a expressão (palavra ou frase): oi gente
```

Saída:

```bash
Anagramas encontrados:
EGO I NET
EGO I TEN
EGO TINE
ENG I TOE
EON GET I
GEE I NOT
GEE I TON
GEE IN TO
GEE INTO
GEE IT NO
GEE IT ON
GEE OINT
GEE TONI
GENE I TO
GENE ITO
GENIE TO
GET I ONE
GINO TEE
GO I TEEN
GO IN TEE
GONE TIE
```

## Detalhes do Código

### 1. **Função `carregarPalavrasValidas`**

Carrega um conjunto de palavras válidas a partir de um arquivo de texto. As palavras são lidas, convertidas para maiúsculas e adicionadas a um `Set` para garantir a unicidade.

### 2. **Função `validarEntrada`**

Verifica se a expressão fornecida contém apenas letras (A-Z) e espaços. Caso contrário, o programa exibe uma mensagem de erro e encerra a execução.

### 3. **Função `gerarAnagramas`**

Processa a expressão fornecida, removendo espaços e convertendo para maiúsculas, e então gera os anagramas possíveis verificando se as permutações formam palavras válidas.

### 4. **Função `gerarCombinacoes`**

Esta função recursiva é responsável por gerar todas as combinações possíveis de letras da expressão e verificar se elas correspondem a palavras válidas do conjunto de palavras carregadas.

### 5. **Função `permutar`**

Gera todas as permutações possíveis de uma lista de letras de tamanho específico.

### 6. **Função `permutarRecursivo`**

Função auxiliar recursiva para gerar permutações de uma lista de letras. Ela assegura que as permutações sejam únicas, evitando duplicações.

## Dependências

- **`java.io`**: Para ler o arquivo de palavras válidas e interagir com o sistema de arquivos.
- **`java.util`**: Para manipulação de listas, conjuntos e ordenação.

## Observações

- Certifique-se de que o arquivo `words.txt` esteja no mesmo diretório que o programa ou ajuste o caminho do arquivo na linha que faz a leitura (`BufferedReader reader = new BufferedReader(new FileReader(arquivo));`).
- O programa é sensível à entrada e apenas palavras alfabéticas e espaços são aceitas. Se a entrada contiver caracteres especiais ou números, o programa exibirá uma mensagem de erro.

## Links Úteis

- [Arquivo de palavras válidas (words.txt)](https://osprogramadores.com/desafios/d06/words.txt)

## Licença

Este programa é de código aberto. Sinta-se à vontade para modificar e usar conforme necessário.

## Autor

- **Maurilio Souza**
