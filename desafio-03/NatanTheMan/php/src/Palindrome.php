<?php

namespace App;

use InvalidArgumentException;

class Palindrome
{
    public function __construct(string $start, string $end)
    {
        if (!is_numeric($start) || !is_numeric($end)) {
            throw new InvalidArgumentException("Parâmetros devem ser números inteiros");
        }
        if (intval($start) <= 0 || intval($end) <= 0) {
            throw new InvalidArgumentException("Parâmetros devem ser maiores que 0");
        }
        if (!is_int($start) || !is_int($start)) {
            throw new InvalidArgumentException("Parâmetros devem ser inteiros");
        }
    }
}
