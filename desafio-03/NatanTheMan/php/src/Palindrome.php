<?php

namespace App;

use InvalidArgumentException;

class Palindrome
{
    public readonly int $start;
    public readonly int $end;

    public function __construct($num1, $num2)
    {
        $this->validate($num1, $num2);

        $this->start = min(intval($num1), intval($num2));
        $this->end = max(intval($num1), intval($num2));
    }

    private function validate($num1, $num2)
    {
        if (is_null($num1) || is_null($num2))
            throw new InvalidArgumentException("Informe os parâmetros necessários");
        if (!is_numeric($num1) || !is_numeric($num2))
            throw new InvalidArgumentException("Parâmetros devem ser números inteiros");
        if (intval($num1) <= 0 || intval($num2) <= 0)
            throw new InvalidArgumentException("Parâmetros devem ser maiores que 0");
    }

    public function getPalindromes(): array
    {
        $palindromes = [];
        for ($i = $this->start; $i <= $this->end; $i++) {
            if (strlen($i) == 1 || strval($i) == strrev(strval($i)))
                array_push($palindromes, strval($i));
        }
        return $palindromes;
    }
}
