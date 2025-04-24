# Numeros palindromos
Resolução do desafio de palindromos usando C++.

## Configure o mingw
Após instalar o MinGW, adicione o local de instalação no `Path` das suas variaveis de ambiente
```bash
C:\mingw64\bin
```

Faça o teste, abra o terminal e digite os comandos, individualmente
```bash
g++ --version
```

```bash
mingw32-make --version
```

Se os dois montrarem a versão do g++ e do MinGW, pode prosseguir.


## Build
Crie o diretorio `build`
```bash
mkdir build
```

Entre no diretorio
```bash
cd build
```

Configure os arquivos de build
```bash
cmake .. -G "MinGW Makefiles"
```

Gere o executavel
```bash
mingw32-make
```