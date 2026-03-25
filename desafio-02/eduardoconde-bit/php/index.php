<?php

// Using Eratosthenes Sieve O(n log log n)
function sieveOfEratosthenes(int $limit): void
{
    if ($limit < 0) {
        throw new LogicException("Limit: $limit, limit number cannot be negative");
    }

    // Initialize all numbers as prime
    $sieve = array_fill(0, $limit + 1, true);
    $sieve[0] = $sieve[1] = false; // 0 and 1 are not prime

    // Mark all even numbers > 2 as not prime = [n = 2k com k > 1 ⟹ n, not is prime]
    //Complexity O(n/2)
    for ($i = 4; $i <= $limit; $i += 2) {
        $sieve[$i] = false;
    }

    // Mark multiples of odd numbers starting from 3, O(n/2) + O(n/3) ... = O(n log log n)
    for ($i = 3; $i <= sqrt($limit); $i += 2) {
        if ($sieve[$i]) {
            for ($j = $i * $i; $j <= $limit; $j += $i * 2) { // Multiples of i
                $sieve[$j] = false;
            }
        }
    }

    for ($i = 0; $i <= $limit; $i++) {
        if ($sieve[$i]) {
            echo $i . PHP_EOL;
        }
    }
}

$limit = 10000;

try {
    sieveOfEratosthenes($limit);
} catch (LogicException) {
    echo "Apenas Inteiros não negativos são aceitos como limite para busca!";
}
