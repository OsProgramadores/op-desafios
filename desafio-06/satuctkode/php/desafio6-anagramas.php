<?php
class Anagramas {
  public function mostrarAnagramas($arquivoRecebido, $expressaoRecebida) {
    define("EXPRESSAO_UPPER_NOSPACE", strtoupper(preg_replace("/\s+/", "", $expressaoRecebida)));

    if(preg_match("/^[a-z]{1,16}$/i", EXPRESSAO_UPPER_NOSPACE, $match)) {
      $grupoTodasExpressoes = [];
      $grupoExpressoesEscolhidas = [];
      $arquivoDados = fopen($arquivoRecebido, 'r') or die("Erro ao abrir arquivo!");
      while(!feof($arquivoDados)) {
        array_push($grupoTodasExpressoes, fgets($arquivoDados));
      }
      fclose($arquivoDados);

      foreach($grupoTodasExpressoes as $expressaoOriginal) {
        if(count(str_split(preg_replace("/\s+/", "", $expressaoOriginal))) === count(str_split(EXPRESSAO_UPPER_NOSPACE))) {
          array_push($grupoExpressoesEscolhidas, $expressaoOriginal);
        }
      }

      define("ARRAY_EXPRESSAO_UPPER_NOSPACE_LET_SEP", str_split(preg_replace("/\s+/", "", EXPRESSAO_UPPER_NOSPACE)));

      foreach($grupoExpressoesEscolhidas as $expressaoArray) {
        $arrayExpUpNSLetSepTemporario = ARRAY_EXPRESSAO_UPPER_NOSPACE_LET_SEP;
        $arrayExpressaoArrayLetSep = str_split(preg_replace("/\s+/", "", $expressaoArray));

        foreach($arrayExpressaoArrayLetSep as $letraExpArray) {
          foreach($arrayExpUpNSLetSepTemporario as $indexExpUpNSTemp => $letraExpUpNSTemp) {
            if($letraExpArray === $letraExpUpNSTemp) {
              unset($arrayExpUpNSLetSepTemporario[$indexExpUpNSTemp]);
              break;
            }
          }
        }
  
        if(empty($arrayExpUpNSLetSepTemporario)) {
          echo $expressaoArray."<br>";
        }
      }

    } else {
      die("Error, a expressão precisa ter no máximo 16 caracteres e não pode ter caracteres especiais, exceto espaços!");
    }
  }
}

$anagramas = new Anagramas;
$anagramas->mostrarAnagramas("words.txt", "ogd");