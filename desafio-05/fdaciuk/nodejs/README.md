# Desafio 05 - Node.js

## Versão do Node.js

Preferencialmente a mais recente, mas o programa vai funcionar corretamente com a v12 ou posterior.

## Como executar

O arquivo `app.js` já tem permissão de execução, então só precisa usar:

```js
$ ./app.js Funcionarios5M.json | sort | md5sum
```

Ou então, usando a CLI do Node.js:

```js
$ node app.js Funcionarios5M.json | sort | md5sum
```

## Autor

[Fernando Daciuk (@fdaciuk)](https://github.com/fdaciuk)

## Observações gerais

- Não use esse tipo de código em casa (ou no trabalho);
- O código não foi feito pensando em boas práticas, e sim performance / escovação de bits;
- Use com moderação.
