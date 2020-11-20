<?php

namespace Src\Business;

use Src\Lib\Filter;
use Src\Model\Data;

/**
 * Author: David Ribeiro
 * Class Company
 * @package Src\Business
 */
class Company extends Data implements Calculate
{
    /**
     * @var Filter
     */
    private Filter $filter;

    /**
     * @return string|void
     */
    public function max(): string
    {
        $salary = $this->filter()->maxSalary($this->salary());

        foreach ($this->data() as $value) {
            if ($salary == $value['salario']) {
                return "global_max|{$value['nome']} {$value['sobrenome']}|
                        {$this->filter()->standardNumberFormat($value['salario'])}" . "<br>";
            }
        }
    }

    /**
     * @return string|void
     */
    public function min(): string
    {
        $salary = $this->filter()->minSalary($this->salary());

        foreach ($this->data() as $value) {
            if ($salary == $value['salario']) {
                return "global_min|{$value['nome']} {$value['sobrenome']}|
                      {$this->filter()->standardNumberFormat($value['salario'])}" . "<br>";
            }
        }
    }

    /**
     * @return string|void
     */
    public function average(): string
    {
        foreach ($this->data() as $value) {
            $sum[] = $value['salario'];
            $count[] = $value['salario'];
            $result = array_sum($sum) / count($count);
        }

        return "global_avg|" . $this->filter()->standardNumberFormat($result) . "<br>";
    }

    /**
     * @return Filter
     */
    private function filter(): Filter
    {
        return $this->filter = new Filter();
    }


}