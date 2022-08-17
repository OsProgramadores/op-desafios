<?php

use Klisostom\Php\Tests\PrimosMock;
use Klisostom\Php\ListandoPrimosEntreUmEDezMil;

test('Listando números primos.', function () {
    // Arrange
    $listandoPrimos = new ListandoPrimosEntreUmEDezMil;
    $primosAteDezMil = new PrimosMock;
    $maxValue = 10000;

    // Act
    $expected = $primosAteDezMil->mock();

    // Assert
    expect($listandoPrimos->listar($maxValue))->toEqualCanonicalizing($expected);
});
