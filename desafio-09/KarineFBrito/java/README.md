## Lógica do Código
- Ele determina valores fixos na classe como os dígitos, base máxima, base mínima e o limite
- O código recebe o arquivo por linha de comando. Verifica se foi passado um caminho e se ele existe.
- Depois, em cada linha, ele faz o processo de:
    - separar a linha em partes para determinar base entrada, base saída e o número;
    - Faz as verificações(se as bases estão no limite, não possuir números negativos e nem acima do limite determinado) se uma dessas condições for verdadeira imprime a mensagem "???";
    - Logo após realiza a conversão da base entrada para a base decimal (Dessa maneira fica mais fácil converter para outras bases);
    - Depois desses passos o código converte a base decimal para a base saída e em seguida imprime o resultado.

## Versão que usei:
- Java 21 (JDK 21).

## Como executar o código
  - Para compilar o código execute o comando abaixo:

  ```
  javac BigBase.java
  ```
  - Para executar o código, utilize o seguinte comando:
```
java BigBase <caminho-absoluto>
```
