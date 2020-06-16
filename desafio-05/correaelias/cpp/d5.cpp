/*
Desafio 5 em C++ (C++11) por Elias Correa
Para compilar(gcc/mingw compiler):
g++ -std=c++11 -O3 d5.cpp -o d5
*/

#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <iomanip>
#include <thread>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

//Hashed string
struct HString{
  size_t hash, len;
  char *str;
};

inline bool operator == (const HString& a, const HString& b){
    return a.len == b.len && a.hash == b.hash &&
           ((a.len > 0 && a.str[0] == b.str[0] && a.str[a.len - 1] == b.str[b.len - 1]) || a.len == 0);
}

std::ostream& operator <<(std::ostream& os, const HString& hs){
  os.write(hs.str, hs.len);
  return os;
}

struct HStringHash{
  size_t operator () (const HString& hs) const{
    return hs.hash;
  }
};

struct Surname{
  int total_employees;
  int max_salary;
  std::vector<HString> max_names;
};

struct Area{
  HString name;
  int total_employees;
  long long int total_salary;
  int min_salary, max_salary;
  std::vector<HString> min_names, max_names;
};

struct ThreadData{
  char *buffer;
  int total_employees;
  long long int total_salary;
  int min_salary, max_salary;
  std::vector<HString> min_names, max_names;
  std::unordered_map<HString, Surname, HStringHash> surnames;
  std::unordered_map<HString, Area, HStringHash> areas;
};

inline void add_min_name(std::vector<HString>& list, int& list_salary, const HString& name, const HString& surname, int salary){
  if(list_salary == salary){
    list.push_back(name);
    list.push_back(surname);
  }
  else if(list_salary == 0 || salary < list_salary){
    list_salary = salary;
    list.clear();
    list.push_back(name);
    list.push_back(surname);
  }
}

inline void add_max_name(std::vector<HString>& list, int& list_salary, const HString& name, const HString& surname, int salary){
  if(list_salary == salary){
    list.push_back(name);
    list.push_back(surname);
  }
  else if(list_salary == 0 || salary > list_salary){
    list_salary = salary;
    list.clear();
    list.push_back(name);
    list.push_back(surname);
  }
}

inline void add_max_surname(std::vector<HString>& list, int& list_salary, const HString& name, int salary){
  if(list_salary == salary){
    list.push_back(name);
  }
  else if(list_salary == 0 || salary > list_salary){
    list_salary = salary;
    list.clear();
    list.push_back(name);
  }
}

inline void join_name_list(const std::vector<HString>& source_list, std::vector<HString>& dest_list, int source_salary, int& dest_salary, bool keep_min){
  if(source_salary == 0) return;
  if(source_salary == dest_salary){
    dest_list.insert(dest_list.end(), source_list.begin(), source_list.end());
  }else if(dest_salary == 0 ||
          (keep_min && source_salary < dest_salary) ||
          (!keep_min && source_salary > dest_salary)){
    dest_salary = source_salary;
    dest_list = source_list;
  }
}

inline char *get_string(char *c, HString& hs){
  while(*c != ':') ++c;
  while(*c != '"') ++c;
  ++c;
  char *start = c;
  while(*c != '"') ++c;
  hs = {0, static_cast<size_t>(c - start), start};
  return ++c;
}

inline char *get_string_hashed(char *c, HString& hs){
  while(*c != ':') ++c;
  while(*c != '"') ++c;
  ++c;
  char *start = c;
  //calc X31 hash while reading
  size_t h;
  for(h = 0; *c != '"'; ++c)
		h = (h << 5) - h + *c;
  hs = {h, static_cast<size_t>(c - start), start};
  return ++c;
}

inline char *get_number(char *c, int& num){
  while(*c != ':') ++c;
  ++c;
  while(*c == ' ') ++c;
  for(num = 0; *c != '.'; ++c)
    num = num * 10 + (*c - '0');
  num = num * 10 + (*++c - '0');
  num = num * 10 + (*++c - '0');
  return ++c;
}

void parse_json_chunk(ThreadData *data){
  char *c = data->buffer;
  int salary;
  HString name_str, surname_str, area_str;
  Area *area;
  Surname * surname;
  for(;;){
    while(*c && *c != '"') ++c;
    if(*c == 0)
      break;
    else
      ++c;
    switch(*c){
      case 'i': //employee (starts with i of id)
        //ignore id
        c += 2;
        while(*c != ',') ++c;
        
        //read name
        c += 7;
        c = get_string(c, name_str);
        
        //read surname
        c += 11;
        c = get_string_hashed(c, surname_str);
        
        //read salary
        c += 9;
        c = get_number(c, salary);
        
        //read area
        c += 6;
        c = get_string_hashed(c, area_str);
        
        //update global counters
        data->total_salary += salary;
        ++data->total_employees;
        add_min_name(data->min_names, data->min_salary, name_str, surname_str, salary);
        add_max_name(data->max_names, data->max_salary, name_str, surname_str, salary);
        
        //update area
        area = &data->areas[area_str];
        ++area->total_employees;
        area->total_salary += salary;
        add_min_name(area->min_names, area->min_salary, name_str, surname_str, salary);
        add_max_name(area->max_names, area->max_salary, name_str, surname_str, salary);
        
        //update surname
        surname = &data->surnames[surname_str];
        ++surname->total_employees;
        add_max_surname(surname->max_names, surname->max_salary, name_str, salary);
      break;
      case 'c': //area (starts with c of code)
        //get code
        c += 6;
        c = get_string_hashed(c, area_str);
        
        //get name
        c += 6;
        c = get_string(c, name_str);
        
        //set area name
        data->areas[area_str].name = name_str;
      break;
    }
  }
}

