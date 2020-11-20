<?php

require_once __DIR__ . "/autoload.php";

use Src\Business\Company;
use Src\Business\Department;
use Src\Business\Employee;

$company = new Company();
$department = new Department();
$employee = new Employee();

echo $company->min();
echo $company->max();
echo $company->average();

echo $department->min();
echo $department->max();
echo $department->average();

echo $department->mostEmployees();
echo $department->leastEmployees();

echo $employee->maxSalaryByLastName();