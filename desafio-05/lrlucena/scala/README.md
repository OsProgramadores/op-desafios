# Instalação de Scala 2.12+

A maneira mais simples de instalar Scala no Linux é usando o SDKMAN (https://sdkman.io)

````terminal
$ curl -s "https://get.sdkman.io" | bash
$ source "$HOME/.sdkman/bin/sdkman-init.sh"
````

# Execução

````terminal
$ export lang="C.UTF-8"
$ scalac desafio05.scala -d desafio05.jar
$ scala desafio05.jar Funcionarios-10K.json | sort
````
