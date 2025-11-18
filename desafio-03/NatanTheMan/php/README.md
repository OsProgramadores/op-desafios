# Palíndromos

Um palíndromo é uma palavra ou expressão que pode ser lida da esquerda para a direita ou da direita para a esquerda mantendo o mesmo significado. Exemplo: "reviver", "ovo", "arara", "osso", etc.
No caso deste desafio: "2", "7007", "111", "919", etc.

## Objetivo do Programa

Ler dois números inteiros e retornar os palíndromos que existem no intervalos entre eles.

## Requisitos

O programa foi escrito em PHP, versão 8.4.13. Para instrucoes de como instalar o PHP em seu OS consulte: [PHP: Downloads & Installation Instructions](https://www.php.net/downloads.php)

PHPUnit versao 10.5.58. Instale-o com:
```
wget -O phpunit.phar https://phar.phpunit.de/phpunit-10.phar
```

Certifique-se de que os arquivos `index.php` e `phpunit.phar` tem permissao para serem executados.

Caso nao possuam permissao, conceda com este comando:
```
chmod +x index.php phpunit.phar
```

## Como rodar

A ordem dos argumentos não importa, o programa saberá lidar com isso. Ele sempre utilizara o menor valor fornecido como inicio e o maior como fim.

```
php index.php <start> <end>
```
ou
```
./index.php <start> <end>
```

`start` - inteiro positivo\
`end`   - inteiro positivo

Número máximo unsigned int de 64bits.

## Rodar testes

```
./phpunit.phar tests --testdox
```
