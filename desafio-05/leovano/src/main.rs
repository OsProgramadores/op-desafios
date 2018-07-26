extern crate desafio_05;

use std::env;

fn main() {
    let json = env::args().nth(1).expect("NoArg");

    let mut j = String::new();
    let eprse = desafio_05::parse(&mut j, &json).expect("ParseFail");
    let stats = desafio_05::get_stats(&eprse);

    // Global
    for f in &stats.global.list_max {
        println!("global_max|{}|{}", f.nome(), f.salario);
    }

    for f in &stats.global.list_min {
        println!("global_min|{}|{}", f.nome(), f.salario);
    }

    println!("global_avg|{}", stats.global.average());

    // Por Área
    for (c, s) in stats.by_area.iter() {
        let cn = &eprse.areas[c];

        for f in &s.list_max {
            println!("area_max|{}|{}|{}", cn, f.nome(), f.salario);
        }

        for f in &s.list_min {
            println!("area_min|{}|{}|{}", cn, f.nome(), f.salario);
        }

        println!("area_avg|{}|{}", cn, s.average());
    }

    // Por Empregados
    let (e_min, e_max) = stats.by_employees.minmax();

    for a in &e_max.0 {
        let an = &eprse.areas[a];
        println!("most_employees|{}|{}", an, e_max.1);
    }

    for a in &e_min.0 {
        let an = &eprse.areas[a];
        println!("least_employees|{}|{}", an, e_min.1);
    }

    // Por Sobrenome
    for (ln, (s, fs)) in stats.by_lastname.into_iter() {
        for f in fs {
            println!("last_name_max|{}|{}|{}", ln, f.nome(), s);
        }
    }
}
