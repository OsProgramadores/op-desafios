<?php

namespace App;

use InvalidArgumentException;

class Palindrome
{
    public function __construct(string $start, string $end)
    {
        if (intval($start) <= 0 || intval($end) <= 0) {
            throw new InvalidArgumentException("Parâmetros devem ser maior que 0");
        }
        throw new InvalidArgumentException("foo");
    }
}
