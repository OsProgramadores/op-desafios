#!/usr/bin/env php
<?php

require __DIR__ . "/vendor/autoload.php";

use App\Palindrome;

try {
    $palindrome = new Palindrome($argv[1] ?? null, $argv[2] ?? null);
    foreach ($palindrome->getPalindromes() as $item) {
        echo $item, PHP_EOL;
    }
} catch (Exception $e) {
    echo $e->getMessage(), PHP_EOL;
}
