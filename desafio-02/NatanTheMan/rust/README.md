# Desafio 02 - Numeros Primos

O programa percorre todos os números de 1 a 10.000(dez mil), e escreve-os na tela caso ele seja um número primo.

# Explicação da lógica

A função recebe um númoro inteiro positivi. Utilizei u16 pois ele comporta valores até pouco mais de 60000, mais do que necessário para armazenar o número máximo que é 10000. A função verifica se o argumento passado é primo, caso seja retona true.

```
fn is_prime(num: u16) -> bool
```

Um número é primo quando ele é divisível apenas por 1 e por ele mesmo(x % 1 == 0 x % x == 0). Logo este dois valores serão removidos da amostragem do loop.

```
for j in 2..limit {
    if num % j == 0 {
        return false;
    }
}
```

Como o número só pode ser divisível por 1 e ele, caso o resta da divisão dele por outro número o invalida, e a função retorna false.

Aqui é calculada a raiz quadrada do número a ser analisado e ela é usada como limite do loop, por que se um número for divisível por qualquer número maior que sua raiz quadrada, ele também será divisível por todos os números menores que sua raiz quadrada.

```
let limit = f64::sqrt(num as f64) as u16 + 1;
for j in 2..limit {...}
```

# Compilar

```
rustc main.rs
```

# Rodar

```
./main
```

# Linguagem

Rust 1.90

# Autor

[Natan Costa](https://github.com/NatanTheMan)

# Aprenda mais sobre Rust

[The Rust Programming Language](https://doc.rust-lang.org/book/) - livro para aprender Rust

[Rust Playground](https://play.rust-lang.org/?version=stable&mode=debug&edition=2024) - editor online para Rust

[Rust By Example](https://doc.rust-lang.org/rust-by-example/) - colecao de exemplos executaveis que ilustrao bibliotecas padroes e conceitos da linguagem

[Documentacao para a bilbioteca padrao do Rust](https://doc.rust-lang.org/std/index.html)
