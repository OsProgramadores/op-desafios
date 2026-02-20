## DESAFIO 03 - PALÍNDROMOS

### 🙋Autor
- Nome: Lestter Gabriel
- Área: Desenvolvimento Web

Desenvolvido em JavaScript <br />
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)


### 🖥️Funcionamento
Obtenho os argumentos de início e fim passados na execução do código e os valido antes de executar de fato a lógica.
Após isso, eu sigo com a lógica, passando por cada valor e criando uma cópia intertida para comparação. Se a cópia
for igual ao original, o número é adicionado ao array Palíndromos, que os exibo na tela através de um outro FOR.

### ✅Requisitos
- NodeJS a partir da versão 20.17.0 <br />
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)

### ⚙️Execução
Não é preciso nenhuma dependência. Execute com:
```shell
node main.js <arg1> <arg2>
```
>Se for passado nenhum ou mais que *2 valores* ou que não sejam *numéricos* um erro será informado e o script não será executado

- Exemplo VÁLIDO <br />
  ![NodeJS](https://img.shields.io/badge/Válido-00FF00?style=for-the-badge)

```shell
node main.js 100 1000
```


- Exemplos INVÁLIDOS<br />
  ![NodeJS](https://img.shields.io/badge/inválido-DC143C?style=for-the-badge)
```shell
node main.js asd 1000
```
ou
```shell
node main.js 100 1000 2000
```

### Licença
Este código é público e qualquer pessoa está livre para usar e modificar conforme suas necessidades sem quais burocracias jurídicas
