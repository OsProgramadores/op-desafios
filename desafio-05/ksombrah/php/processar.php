<?php
/**
 *
 * Resolução de um desafio proposto pelo site OsProgramadores.com feito
 * em PHP estruturado.
 * @author  Alcione Ferreira <sombra@alcionesytes.net>
 *
 * @since 1.0
 * @version 1.0.0
 * @copyright 2009-2021 AlcioneSytes.Net
 * @license GPL
 * @license http://www.gnu.org/licenses/licenses.html#GPL GNU General Public License
 * @link https://osprogramadores.com/desafios/d05/ Desafio #5
 *
 */
ini_set('error_reporting',0);
ini_set('memory_limit',-1);
ini_set('zend.enable_gc',0);
set_time_limit(0);
if ($argc >= 2)
  {
  $arq = $argv[1];
  if (file_exists($arq))
    {
    $response=file_get_contents($arq);
    $response=str_replace('},]',"}]",$response);
    $data=json_decode($response);
    /* Global Max e Min - Quem recebe mais */
    $max=0.0;
    $min=9999999.9;
    $avg=0.0;
    $qtd=count($data->funcionarios);
    foreach($data->funcionarios as $funcionario)
      {
      if ($funcionario->salario > $max)
        {
        $max=$funcionario->salario;
        }
      if ($funcionario->salario < $min)
        {
        $min=$funcionario->salario;
        }
      $avg+=$funcionario->salario;
      }
    $avg=$avg/$qtd;
    /* Buscando Max e Min */
    $q_max="";
    $q_min="";
    $q_last="";
    $imax=$imin=false;
    foreach($data->funcionarios as $funcionario)
      {
      if ($funcionario->salario == $max)
        {
        if ($imax)
          {
          $q_max.="\n";
          $q_last.="\n";
          }
        $q_max.="global_max|".$funcionario->nome." ".$funcionario->sobrenome."|".number_format($funcionario->salario,2,'.','');
        $q_last.="last_name_max|".$funcionario->sobrenome."|".$funcionario->nome." ".$funcionario->sobrenome."|".number_format($funcionario->salario,2,'.','');
        $imax=true;
        }
      if ($funcionario->salario == $min)
        {
        if ($imin)
          {
          $q_min.="\n";
          }
        $q_min.="global_min|".$funcionario->nome." ".$funcionario->sobrenome."|".number_format($funcionario->salario,2,'.','');
        $imin=true;
        }
      }
      echo ('
'.$q_max.'
'.$q_min.'
global_avg|'.number_format($avg,2,'.',''));
    /*Varetura por área*/
    $qtd_z=false;
    $most=0;
    $least=99999;
    $ia=0;
    foreach($data->areas as $area)
      {
      $max_a=0.0;
      $min_a=9999999.9;
      $avg_a=0.0;
      $qtd_a=0;
      $q_max_a="";
      $q_min_a="";
      $q_avg_a="";
      foreach($data->funcionarios as $funcionario)
        {
        if (strcmp($funcionario->area,$area->codigo) == 0)
          {
          if ($funcionario->salario > $max_a)
            {
            $max_a=$funcionario->salario;
            }
          if ($funcionario->salario < $min_a)
            {
            $min_a=$funcionario->salario;
            }
          $avg_a+=$funcionario->salario;
          $qtd_a++;
          }
        }
      $areaq[$ia]['nome']=$area->nome;
      $areaq[$ia]['qtd']=$qtd_a;
      if ($qtd_a > $most)
        {
        $most=$qtd_a;
        $q_most="most_employees|".$area->nome."|".$qtd_a;
        }
      if ($qtd_a < $least)
        {
        $least=$qtd_a;
        $q_least="least_employees|".$area->nome."|".$qtd_a;
        }
      if ($qtd_a == 0)
        {
        $avg_a=0;
        if ($qtd_z)
          {
          $q_least.="\nleast_employees|".$area->nome."|".$qtd_a;
          }
        $qtd_z=true;
        }
      else
        {
        $avg_a=$avg_a/$qtd_a;
        $imax=$imin=false;
        foreach($data->funcionarios as $funcionario)
          {
          if (strcmp($funcionario->area,$area->codigo) == 0)
            {
            if ($funcionario->salario == $max_a)
              {
              if ($imax)
                {
                $q_max_a.="\n";
                }
              $q_max_a.="area_max|".$area->nome."|".$funcionario->nome." ".$funcionario->sobrenome."|".number_format($funcionario->salario,2,'.','');
              $imax=true;
              }
            if ($funcionario->salario == $min_a)
              {
              if ($imin)
                {
                $q_min_a.="\n";
                }
              $q_min_a .= "area_min|".$area->nome."|".$funcionario->nome." ".$funcionario->sobrenome."|".number_format($funcionario->salario,2,'.','');
              $imin=true;
              }
            }
          }
        }
      $q_avg_a="area_avg|".$area->nome."|".number_format($avg_a,2,'.','');
      $ia++;
      echo ('
'.$q_max_a.'
'.$q_min_a.'
'.$q_avg_a);
      }
    if ($most > 0)
      {
      $q = 0;
      foreach($areaq as $am)
        {
        if ($am['qtd'] == $most)
          {
          $q++;
          }
        if ($q > 1)
          {
          $q_most.="\nmost_employees|".$am['nome']."|".$am['qtd'];
          }
        }
      }
    if ($least > 0)
      {
      $q=0;
      foreach($areaq as $am)
        {
        if ($am['qtd'] == $least)
          {
          $q++;
          }
        if ($q > 1)
          {
          $q_leat.="\nleast_employees|".$am['nome']."|".$am['qtd'];
          }
        }
      }

    echo ('
'.$q_most.'
'.$q_least.'
'.$q_last.'
    ');
    }
  }
else
  {
  echo ("Usage: php processar.php <arquivo.json>\n");
  }
?>