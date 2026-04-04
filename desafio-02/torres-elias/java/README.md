# Desafio 02 - Listando Números Primos

## Descrição
Um programa que lista todos os números primos entre 1 e 10000.

## Solução
A abordagem consiste em iterar somente sobre os números ímpares a partir de 3 (visto que o 2 é tratado separadamente e se trata do único primo par) verificando para cada candidato se ele possui algum divisor entre 3 e sua raiz quadrada. Caso nenhum divisor seja encontrado, o número é primo.

### Por que testar apenas até a raiz quadrada?

Se um número é composto, ele pode ser escrito como:

$$n = a \cdot b$$

A raiz quadrada $\sqrt{n}$ funciona como um limiar.
Se você multiplicar:

$$\sqrt{n} \cdot \sqrt{n} = n$$

Se ambos $a$ e $b$ forem maiores que $\sqrt{n}$, evidentemente o resultado vai passar de $n$. Sendo assim, se um dos valores ($a$ ou $b$) for maior que $\sqrt{n}$, o outro obrigatoriamente terá que ser menor que $\sqrt{n}$.

**Portanto, se você testar todos os números até a raiz e nenhum funcionar, não há possibilidade dos valores acima funcionarem.**


**OBS:** nos casos de quadrado perfeito, a própria raiz é um divisor.

## Como executar
```bash
javac ListaPrimos.java
java ListaPrimos
```
Testado com Java 21.
