## Desafio 02

**Descrição**

Lista todos os números primos entre 1 e 10.000

**Requisitos**

PHP >= 8.2

**Como executar**

Abra o terminal, navegue até a pasta onde se encontra o código fonte e execute o comando abaixo

```bash
php index.php
```

---

Obs: Se não tiver o PHP instalado, use serviços online como o [OnlinePHP](https://onlinephp.io)

1 - Copie todo o conteúdo da classe Primos e cole em `PHP Sandbox`

2 - Abaixo do fechamento da classe, coloque o seguinte código

```php
try {
    $primos = new Primos(1, 10000);
    $primos->process();
} catch (InvalidArgumentException $e) {
    echo $e->getMessage();
}
```

3 - Em `PHP Versions and Options`, selecione a versão 8.2.0. Desmarque qualquer outra versão que estiver selecionada

4 - Clique em `Execute Code`

---

**Otimização**

Para que a execução fique mais eficiente, utilizei um "limitador" no loop onde verifica se o divisor é menor que o número. O loop vai percorrer até que o divisor seja **menor ou igual à raiz quadrada** do número

> Antes

```php
$divisor < $i;
```

*Exemplo:*

Para saber se o número 97 é primo, eram realizadas 95 verificações ( 2 a 96 )

97 / 2
97 / 3
...
97 / 96

> Depois

```php
$divisor <= sqrt($i);
```

Agora, calculando a raiz quadrada de 97 ( 9.84 ), serão realizadas apenas 8 verificações ( 2 a 9 )

Para evitar que `$i` receba um falso positivo, é preciso usar o operador `<=` para que o loop verifique até o valor exato da raiz quadrada
