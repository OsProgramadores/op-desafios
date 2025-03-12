# Palíndromo

Este projeto contém um programa em C que lê dois números inteiros positivos de até 64 bits e imprime todos os números palíndromos entre os dois, ambos inclusos.

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

## Compilação e Execução

O projeto inclui um Makefile que simplifica o processo de compilação. Siga os passos abaixo:

1. Para compilar o programa, execute o comando:
   ```
   make
   ```

   Isso gerará um executável chamado `desafio-03`.

2. Para executar o programa, use:
   ```
   ./desafio-03
   ```

3. Para limpar os arquivos compilados (remover o executável e quaisquer arquivos objetos gerados), você pode executar:
   ```
   make clean
   ```
