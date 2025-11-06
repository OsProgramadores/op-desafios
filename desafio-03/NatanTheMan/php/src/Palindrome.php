<?php

namespace App;

use InvalidArgumentException;

class Palindrome
{
    public function __construct(string $start, string $end)
    {
        throw new InvalidArgumentException("foo");
    }
}
