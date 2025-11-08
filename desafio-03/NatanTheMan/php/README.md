# Palíndromos

Um palíndromo é uma palavra ou expressão que pode ser lida da esquerda para a direita ou da direita para a esquerda mantendo o mesmo significado. Exemplo: "reviver", "ovo", "arara", "osso", etc.
No caso deste desafio: "2", "7007", "111", "919", etc.

## Objetivo do Programa

Ler dois números inteiros e retornar os palíndromos que existem no intervalos entre eles.

## Como rodar

```
php index.php <start> <end>
```

`start` - inteiro positivo\
`end`   - inteiro positivo

A ordem dos argumentos não importa, o programa saberá lidar com isso.

Número máximo unsigned int de 64bits.

## Rodar testes

```
./vendor/bin/phpunit tests --testdox
```

---

O programa foi escrito em PHP, versão 8.4.13.
