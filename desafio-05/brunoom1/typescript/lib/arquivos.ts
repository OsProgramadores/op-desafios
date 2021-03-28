import { readFileSync, statSync } from "fs";

import {
  FuncionariosDB
} from "./interfaces";

export const lerArquivoFuncionarios = (filename: string): FuncionariosDB => {
  const statsResult = statSync(filename);

  if (statsResult.isFile) {
    const result = readFileSync(filename).toString();
    const database = JSON.parse(result) as FuncionariosDB;
    return database;
  } else {
    throw new Error("File is not found");
  }
}
