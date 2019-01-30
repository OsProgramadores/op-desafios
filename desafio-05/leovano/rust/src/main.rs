extern crate desafio_05;

use std::env;
use std::fs;

fn main() {
    let json = env::args().nth(2).expect("Arg1");
    let cpus = env::args()
        .nth(1)
        .expect("Arg2")
        .parse::<u32>()
        .expect("Arg2Fail");
    let json = fs::read(json).expect("ReadFail");
    let eprse = desafio_05::get_stats(&json, cpus).expect("ParseFail");

    let stats = eprse.stats;
    let areas = eprse.areas;

    let global = stats.global;
    let by_area = stats.by_area;
    let by_employees = stats.by_employees;
    let by_lastname = stats.by_lastname;

    // Global
    for f in &global.list_max {
        println!("global_max|{}|{}", f.nome(), f.salario);
    }

    for f in &global.list_min {
        println!("global_min|{}|{}", f.nome(), f.salario);
    }

    println!("global_avg|{}", global.average());

    // Por Área
    for (c, s) in by_area.iter() {
        let cn = &areas[c];

        for f in &s.list_max {
            println!("area_max|{}|{}|{}", cn, f.nome(), f.salario);
        }

        for f in &s.list_min {
            println!("area_min|{}|{}|{}", cn, f.nome(), f.salario);
        }

        println!("area_avg|{}|{}", cn, s.average());
    }

    // Por Empregados
    let (e_min, e_max) = by_employees.minmax();

    for a in &e_max.0 {
        let an = &areas[a];
        println!("most_employees|{}|{}", an, e_max.1);
    }

    for a in &e_min.0 {
        let an = &areas[a];
        println!("least_employees|{}|{}", an, e_min.1);
    }

    // Por Sobrenome
    for (ln, s, fs) in by_lastname.into_iter() {
        for f in fs {
            println!("last_name_max|{}|{}|{}", ln, f.nome(), s);
        }
    }
}
