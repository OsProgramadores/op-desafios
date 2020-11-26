# Potigol

## Instalação

 - Instale Java 8+ (java.com)
 - Baixe a versão mais nova de Potigol do site https://potigol.github.io e siga as [instuções de instalação](https://github.com/potigol/potigol#instala%C3%A7%C3%A3o).

## Execução

````terminal
$ echo verdade | potigol anagram.poti
AD VERDE
ADD VEER
DAD VEER
DADE REV
DAVE RED
DEAD REV
RED VADE
RED VEDA
````

> O pior caso até agora é para a entrada "maryhadalittleox".

````terminal
$ time echo maryhadalittleox | potigol anagram.poti > maryhadalittleox.txt

real    0m48.343s
user    0m53.547s
sys     0m8.234s
````
