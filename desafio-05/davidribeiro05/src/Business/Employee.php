<?php

namespace Src\Business;

use Src\Model\Data;
use Src\Lib\Filter;

/**
 * Author: David Ribeiro
 * Class Employee
 * @package Src\Business
 */
class Employee extends Data
{
    /**
     * @var Filter
     */
    private Filter $filter;

    /**
     * @return string
     */
    public function maxSalaryByLastName(): string
    {
        $salary = $this->filter()->maxSalary($this->salary());

        foreach ($this->data() as $value) {
            if ($salary == $value['salario']) {
                return "last_name_max|{$value['sobrenome']}|{$value['nome']} {$value['sobrenome']}
                    |{$this->filter()->standardNumberFormat($value['salario'])}" . PHP_EOL;
            }
        }
    }

    /**
     * @return Filter
     */
    public function filter(): Filter
    {
        return $this->filter = new Filter();
    }
}