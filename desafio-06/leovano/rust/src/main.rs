use std::fs::File;
use std::io::{BufReader, BufWriter, Write, stdout};
use std::path::PathBuf;
use std::process::ExitCode;
use std::{env, io};

use thiserror::Error;

use desafio_06::{Solver, SolverError};

#[derive(Error, Debug)]
pub enum AppError {
    #[error("Usage: anagram <phrase> [words_file]")]
    MissingArgument,

    #[error(transparent)]
    Solver(#[from] SolverError),

    #[error("Failed to read '{path}': {source}")]
    Io {
        path: PathBuf,

        #[source]
        source: std::io::Error,
    },
}

fn main() -> ExitCode {
    match run() {
        Ok(()) => ExitCode::SUCCESS,
        Err(err) => {
            eprintln!("{err}");
            ExitCode::FAILURE
        }
    }
}

fn run() -> Result<(), AppError> {
    let input = env::args().nth(1).ok_or(AppError::MissingArgument)?;
    let dict_path = env::args()
        .nth(2)
        .map(PathBuf::from)
        .unwrap_or_else(|| PathBuf::from("words.txt"));

    let file = File::open(&dict_path).map_err(|source| AppError::Io {
        path: dict_path.clone(),
        source,
    })?;

    let solver = Solver::new(BufReader::new(file), &input)?;
    let mut out = BufWriter::with_capacity(64 * 1024, stdout().lock());

    solver
        .for_each_solution(|words| -> Result<(), io::Error> {
            for (i, w) in words.iter().enumerate() {
                if i > 0 {
                    out.write_all(b" ")?;
                }
                out.write_all(w.as_bytes())?;
            }
            out.write_all(b"\n")?;
            Ok(())
        })
        .map_err(|source| AppError::Io {
            path: PathBuf::from("<stdout>"),
            source,
        })?;

    out.flush().map_err(|source| AppError::Io {
        path: PathBuf::from("<stdout>"),
        source,
    })?;

    Ok(())
}
