# OsProgramadores.com

### Desafio #3: Números palindrômicos

**Instruções:** Imprima todos os números palindrômicos entre dois outros números, incluindo ambos extremos.

Para o desafio, assuma:

- Apenas inteiros positivos podem ser usados como limites.
- Números de um algarismo são palíndromos por definição.
- Máximo número: (1 << 64) - 1 (máximo unsigned int de 64 bits).

### Racional da solução:

```
├── verificar se o input é um número, e se os parâmetros estão na ordem correta.
├── para testar se é palíndromo:
│   ├── em uma variável para teste, transformar o número em um array
│   │   contendo seus algarismos
│   ├── inverter a ordem do array e unir os algarismos novamente
│   ├── transformar a string resultando em um número
│   └── comparar a variável de testes com o parâmetro passado para
│       a função
└── se for palíndromo, imprimir o número na tela

```
### Teste e execução

Para testar a solução, é necessário ter o [Node.js](https://nodejs.org/) instalado em sua máquina.

Faça um clone do repositório para a máquina local, e rode o arquivo no node, passando os números como argumentos:

```bash
$ git clone git@github.com:OsProgramadores/op-desafios.git

$ cd .\op-desafios\

$ node .\desafio-03\bpires\javascript\03-palindromos.js "número 1" "número 2"
```
