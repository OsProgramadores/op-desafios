<?php

namespace Src\Lib;

class Filter
{
    public function maxSalary(array $array): ?float
    {
        return max($array);
    }

    public function minSalary(array $array): ?float
    {
        return min($array);
    }

    public function standardNumberFormat(float $number)
    {
        return number_format($number, 2, ",", ".");
    }
}