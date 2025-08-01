## DESAFIO 03 - PALÍNDROMOS

### Funcionamento
Obtenho os argumentos de início e fim passados na execução do código e os valido antes de executar de fato a lógica. 
Após isso, eu sigo com a lógica, passando por cada valor e criando uma cópia intertida para comparação. Se a cópia
for igual ao original, o número é adicionado ao array Palíndromos, que os exibo na tela através de um outro FOR.

### Requisitos
- NodeJS a partir da versão 20.17.0

### Execução
Não é preciso nenhuma dependência. Execute com:
```shell
node main.js <arg1> <arg2>
```
>Se for passado nenhum ou mais que *2 valores* ou que não sejam *numéricos* um erro será informado e o script não será executado

- Exemplo VÁLIDO
```shell
node main.js 100 1000
```


- Exemplos INVÁLIDOS
```shell
node main.js asd 1000
```
ou
```shell
node main.js 100 1000 2000
```
