<?php

namespace Src\Business;

use Src\Lib\Filter;
use Src\Model\Data;

/**
 * Author: David Ribeiro
 * Class Department
 * @package Src\Business
 */
class Department extends Data implements Calculate
{
    /**
     * @var Filter
     */
    private Filter $filter;

    /**
     * @return string
     */
    public function max(): string
    {
        $salary = $this->filter()->maxSalary($this->salary());

        foreach ($this->data() as $value) {
            if ($salary == $value['salario']) {
                return "area_max|{$value['area']}|{$value['nome']} {$value['sobrenome']}|
                 {$this->filter()->standardNumberFormat($value['salario'])}" . "<br>";
            }
        }
    }

    /**
     * @return string
     */
    public function min(): string
    {
        $salary = $this->filter()->minSalary($this->salary());

        foreach ($this->data() as $value) {
            if ($salary == $value['salario']) {
                return "area_min|{$value['area']}|{$value['nome']} {$value['sobrenome']}|
                 {$this->filter()->standardNumberFormat($value['salario'])}" . "<br>";
            }
        }
    }

    /**
     * @return string
     */
    public function average(): string
    {
        foreach ($this->data() as $value) {
            $sum[] = $value['salario'];
            $count[] = $value['salario'];
            $result = array_sum($sum) / count($count);
        }

        return "area_avg|{$value['area']}|" . $this->filter()->standardNumberFormat($result) . "<br>";
    }

    /**
     * @return string
     */
    public function mostEmployees(): string
    {
        $countDepartments = array_count_values($this->department());
        $maxDepartments = $this->filter()->maxSalary($countDepartments);

        foreach ($countDepartments as $key => $value) {
            if ($maxDepartments == $value) {
                return "most_employees|" . $key . "|" . $value . "<br>";
            }
        }
    }

    /**
     * @return string
     */
    public function leastEmployees(): string
    {
        $countDepartments = array_count_values($this->department());
        $minDepartments = $this->filter()->minSalary($countDepartments);

        foreach ($countDepartments as $key => $value) {
            if ($minDepartments == $value) {
                return "least_employees|" . $key . "|" . $value . "<br>";
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