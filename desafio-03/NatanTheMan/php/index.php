<?php

use app\Palindrome;

try {
    $x = new Palindrome($argv, $argc);
    $palindromes = $x->execute();
    foreach ($palindromes as $p) {
        echo $p;
    }
} catch (Exception $e) {
    echo $e->getMessage();
}
