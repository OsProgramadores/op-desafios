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

Para testar a solução, clone o repositório, navegue até o diretório e instale as dependências. Depois, utilize o node.js para rodar o programa em sua máquina:

```bash
$ git clone git@github.com:OsProgramadores/op-desafios.git
$ cd .\op-desafios\desafio-03\bpires\javascript\
$ npm install
$ node 03-palindromos.js
```

> **Nota:** Foi utilizado o pacote prompt-sync para node com o objetivo de permitir a leitura de inputs do usuário.
