# Desafio 02

### Foi utilizado o pacote [PestPHP](https://pestphp.com/docs/installation "PestPHP") para os testes com a linguagem PHP. Bem como, o composer para gerenciá-lo.

#### Um procedimento para executar os testes:
1 - `composer install`
2 - `composer dumpautoload -o`
3 - `./vendor/bin/pest tests/ListandoPrimosEntreUmEDezMilTest.php`

#### A forma como as importações e namespace está configurado, se encontra no arquivo *composer.json* em "autoload".