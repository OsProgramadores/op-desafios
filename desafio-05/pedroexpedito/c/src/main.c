#include <err.h>
#include <json-c/json.h>
#include <stdio.h>
#include <stdlib.h>
#include <float.h>
#include <string.h>

#define ERROR(i, msg)                                                          \
  fprintf(stderr, "%s\n", msg);                                                \
  exit(i)

#include "headers/foo.h"


unsigned int get_file_size(FILE *file) {
  fseek(file, 0, SEEK_END);
  unsigned int ret  = ftell(file);
  fseek(file, 0, SEEK_SET);
  return ret;
}


void last_name_max(struct json_object *j_funcionarios) {

  unsigned int funcionarios_length;
  funcionarios_length = json_object_array_length(j_funcionarios);

  struct json_object *j_all_surnames = json_object_new_array();
  struct json_object *j_surname;
  struct json_object *j_current_surname;

  struct json_object *j_funcionario;
  struct json_object *j_current_funcionario;

  unsigned int i;
  unsigned int j;

  Str_list *list = str_list_create();

  for( i = 0; i < funcionarios_length; i++) {
    j_funcionario = json_object_array_get_idx(j_funcionarios,i);
    json_object_object_get_ex(j_funcionario,"sobrenome",&j_surname);
    for( j = i+1; j < funcionarios_length; j++) {
      j_current_funcionario = json_object_array_get_idx(j_funcionarios,j);

      json_object_object_get_ex(j_current_funcionario,"sobrenome",&j_current_surname);

      if(strcmp(json_object_get_string(j_surname),json_object_get_string(
              j_current_surname)) == 0 &&
          str_list_search(list,
            json_object_get_string(j_current_surname)) == 0) {

        str_list_push(list,
            json_object_get_string(j_current_surname));
        json_object_array_add(j_all_surnames, j_funcionario);
      }
    }
    print_last_name(j_all_surnames);
    j_all_surnames = json_object_new_array();
  }
  str_list_free(list);
  // Preciso fazer uma forma de separar os  funcionarios por
  // sobrenome porém eu não sei quantos sobrenomes tem.
  // O problema é que eu preciso criar um array e verificar se
  // dentro deste array tenho que verificar se já existe o array
  // do sobrenome para adicionar os novos ou é inedito
  // Só falta verificar se o username já foi processado

}

int main(int argc, char **argv) {
  if (argc < 2) {
    ERROR(EXIT_FAILURE, "Passe o arquivo como argumento");
  }
  FILE *data;
  data = fopen(argv[1], "r");
  if (data == NULL) {
    ERROR(1, "File Not Found");
  }
  unsigned int bufferSize = get_file_size(data);
  char *buffer = malloc(bufferSize);
  fread(buffer, bufferSize, 1, data);
  fclose(data);

  struct json_object *parsed_json;
  struct json_object *j_funcionarios;
  struct json_object *j_areas;

  parsed_json = json_tokener_parse(buffer);

  json_object_object_get_ex(parsed_json, "funcionarios", &j_funcionarios);
  json_object_object_get_ex(parsed_json, "areas", &j_areas);


  print(j_funcionarios,"global","");
  area_print(j_funcionarios, j_areas);
  employeers(j_funcionarios, j_areas);
  last_name_max(j_funcionarios);
}

