#### Compilação:

Execute o seguinte comando dentro da pasta maykon-oliveira.

```
javac -cp .;lib\gson-2.8.2.jar -d bin Main.java
```

#### Execução:

Na pasta bin execute o seguinte comando.

```
cd bin
java -cp .;..\lib\gson-2.8.2.jar Main
```

##### Ps.

O caminho para um arquivo json diferente pode ser passado como parâmetro.

`java -cp .;..\lib\gson-2.8.2.jar Main 'CAMINHO'`