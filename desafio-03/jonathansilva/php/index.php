<?php

declare(strict_types=1);

require_once __DIR__ . './Palindromos.php';

try {
    $limiteInicial = (int) $argv[1];
    $limiteFinal = (int) $argv[2];

    $palindromos = new Palindromos($limiteInicial, $limiteFinal);
    $palindromos->process();
} catch (InvalidArgumentException $e) {
    echo $e->getMessage();
}