<?php

require __DIR__ . "/vendor/autoload.php";

use App\Palindrome;


try {
    $palindrome = new Palindrome($argv[1], $argv[2]);
    foreach ($palindrome->getPalindromes() as $item) {
        echo $item, PHP_EOL;
    }
} catch (Exception $e) {
    echo $e->getMessage();
}
