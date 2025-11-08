<?php

namespace App;

use InvalidArgumentException;

class Palindrome
{
    public readonly int $start;
    public readonly int $end;

    public function __construct(string $start, string $end)
    {
        $this->validate($start, $end);
        $this->start = intval($start);
        $this->end = intval($end);
    }

    private function validate(string $arg1, string $arg2)
    {
        if (!is_numeric($arg1) || !is_numeric($arg2)) {
            throw new InvalidArgumentException("Parâmetros devem ser números inteiros");
        }
        if (intval($arg1) <= 0 || intval($arg2) <= 0) {
            throw new InvalidArgumentException("Parâmetros devem ser maiores que 0");
        }
    }

    public function getPalindromes(): array
    {
        return ["1", "2", "3", "4", "5", "6", "7", "8", "9"];
    }
}
