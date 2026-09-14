# Desafio 09 - pedrobenicio2005

Converte numeros entre bases 2 e 62.

## Como executar

    python3 main.py < arquivo_de_entrada.txt

## Formato da entrada

Cada linha tem: base_entrada base_saida numero

Exemplo:

    10 16 1500
    36 10 GOODBYE

## Implementacao

- Escrito em Python 3.
- Nao usa funcoes nativas de conversao (int(s, base) ou format).
- Faz a conversao manualmente usando os 62 caracteres:
  0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
- Imprime ??? para: base invalida, numero negativo, numero grande demais
  ou digito invalido para a base.
