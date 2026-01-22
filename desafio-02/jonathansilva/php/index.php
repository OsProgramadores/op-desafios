<?php

declare(strict_types=1);

require_once __DIR__ . './Primos.php';

try {
    new Primos(1, 10000);
} catch (InvalidArgumentException $e) {
    echo $e->getMessage();
}