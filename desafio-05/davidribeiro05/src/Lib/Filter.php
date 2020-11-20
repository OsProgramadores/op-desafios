<?php

namespace Src\Lib;

/**
 * Author: David Ribeiro
 * Class Filter
 * @package Src\Lib
 */
class Filter
{
    /**
     * @param array $array
     * @return float|null
     */
    public function maxSalary(array $array): ?float
    {
        return max($array);
    }

    /**
     * @param array $array
     * @return float|null
     */
    public function minSalary(array $array): ?float
    {
        return min($array);
    }

    /**
     * @param float $number
     * @return string
     */
    public function standardNumberFormat(float $number)
    {
        return number_format($number, 2, ",", ".");
    }
}