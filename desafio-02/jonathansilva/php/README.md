## Desafio 02

> Primos

**Requisitos**

- PHP >= 8.2

Abra o terminal, navegue até a pasta onde se encontra o código fonte e execute o comando abaixo

```bash
php index.php
```

---

Se não tiver o PHP instalado, use serviços online como o [OnlinePHP](https://onlinephp.io)

1 - Copie todo o conteúdo da classe Primos e cole em `PHP Sandbox`

2 - Abaixo do fechamento da classe, coloque o seguinte código

```php
try {
    new Primos(1, 10000);
} catch (InvalidArgumentException $e) {
    echo $e->getMessage();
}
```

3 - Em `PHP Versions and Options`, selecione a versão 8.2.0. Desmarque qualquer outra versão que estiver selecionada

4 - Clique em `Execute Code`
