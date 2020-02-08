<?php
Class Funcionarios {
  protected $funcionarios_info;
  protected $qtdPorArea;

  public function __construct() {
    $this->funcionarios_info = json_decode(file_get_contents("funcionarios.json"));
    $this->qtdPorArea = [];
  }

  public function MaioresSalarios() {
    $global_max = [];

    foreach($this->funcionarios_info->funcionarios as $index => $valor) {
      if($index == 0) {
        array_push($global_max, array("nome" => $valor->nome,
                                      "sobrenome" => $valor->sobrenome,
                                      "salario" => $valor->salario));
      } else {
        if($global_max[0]["salario"] < $valor->salario) {
            $global_max = [];
            array_push($global_max, array("nome" => $valor->nome,
                                      "sobrenome" => $valor->sobrenome,
                                      "salario" => $valor->salario));
        } else if($global_max[0]["salario"] == $valor->salario) {
            array_push($global_max, array("nome" => $valor->nome,
                                      "sobrenome" => $valor->sobrenome,
                                      "salario" => $valor->salario));
        }
      }
    }

    foreach($global_max as $valor) {
      echo "global_max|$valor[nome] $valor[sobrenome]|$valor[salario]<br>";
    }
  }

  public function MenoresSalarios() {
    $global_min = [];

    foreach($this->funcionarios_info->funcionarios as $index => $valor) {
      if($index == 0) {
        array_push($global_min, array("nome" => $valor->nome,
                                      "sobrenome" => $valor->sobrenome,
                                      "salario" => $valor->salario));
      } else {
        if($global_min[0]["salario"] > $valor->salario) {
            $global_min = [];
            array_push($global_min, array("nome" => $valor->nome,
                                      "sobrenome" => $valor->sobrenome,
                                      "salario" => $valor->salario));
        } else if($global_min[0]["salario"] == $valor->salario) {
            array_push($global_min, array("nome" => $valor->nome,
                                      "sobrenome" => $valor->sobrenome,
                                      "salario" => $valor->salario));
        }
      }
    }

    foreach($global_min as $valor) {
      echo "global_min|$valor[nome] $valor[sobrenome]|$valor[salario]<br>";
    }
  }

  public function MediaSalarios() {
    $global_avg = [];

    foreach($this->funcionarios_info->funcionarios as $valor) {
      array_push($global_avg, intval($valor->salario));
    }

    $mediaSalarios = number_format(array_sum($global_avg) / count($global_avg), 2, '.', '');

    echo "global_avg|$mediaSalarios";
  }

  protected function maxMinMediaPorArea($funcAreaArray, $nomeArea) {
    $area_max = [];
    $area_min = [];
    $area_avg = [];
    $area_nome = null;

    switch($nomeArea) {
      case "SM":
        $area_nome = "Gerenciamento de Software";
        array_push($this->qtdPorArea, array("area" => $area_nome, "quantidadeFunc" => count($funcAreaArray)));
        break;
      case "UD":
        $area_nome = "Designer de UI/UX";
        array_push($this->qtdPorArea, array("area" => $area_nome, "quantidadeFunc" => count($funcAreaArray)));
        break;
      case "SD":
        $area_nome = "Desenvolvimento de Software";
        array_push($this->qtdPorArea, array("area" => $area_nome, "quantidadeFunc" => count($funcAreaArray)));
        break;
    }

    foreach($funcAreaArray as $index => $valor) {
      if($index == 0) {
        array_push($area_max, array("nome" => $valor['nome'],
                                      "sobrenome" => $valor['sobrenome'],
                                      "salario" => $valor['salario']));
      } else {
        if($area_max[0]["salario"] < $valor['salario']) {
          $area_max = [];
          array_push($area_max, array("nome" => $valor['nome'],
                                        "sobrenome" => $valor['sobrenome'],
                                        "salario" => $valor['salario']));
        } else if($area_max[0]["salario"] == $valor['salario']) {
          array_push($area_max, array("nome" => $valor['nome'],
                                        "sobrenome" => $valor['sobrenome'],
                                        "salario" => $valor['salario']));
        }
      }
    }
    
    foreach($funcAreaArray as $index => $valor) {
      if($index == 0) {
        array_push($area_min, array("nome" => $valor['nome'],
                                      "sobrenome" => $valor['sobrenome'],
                                      "salario" => $valor['salario']));
      } else {
        if($area_min[0]["salario"] > $valor['salario']) {
            $area_min = [];
            array_push($area_min, array("nome" => $valor['nome'],
                                      "sobrenome" => $valor['sobrenome'],
                                      "salario" => $valor['salario']));
        } else if($area_min[0]["salario"] == $valor['salario']) {
            array_push($area_min, array("nome" => $valor['nome'],
                                      "sobrenome" => $valor['sobrenome'],
                                      "salario" => $valor['salario']));
        }
      }
    }

    foreach($funcAreaArray as $valor) {
      array_push($area_avg, intval($valor['salario']));
    }

    $mediaSalarios = number_format(array_sum($area_avg) / count($area_avg), 2, '.', '');

    foreach($area_max as $valor) {
      echo "area_max|$area_nome|$valor[nome] $valor[sobrenome]|$valor[salario]<br>";
    }

    foreach($area_min as $valor) {
      echo "area_min|$area_nome|$valor[nome] $valor[sobrenome]|$valor[salario]<br>";
    }

    echo "area_avg|$area_nome|$mediaSalarios<br>";
  }

  public function mostrarDadosPorArea() {
    $arraySM = [];
    $arrayUD = [];
    $arraySD = [];
    $arrayQtd = [];

    foreach($this->funcionarios_info->funcionarios as $valor) {
      switch($valor->area) {
        case "SM":
          array_push($arraySM, array("nome" => $valor->nome,
                                        "sobrenome" => $valor->sobrenome,
                                        "salario" => $valor->salario));
          break;
        case "UD":
          array_push($arrayUD, array("nome" => $valor->nome,
                                     "sobrenome" => $valor->sobrenome,
                                     "salario" => $valor->salario));
          break;
        case "SD":
          array_push($arraySD, array("nome" => $valor->nome,
                                     "sobrenome" => $valor->sobrenome,
                                     "salario" => $valor->salario));
          break;
      }
    }

    $this->maxMinMediaPorArea($arraySM, "SM");
    $this->maxMinMediaPorArea($arrayUD, "UD");
    $this->maxMinMediaPorArea($arraySD, "SD");

    foreach($this->qtdPorArea as $valor) {
      array_push($arrayQtd, $valor['quantidadeFunc']);
    }

    foreach($this->qtdPorArea as $valor) {
      if($valor["quantidadeFunc"] == max($arrayQtd)) {
        echo "most_employees|$valor[area]|$valor[quantidadeFunc]<br>";
      }
    }

    foreach($this->qtdPorArea as $valor) {
      if($valor["quantidadeFunc"] == min($arrayQtd)) {
        echo "least_employees|$valor[area]|$valor[quantidadeFunc]<br>";
      }
    }
  }

  public function maioresSalariosPorMesmoSobrenome() {
    $arraySobrenomes = [];
    $arrayFuncSobrenomesQtdMaior1 = [];
    $arraySobrenomesQtdMaior1 = [];
    $arrayFuncSobrenomeMaiorSalario = [];

    foreach($this->funcionarios_info->funcionarios as $valor) {
      if(array_key_exists($valor->sobrenome, $arraySobrenomes)) {
        $arraySobrenomes[$valor->sobrenome]++;
      } else if(!array_key_exists($valor->sobrenome, $arraySobrenomes)) {
        $arraySobrenomes[$valor->sobrenome] = 1;
      }
    }

    foreach($this->funcionarios_info->funcionarios as $valor) {
      if($arraySobrenomes[$valor->sobrenome] > 1) {
        array_push($arrayFuncSobrenomesQtdMaior1, array("nome" => $valor->nome,
                                                    "sobrenome" => $valor->sobrenome,
                                                    "salario" => $valor->salario));
      }
    }

    foreach($arraySobrenomes as $index => $valor) {
      if($valor > 1) {
        array_push($arraySobrenomesQtdMaior1, $index);
      }
    }

    foreach($arraySobrenomesQtdMaior1 as $index => $valor) {
      foreach($arrayFuncSobrenomesQtdMaior1 as $index2A => $valor2A) {
        if($valor == $valor2A['sobrenome']) {
          if(!isset($arrayFuncSobrenomeMaiorSalario[$index])) {
            $arrayFuncSobrenomeMaiorSalario[$index] = array("sobrenome" => $valor2A['sobrenome'], "maiorSalario" => $valor2A['salario']);
          } else if ($arrayFuncSobrenomeMaiorSalario[$index]["maiorSalario"] < $valor2A['salario']) {
            $arrayFuncSobrenomeMaiorSalario = [];
            $arrayFuncSobrenomeMaiorSalario[$index] = array("sobrenome" => $valor2A['sobrenome'], "maiorSalario" => $valor2A['salario']);
          }
        }
      }
    }

    foreach($arrayFuncSobrenomesQtdMaior1 as $valor) {
      foreach($arrayFuncSobrenomeMaiorSalario as $valor2A) {
        if($valor['sobrenome'] == $valor2A['sobrenome'] && $valor['salario'] == $valor2A['maiorSalario']) {
          echo "last_name_max|$valor[sobrenome]|$valor[nome] $valor[sobrenome]|$valor[salario]<br>";
        }
      }
    }
  }
}

$funcionarios = new Funcionarios;
$funcionarios->MaioresSalarios();
$funcionarios->MenoresSalarios();
$funcionarios->MediaSalarios();
$funcionarios->mostrarDadosPorArea();
$funcionarios->maioresSalariosPorMesmoSobrenome();