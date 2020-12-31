use memmap::Mmap;
use std::env;
use std::fs::File;

fn main() {
    let file = env::args().nth(2).expect("Arg1");
    let cpus = env::args()
        .nth(1)
        .expect("Arg2")
        .parse::<u32>()
        .expect("Arg2Fail");
    let file = File::open(file).expect("FileFail");
    let data = unsafe { Mmap::map(&file).expect("MapFail") };
    let eprse = desafio_05::get_stats(&data, cpus).expect("ParseFail");

    let stats = eprse.stats;
    let areas = eprse.areas;

    let global = stats.global;
    let by_area = stats.by_area;
    let by_employees = stats.by_employees;
    let by_lastname = stats.by_lastname;

    // Global
    for f in &global.list_max {
        println!("global_max|{}|{}", f.nome, global.max);
    }

    for f in &global.list_min {
        println!("global_min|{}|{}", f.nome, global.min);
    }

    println!("global_avg|{}", global.average());

    // Por Área
    for (code, astats) in by_area.iter() {
        let area = &areas[code];

        for f in &astats.list_max {
            println!("area_max|{}|{}|{}", area, f.nome, astats.max);
        }

        for f in &astats.list_min {
            println!("area_min|{}|{}|{}", area, f.nome, astats.min);
        }

        println!("area_avg|{}|{}", area, astats.average());
    }

    // Por Empregados
    let cstats = by_employees.minmax();

    for code in &cstats.list_max {
        let an = &areas[code];
        println!("most_employees|{}|{}", an, cstats.max);
    }

    for code in &cstats.list_min {
        let an = &areas[code];
        println!("least_employees|{}|{}", an, cstats.min);
    }

    // Por Sobrenome
    for mstats in by_lastname.into_iter() {
        for f in mstats.list {
            println!(
                "last_name_max|{}|{}|{}",
                mstats.surname, f.nome, mstats.salary
            );
        }
    }
}
