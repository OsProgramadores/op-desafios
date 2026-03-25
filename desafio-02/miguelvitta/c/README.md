# Gerador de Números Primos

Este projeto contém um programa em C que gera e imprime todos os números primos menores que 10.000. Ele utiliza a função `sqrt` da biblioteca `<math.h>`, então é necessário ter o compilador GCC instalado para compilar e executar o código.

## Pré-requisitos

Certifique-se de ter o GCC instalado no seu sistema. Você pode verificar isso executando o comando:
```
gcc --version
```

Se o GCC não estiver instalado, você pode instalá-lo com os seguintes comandos:

- **Ubuntu/Debian**:
  ```
  sudo apt update
  sudo apt install build-essential
  ```

- **Fedora**:
  ```
  sudo dnf install gcc
  ```

- **Arch Linux**:
  ```
  sudo pacman -S gcc
  ```

Além disso, o código usa a biblioteca matemática (`math.h`), então o GCC precisa do argumento `-lm` para fazer o link com essa biblioteca.

## Compilação e Execução

O projeto inclui um Makefile que simplifica o processo de compilação. Siga os passos abaixo:

1. Para compilar o programa, execute o comando:
   ```
   make
   ```

   Isso gerará um executável chamado `primos`.

2. Para executar o programa e ver os números primos gerados, use:
   ```
   ./primos
   ```

3. Para limpar os arquivos compilados (remover o executável e quaisquer arquivos objetos gerados), você pode executar:
   ```
   make clean
   ```
