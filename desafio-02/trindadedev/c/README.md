# Números primos
Números primos entre 1 e 10000.

# Como funciona?
Esse programa executa um loop começando em 2 até `max`, que no caso, é 10000.
Dentro desse loop, o programa testa os possíveis divisores do `num` (número atual do loop) exceto os divisores 0, 1.
Se o número for divisível por esses números, então ele não é primo, pois números só são divisíveis por 1 e por ele mesmo.

## Porque não começar com 0?
Bem, já sabemos que 0 e 1 não são primos, pois:
0 : Tem muitos divisores (infitos) .
1 : só tem 1 dividor, que no caso, é ele mesmo.

# Como executar?

Para compilar você pode usar algum compilador de C, como GCC (GNU Compiler Collection) do GNU, ou então CLang do LLVM.
No código abaixo mostro como você pode compilar usamdo GCC.

```bash
gcc main.c -o primes
chmod +x primes
./primes
```

## Programa escrito por Aquiles Trindade [trindadedev](https://github.com/trindadedev13)