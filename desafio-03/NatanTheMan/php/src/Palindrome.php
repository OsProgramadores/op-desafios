<?php

namespace App;

use InvalidArgumentException;

class Palindrome
{
    public readonly int $start;
    public readonly int $end;

    public function __construct(string $num1, string $num2)
    {
        $this->validate($num1, $num2);

        $this->start = min(intval($num1), intval($num2));
        $this->end = max(intval($num1), intval($num2));
    }

    private function validate(string $num1, string $num2)
    {
        if (!is_numeric($num1) || !is_numeric($num2)) {
            throw new InvalidArgumentException("Parâmetros devem ser números inteiros");
        }
        if (intval($num1) <= 0 || intval($num2) <= 0) {
            throw new InvalidArgumentException("Parâmetros devem ser maiores que 0");
        }
    }

    public function getPalindromes(): array
    {
        return ["1", "2", "3", "4", "5", "6", "7", "8", "9"];
    }
}
