#ifndef FOO_H_
#define FOO_H_

#include <stdio.h>
#include <stdlib.h>
#include <json-c/json.h>
#include <float.h>
#include <string.h>
#include <limits.h>

typedef struct str_list {
  struct str_list *head;
  struct str_list *current;
  struct str_list *prox;
  char surname[50];
} Str_list;

Str_list *str_list_create() {
  Str_list *p = (Str_list *)malloc(sizeof(Str_list));

  if ( p == NULL ) {
    fprintf(stderr, "Error Alocate Memory\n");
    exit(1);
  }

  p->prox = NULL;
  p->head= NULL;
  p->current = NULL;

  return p;
}

void str_list_push(Str_list *list,const char *str) {
  if( list->head == NULL) {
    strcpy(list->surname, str);
    list->head = list;
    list->prox = NULL;
    list->current = list;
  } else {
    if(1) {
      Str_list *p = (Str_list *)malloc(sizeof(Str_list));
      if ( p == NULL ) {
        fprintf(stderr, "Error Alocate Memory\n");
        exit(1);
      }
      strcpy(p->surname,str);
      p->prox = NULL;
      list->current->prox = p;
      list->current = p;
    }
  }
}

int str_list_search(Str_list *list,const char *str) {
  Str_list *aux = list->head;

  while( aux != NULL) {
    if(strcmp(aux->surname, str) == 0) {
      return 1;
    }
    aux = aux->prox;
  }
  return 0;
}

void str_list_free(Str_list *list) {
  Str_list *head = list->head;
  Str_list *tmp;

  while(head != NULL) {
    tmp = head;
    head = head->prox;
    free(tmp);
  }
}


void print_last_name(json_object *j_funcionarios) {
  unsigned int i;

  unsigned int funcionarios_length;
  funcionarios_length = json_object_array_length(j_funcionarios);

  struct json_object *j_funcionario;
  struct json_object *j_salario;

  struct json_object *j_max_salary;
  struct json_object *j_min_salary;

  j_max_salary = json_object_new_array();
  j_min_salary = json_object_new_array();

  float currentSalary;
  float MaxSalary = 0;
  float MinSalary = FLT_MAX;

  for ( i = 0; i < funcionarios_length; i++ ) {
    j_funcionario = json_object_array_get_idx(j_funcionarios, i);
    json_object_object_get_ex(j_funcionario, "salario", &j_salario);
    currentSalary = json_object_get_double(j_salario);


    if( currentSalary > MaxSalary ) {
      j_max_salary = json_object_new_array();
      json_object_array_add(j_max_salary, j_funcionario);
      MaxSalary = currentSalary;
    } else if( currentSalary == MaxSalary) {
      json_object_array_add(j_max_salary, j_funcionario);
    }
    if( currentSalary < MinSalary) {
      MinSalary = currentSalary;
      j_min_salary = json_object_new_array();
      json_object_array_add(j_min_salary, j_funcionario);
    } else if( currentSalary == MinSalary) {
      json_object_array_add(j_min_salary, j_funcionario);
    }
  }

  // effetive print
  struct json_object *j_name;
  struct json_object *j_surname;
  struct json_object *j_salary;

  for ( i = 0; i < json_object_array_length(j_max_salary); i++) {
    j_funcionario = json_object_array_get_idx(j_max_salary, i);
    json_object_object_get_ex(j_funcionario, "nome", &j_name);
    json_object_object_get_ex(j_funcionario, "sobrenome", &j_surname);
    json_object_object_get_ex(j_funcionario, "salario", &j_salary);

      printf("last_name_max|%s|%s %s|%.2f\n",
        json_object_get_string(j_surname),
        json_object_get_string(j_name),
        json_object_get_string(j_surname),
        json_object_get_double(j_salary));
  }
}

void employeers(struct json_object *j_funcionarios,struct json_object *j_areas) {

  unsigned int areas_length = json_object_array_length(j_areas);

  unsigned int funcionarios_length = json_object_array_length(j_funcionarios);

  struct json_object *j_area_most_employeers;
  struct json_object *j_area_min_employeers;
  struct json_object *j_current_list = json_object_new_array();
  struct json_object *j_area;
  struct json_object *j_area_code;
  struct json_object *j_funcionario;
  struct json_object *j_funcionario_code;

  unsigned int i;
  unsigned int j;

  unsigned int max = 0;
  unsigned int min = UINT_MAX;

  for ( i = 0; i < areas_length; i++) {
    j_area = json_object_array_get_idx(j_areas, i);
    json_object_object_get_ex(j_area, "codigo", &j_area_code);
    for( j = 0; j < funcionarios_length; j++) {
      j_funcionario = json_object_array_get_idx(j_funcionarios, j);
      json_object_object_get_ex(j_funcionario, "area", &j_funcionario_code);

      if(strcmp(json_object_get_string(j_funcionario_code),
        json_object_get_string(j_area_code)) == 0) {
        json_object_array_add(j_current_list, j_funcionario);
      }
    }

    if( max < json_object_array_length(j_current_list)) {
      j_area_most_employeers = json_object_array_get_idx(j_areas, i);
      max = json_object_array_length(j_current_list);
    } else if ( min > json_object_array_length(j_current_list)) {
      j_area_min_employeers = json_object_array_get_idx(j_areas, i);
      min = json_object_array_length(j_current_list);
    }
    j_current_list = json_object_new_array();
  }

  struct json_object *j_area_name;
  json_object_object_get_ex(j_area_most_employeers,"nome", &j_area_name);
  printf("most_employers|%s|%d\n",json_object_get_string(j_area_name), max);
  json_object_object_get_ex(j_area_min_employeers,"nome", &j_area_name);
  printf("least_employees|%s|%d\n",json_object_get_string(j_area_name), min);


}

