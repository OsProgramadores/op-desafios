import { read_input_file_name, openFile, mensure } from "./helper";

const filename = read_input_file_name();
openFile(filename).then(result => {
  mensure(result);
});
