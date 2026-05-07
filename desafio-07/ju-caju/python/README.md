# Desafio 07

## Informações sobre a implementação

Esta solução implementa um comportamento parecido com o comando `tac`.

O arquivo é aberto em modo binário e lido de trás para frente em blocos, sem carregar tudo de uma vez na memória.

Cada linha é então impressa na ordem inversa da original, o que permite lidar melhor com arquivos grandes.

## Como rodar o exercício

Entre na pasta da solução:

```bash
cd desafio-07/ju-caju/python
```

Execute o programa informando o arquivo de entrada:

```bash
python3 resposta.py arquivo.txt
```

## Como instalar o Python

Se o Python 3 já estiver instalado, você pode confirmar com:

```bash
python3 --version
```

Se não estiver instalado, no Ubuntu ou Debian rode:

```bash
sudo apt update
sudo apt install python3
```
