<?php

declare(strict_types=1);

require_once __DIR__ . './Primos.php';

try {
    $primos = new Primos(1, 10000);
    $primos->process();
} catch (InvalidArgumentException $e) {
    echo $e->getMessage();
}