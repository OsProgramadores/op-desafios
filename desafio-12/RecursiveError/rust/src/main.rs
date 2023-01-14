/* 
Autor: Guilherme Silva Schultz (RecursiveError)
Data: 14-01-2023
Explicação, o desafio consiste em varificar se o numero é uma potencia de 2, esse processo usa calculos matematicos com log para resolver.
porem por ser uma base de 2 podemos simplificar usando binario, binario é uma notação numerica de base 2, numeros são formados pela soma de potencias de 2
ex: 
0b0001 = 2^0 = 1
0b0010 = 2^1 = 2
0b0011 = 2^1 + 2^0 = 3
0b0100 = 2^2 = 4

como podemos ver, quando um numero pertence a potencia 2, só existe um "1" em toda cadeia de bits, então podemos usar operações de bitwise para resolver o desafio
usando a operação XOR e bitshifts podemos verificar facilmente

primeiro criamos um bitmask usando bitshift a cada operação
ex:
1<<0 = 0b0001
1<<1 = 0b0010
1<<2 = 0b0100

depois usamos esse bitmask para realizar uma operação XOR no numero, se ele for uma potencia de 2 o resultado vai ser 0
ex
4 = 2^2 = 0b0100 XOR 0b0100 = 0b000 = 0
8 = 2^3 = 0b1000 XOR 0b1000 = 0b000 = 0 
10 = 0b1010 XOR 0b1000 = 0b0010 = 2
*/

use std::{fs::File, io::{BufReader, BufRead}};

//modulo para trabalhar com numeros maiores que 2^128-1
use num::{BigUint, Zero, One};



fn check_pow(num: BigUint)-> (bool, u64) {
    let mut bitmask: BigUint = BigUint::one();
    let mut shift = 0u64;
    
    //Diferente de um numero da std de Rust, BigUint não implementa Copy, por isso o uso do clone()
    loop {
        //se bitmask for maior que num, significa que o shift ja passou do valor, logo não é uma potencia de 2
        if bitmask.clone() > num.clone(){
            return (false, 0);
        }

        //faz uma operação XOR e se o resultado for 0 significa que é uma potencia de 2
        if  bitmask.clone() ^ num.clone() == BigUint::zero() {
            return (true, shift);
        }
        bitmask <<= 1; // shift bitmask em 1
        shift += 1;       
    }
}

fn main() {
    let arquivo = "d12.txt";

    //abre o arquivo
    //File em Rust não le linha por linha, logos temos q usar Bufreader para isso 
    let file_nums = File::open(arquivo).expect(&format!("Error ao abrir o arquivo {}", arquivo));
    let buffer = BufReader::new(file_nums);
    
    //tranforma as linhas em numeros
    let numbres: Vec<BigUint> = buffer.lines().map(|line|{
        let number: BigUint = line.unwrap().trim().parse().expect("arquivo invalido");
        number
    }).collect();

    for num in numbres{
        let (b, s) = check_pow(num.clone());
        if b{
            println!("{} true {}", num, s);
        }else {
            println!("{} false", num);
        }
    }
}
