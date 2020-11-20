<?php

namespace Src\Model;

abstract class Data
{
    private $data;

    private $salary;

    private $department;

    public function __construct()
    {
        $this->readerEmployee();
    }

    public function data()
    {
        return $this->data;
    }

    protected function readerEmployee()
    {
        $json = file_get_contents(__DIR__ . "/Funcionarios10K.json");
        $jsonDecoded = json_decode($json);

        foreach ($jsonDecoded->areas as $area) {
            foreach ($jsonDecoded->funcionarios as $func) {
                if ($func->area == $area->codigo) {
                    $arr = [
                        "nome" => $func->nome,
                        "sobrenome" => $func->sobrenome,
                        "salario" => $func->salario,
                        "area" => $area->nome
                    ];

                    $this->data[] = $arr;
                }
            }
        }
        return $this->data;
    }

    protected function salary()
    {
        foreach ($this->data as $key => $value) {
            $arr[] = $value['salario'];
        }
        return $this->salary = $arr;
    }

    protected function department()
    {
        foreach ($this->data as $key => $value) {
            $arr[] = $value['area'];
        }
        return $this->department = $arr;
    }

}