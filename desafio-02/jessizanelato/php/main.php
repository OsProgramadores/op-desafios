<?php

require_once("NumerosPrimos.php");

$start = microtime(true);

$numerosPrimos = NumerosPrimos::encontrarNumerosPrimos(1, 10000);

foreach ($numerosPrimos as $numero) {
    echo $numero . " é um número primo.\n";
}

$totalNumerosPrimos = count($numerosPrimos);

echo "Total de números primos encontrados: {$totalNumerosPrimos}.\n";

echo "Tempo de execução: " . (microtime(true) - $start) . " segundos\n";