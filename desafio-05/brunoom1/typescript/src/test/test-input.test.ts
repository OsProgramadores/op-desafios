import { read_input_file_name } from "./../helper";

test("Testar se o input filename está trazedo o esperado", () => {
  const file_name_mock = "arquivo-teste.pdf";

  process.argv.push(file_name_mock);
  const filename: string = read_input_file_name();

  expect(filename).toEqual(file_name_mock)
});