void print(json_object *j_funcionarios, const char *escopo, const char *area) {
  unsigned int i;

  unsigned int funcionarios_length;
  funcionarios_length = json_object_array_length(j_funcionarios);

  struct json_object *j_funcionario;
  struct json_object *j_salario;

  struct json_object *j_max_salary;
  struct json_object *j_min_salary;

  j_max_salary = json_object_new_array();
  j_min_salary = json_object_new_array();

  float currentSalary;
  float MaxSalary = 0;
  float MinSalary = FLT_MAX;
  float SumSalary = 0;

  for ( i = 0; i < funcionarios_length; i++ ) {
    j_funcionario = json_object_array_get_idx(j_funcionarios, i);
    json_object_object_get_ex(j_funcionario, "salario", &j_salario);
    currentSalary = json_object_get_double(j_salario);

    SumSalary += currentSalary;

    if( currentSalary > MaxSalary ) {
      j_max_salary = json_object_new_array();
      json_object_array_add(j_max_salary, j_funcionario);
      MaxSalary = currentSalary;
    } else if( currentSalary == MaxSalary) {
      json_object_array_add(j_max_salary, j_funcionario);
    }
    if( currentSalary < MinSalary) {
      MinSalary = currentSalary;
      j_min_salary = json_object_new_array();
      json_object_array_add(j_min_salary, j_funcionario);
    } else if( currentSalary == MinSalary) {
      json_object_array_add(j_min_salary, j_funcionario);
    }
  }

  // effetive print
  struct json_object *j_name;
  struct json_object *j_surname;
  struct json_object *j_salary;

  for ( i = 0; i < json_object_array_length(j_max_salary); i++) {
    j_funcionario = json_object_array_get_idx(j_max_salary, i);
    json_object_object_get_ex(j_funcionario, "nome", &j_name);
    json_object_object_get_ex(j_funcionario, "sobrenome", &j_surname);
    json_object_object_get_ex(j_funcionario, "salario", &j_salary);

      printf("%s_max|%s%s %s|%.2f\n",escopo, area, json_object_get_string(j_name),
        json_object_get_string(j_surname), json_object_get_double(j_salary));
  }

  for ( i = 0; i < json_object_array_length(j_min_salary); i++) {
    j_funcionario = json_object_array_get_idx(j_min_salary, i);
    json_object_object_get_ex(j_funcionario, "nome", &j_name);
    json_object_object_get_ex(j_funcionario, "sobrenome", &j_surname);
    json_object_object_get_ex(j_funcionario, "salario", &j_salary);

    printf("%s_min|%s%s %s|%.2f\n",escopo, area, json_object_get_string(j_name),
        json_object_get_string(j_surname), json_object_get_double(j_salary));
  }
  printf("%s_avg|%s%.2f\n",escopo, area, SumSalary / (float) funcionarios_length);
}


void area_print(json_object *j_funcionarios, json_object *j_areas) {

  unsigned int funcionarios_length = json_object_array_length(j_funcionarios);

  unsigned int areas_length = json_object_array_length(j_areas);


  struct json_object *j_array_funci = json_object_new_array();

  struct json_object *j_current_funcionario;
  struct json_object *j_funcionario;
  struct json_object *j_area;
  struct json_object *j_area_code;
  struct json_object *j_funcionario_code;
  struct json_object *j_current_funcionario_code;
  struct json_object *j_area_name;

  unsigned int i;
  unsigned int j;
  unsigned int k = 0;

  char nameArea[100];

  Str_list *list = str_list_create();
  // Essa parte é muito ruim por que é imprimido pela ordem de area de
  // funcionarios no json e não pela ordem de areas no json isso deixa
  // muito lerdo. Mais é requisito

  for( i = 0; i < funcionarios_length; i++) {
    j_funcionario = json_object_array_get_idx(j_funcionarios, i);
    json_object_object_get_ex(j_funcionario,"area", &j_funcionario_code);

    if(str_list_search(list, json_object_get_string(j_funcionario_code)) == 0) {

      str_list_push(list, json_object_get_string(j_funcionario_code));

      for(j = 0; j < funcionarios_length; j++) {
        j_current_funcionario = json_object_array_get_idx(j_funcionarios, j);
        json_object_object_get_ex(j_current_funcionario,"area", &j_current_funcionario_code);

        if(strcmp(json_object_get_string(j_current_funcionario_code),
            json_object_get_string(j_funcionario_code)) == 0) {

            json_object_array_add(j_array_funci, j_current_funcionario);

        }
      }
      for(k = 0 ; k < areas_length; k++) {
        j_area = json_object_array_get_idx(j_areas, k);
        json_object_object_get_ex(j_area, "codigo", &j_area_code);

        if(strcmp(json_object_get_string(j_funcionario_code),
              json_object_get_string(j_area_code)) == 0) {

          json_object_object_get_ex(j_area, "nome", &j_area_name);
          strcpy(nameArea, json_object_get_string(j_area_name));
          strcat(nameArea, "|");

          print(j_array_funci,"area", nameArea);

          j_array_funci = json_object_new_array();
          break;
        }
      }
    }
  }
  str_list_free(list);
}

#endif
