<?php

namespace Src\Model;

/**
 * Author: David Ribeiro
 * Class Data
 * @package Src\Model
 */
abstract class Data
{
    /**
     * @var
     */
    private $data;

    /**
     * @var
     */
    private $salary;

    /**
     * @var
     */
    private $department;

    /**
     * Data constructor.
     */
    public function __construct()
    {
        $this->readerEmployee();
    }

    /**
     * @return mixed
     */
    public function data()
    {
        return $this->data;
    }

    /**
     * @return mixed
     */
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

    /**
     * @return mixed
     */
    protected function salary()
    {
        foreach ($this->data as $key => $value) {
            $arr[] = $value['salario'];
        }
        return $this->salary = $arr;
    }

    /**
     * @return mixed
     */
    protected function department()
    {
        foreach ($this->data as $key => $value) {
            $arr[] = $value['area'];
        }
        return $this->department = $arr;
    }

}