int main(int argc, char *argv[]) {  
  if(argc != 2 && argc != 3){
    std::cout << "Usage: d5 <file> [num_threads]";
    return 1;
  }
  
  FILE *file = fopen(argv[1], "rb");
  if(!file){
    std::cout << "Invalid file path.";
    return 1;
  }
  
  //get file size
  fseek(file, 0, SEEK_END);
  size_t file_size = ftell(file);
  rewind(file);
  
  int num_threads = argc == 3 ? atoi(argv[2]) : std::thread::hardware_concurrency();
  
  std::vector<ThreadData> data(num_threads);
  std::vector<std::thread> threads(num_threads);
  
  for(int i = 0; i < num_threads; ++i){
    //if its the last buffer, read the remains
    size_t buffer_size = (i == num_threads - 1) ? file_size - ftell(file) : ceil(file_size / num_threads);
    
    char *buffer = new char[buffer_size];
    
    size_t read_size = fread(buffer, 1, buffer_size, file);
    
    //read complete json objects only
    for(size_t j = read_size - 1; j > 0; --j){
      if(buffer[j] == '}'){
        buffer[j] = '\0';
        break;
      }
      fseek(file, -1, SEEK_CUR);
    }
    
    data[i].buffer = buffer;
    data[i].surnames.reserve(20000); //reserve good space to avoid slow map rebuild/realloc
    threads[i] = std::thread(parse_json_chunk, &data[i]);
  }
  
  fclose(file);
  
  for(auto& thread : threads){
    thread.join();
  }
  
  ThreadData& d = data[0];
  
  //join threads results
  
  for(auto it = data.begin() + 1; it != data.end(); ++it){
    //global
    d.total_employees += it->total_employees;
    d.total_salary += it->total_salary;
    join_name_list(it->min_names, d.min_names, it->min_salary, d.min_salary, true);
    join_name_list(it->max_names, d.max_names, it->max_salary, d.max_salary, false);
    
    //areas
    for(auto& pair : it->areas){
      Area& area1 = d.areas[pair.first];
      Area& area2 = pair.second;
      if(area2.name.len) area1.name = area2.name;
      area1.total_employees += area2.total_employees;
      area1.total_salary += area2.total_salary;
      join_name_list(area2.min_names, area1.min_names, area2.min_salary, area1.min_salary, true);
      join_name_list(area2.max_names, area1.max_names, area2.max_salary, area1.max_salary, false);
    }
    
    //surnames
    for(auto& pair : it->surnames){
      Surname& surname1 = d.surnames[pair.first];
      Surname& surname2 = pair.second;
      surname1.total_employees += surname2.total_employees;
      join_name_list(surname2.max_names, surname1.max_names, surname2.max_salary, surname1.max_salary, false);
    }
  }
  
  //write results
  
  //global
  
  for(auto it = d.min_names.begin(); it != d.min_names.end(); it += 2){
    std::cout << "global_min|" << *it << ' ' << *(it + 1) << '|' << std::fixed << std::setprecision(2) << d.min_salary * 0.01 << '\n';
  }
  
  for(auto it = d.max_names.begin(); it != d.max_names.end(); it += 2){
    std::cout << "global_max|" << *it << ' ' << *(it + 1) << '|' << std::fixed << std::setprecision(2) << d.max_salary * 0.01 << '\n';
  }
  
  std::cout << "global_avg|" << std::fixed << std::setprecision(2) << d.total_salary * 0.01 / d.total_employees << '\n';
  
  //areas
  
  const Area* least_employees = nullptr;
  const Area* most_employees = nullptr;
  
  for(auto& pair : d.areas){
    const Area& area = pair.second;
    if(area.total_employees > 0){
      std::cout << "area_avg|" << area.name << '|' << std::fixed << std::setprecision(2) << area.total_salary * 0.01 / area.total_employees << '\n';
      
      for(auto it = area.min_names.begin(); it != area.min_names.end(); it += 2){
        std::cout << "area_min|" << area.name << '|' << *it << ' ' << *(it + 1) << '|' << std::fixed << std::setprecision(2) << area.min_salary * 0.01 << '\n';
      }
      
      for(auto it = area.max_names.begin(); it != area.max_names.end(); it += 2){
        std::cout << "area_max|" << area.name << '|' << *it << ' ' << *(it + 1) << '|' << std::fixed << std::setprecision(2) << area.max_salary * 0.01 << '\n';
      }
      
      if(most_employees == nullptr || area.total_employees > most_employees->total_employees){
        most_employees = &area;
      }
      
      if(least_employees == nullptr || area.total_employees < least_employees->total_employees){
        least_employees = &area;
      }
    }
  }
  
  std::cout << "least_employees|" << least_employees->name << '|' << least_employees->total_employees << '\n';
  std::cout << "most_employees|" << most_employees->name << '|' << most_employees->total_employees << '\n';
  
  //surnames
  
  for(auto& pair : d.surnames){
    const HString& surname_str = pair.first;
    const Surname& surname = pair.second;
    if(surname.total_employees > 1){
      for(auto& name : surname.max_names){
        std::cout << "last_name_max|" << surname_str << '|' << name << ' ' << surname_str << '|' << std::fixed << std::setprecision(2) << surname.max_salary * 0.01 << '\n';
      }
    }
  }
}