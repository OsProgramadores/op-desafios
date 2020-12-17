/*
 * Desafio 5 em C++ (C++11/17) por Jonathas Valeriano
 * Para compilar(gcc):
 * g++ -std=c++11 -pthread -lstdc++ -Ofast -ftree-vectorize main.cpp -I third_part/hopscotch-map/tsl/
 *
 * Obs!: fork do source da solução C++ feita por Elias Correa.
 * Todos os créditos dos algoritmos e estruturas de dados para o dev original desta solução.
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

#include <fstream>

#include <chrono>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <atomic>

#include "third_part/hopscotch-map/tsl/hopscotch_map.h"

//Hashed string
struct HString{
  size_t hash, len;
  char *str;
};

inline bool operator == (const HString& a, const HString& b){
    return a.len == b.len && a.hash == b.hash &&
           ((a.len > 0 && a.str[0] == b.str[0] && a.str[a.len - 1] == b.str[b.len - 1]) || a.len == 0);
}

std::ostream& operator << (std::ostream& os, const HString& hs){
  os.write(hs.str, hs.len);
  return os;
}

struct HStringHash{
  size_t operator () (const HString& hs) const{
    return hs.hash;
  }
};

struct Surname{
  int total_employees = 0;
  int max_salary = 0;
  std::vector<HString> max_names;
};

struct Area{
  HString name;
  int total_employees = 0;
  long long int total_salary = 0;
  int min_salary = 0, max_salary = 0;
  std::vector<HString> min_names, max_names;
};

struct ThreadData{
  char *buffer;
  size_t buffer_len;
  size_t buffer_offset;
  int total_employees = 0;
  long long int total_salary = 0;
  int min_salary = 0, max_salary = 0;
  std::vector<HString> min_names, max_names;
  tsl::hopscotch_map<HString, Surname, HStringHash> surnames;
  tsl::hopscotch_map<HString, Area, HStringHash> areas;
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

inline char *get_string(char *c, HString& hs, bool recycle = false){
  while(*c != ':') ++c;
  c += 2;
  char *start = c;
  if(recycle && *(c + hs.len) == '"' && *(c + hs.len + 1) == ','){
    c += hs.len;
  }else{
    while(*c != '"') ++c;
  }
  hs = {0, static_cast<size_t>(c - start), start};
  return ++c;
}

inline char *get_string_hashed(char *c, HString& hs){
  while(*c != ':') ++c;
  c += 2;
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
  for(num = 0; *c != '.'; ++c)
    num = num * 10 + (*c - '0');
  num = num * 10 + (*++c - '0');
  num = num * 10 + (*++c - '0');
  return ++c;
}

void parse_json_chunk(ThreadData *data){

  ::madvise(data->buffer, data->buffer_len, MADV_SEQUENTIAL);

  char *c = data->buffer;
  char *c_end = data->buffer + data->buffer_len;

  int salary, id_offset = 0;
  HString name_str, surname_str, area_str;
  Area *area;
  Surname *surname;
  for(;;){
    while(c != c_end && *c != '"') ++c;
    if(c == c_end)
      break;
    else
      ++c;
    switch(*c){
      case 'i': //employee (starts with i of id)
        //ignore id
        c += 4;
        if(id_offset == 0){
          while(*c != ','){
            ++id_offset;
            ++c;
          }
        }else{
          if(*(c + id_offset) == ','){
            c += id_offset;
          }else if(*(c + id_offset + 1) == ','){
            ++id_offset;
            c += id_offset;
          }else{
            while(*c != ',') ++c;
          }
        }

        //read name
        c += 7;
        c = get_string(c, name_str, true);

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

class ScopedTimer
{
    const std::chrono::time_point<std::chrono::steady_clock> start = std::chrono::steady_clock::now();
    const std::string phrase;
    const bool endlined{false};

public:

    ScopedTimer(const std::string& phrase, bool endl = false) : start{std::chrono::steady_clock::now()}, phrase{phrase} {};
    ~ScopedTimer()
    {
        const auto end = std::chrono::steady_clock::now();
        const std::chrono::duration<double, std::micro> diff = end-start;
        if(!endlined)
        {
            std::cout << std::string{ phrase + " --> " + std::to_string(diff.count()) + " us ~ " + std::to_string(diff.count()/1000.00) + " ms ~ " + std::to_string(diff.count()/1000000.00) + " s.\n"};
        }
        else
        {
            std::cout << std::string{ phrase + " --> " + std::to_string(diff.count()) + " us ~ " + std::to_string(diff.count()/1000.00) + " ms ~ " + std::to_string(diff.count()/1000000.00) + " s."} << std::endl;
        }
    }
};

size_t page_size()
{
    static const size_t page_size = []
    {
        return sysconf(_SC_PAGE_SIZE);
    }();
    return page_size;
}

size_t make_offset_page_aligned(size_t offset) noexcept
{
    const size_t page_size_ = page_size();
    return offset / page_size_ * page_size_;
}

int main(int argc, char *argv[]) {

//    ScopedTimer timer{"\nTotal elapsed time"};

    if(argc != 2 && argc != 3){
      std::cout << "Usage: d5 [num_threads] <file>";
      return 1;
    }

    int file;
    int num_threads;

    if(argc == 3){
      num_threads = atoi(argv[1]);
      file = open64( argv[2], O_RDWR | O_NOATIME, 0644 );
    }else{
      num_threads = std::thread::hardware_concurrency();
      file = open64( argv[1], O_RDWR | O_NOATIME, 0644 );
    }

    if(file < 0)
    {
        std::cout << "ERROR: invalid file path.";
        return 1;
    }

    //get file size
    const size_t file_size = lseek64(file, 0, SEEK_END);
    lseek64(file, 0, SEEK_SET);

    size_t offset{0};
    const int64_t aligned_offset = make_offset_page_aligned(offset);
    const int64_t length_to_map = offset - aligned_offset + file_size;

    char* mapping_start = static_cast<char*>(
        ::mmap64(
            0,
            length_to_map,
            PROT_READ,
            MAP_SHARED,
            file,
            aligned_offset
        )
    );

    std::vector<ThreadData> data(num_threads);
    std::vector<std::thread> threads( num_threads - 1 );

    char *mmap_init = mapping_start + offset - aligned_offset;

    size_t buffer_size = std::ceil(file_size / num_threads);
    size_t current_pos{0};
    size_t read_size{0};

    bool last_chunk{false};
    for(int i = 0; i < num_threads; ++i){
        //if its the last buffer, read the remains
        if(i == num_threads - 1){ buffer_size = file_size - current_pos; last_chunk = true; }

        char *buffer = mmap_init+current_pos;

        size_t j = buffer_size - 1;
        for( ; j > 0; --j){
            if(buffer[j] == '}'){
              break;
            }
        }
        read_size = j;

        auto &d = data[i];
        d.buffer = buffer;
        d.buffer_len = read_size;
        d.buffer_offset = current_pos;
        d.surnames.reserve(10000); //reserve good space to avoid slow map rebuild/realloc

        current_pos += read_size+1;

        if(i < num_threads - 1){ threads[i] = std::thread(parse_json_chunk, &data[i]); }
        else { parse_json_chunk(&data[i]); }
    }

    for(auto& thread : threads){
        if(thread.joinable()){ thread.join(); }
    }

    ThreadData &d = data[0];

    //join threads results
    for(std::vector<ThreadData>::iterator it = data.begin() + 1; it != data.end(); ++it)
    {
      //global
      d.total_employees += it->total_employees;
      d.total_salary += it->total_salary;
      join_name_list(it->min_names, d.min_names, it->min_salary, d.min_salary, true);
      join_name_list(it->max_names, d.max_names, it->max_salary, d.max_salary, false);

      //areas
      for(auto iter = it->areas.begin(); iter != it->areas.end(); iter++){
        Area& area1 = d.areas[iter->first];
        Area& area2 = iter.value();
        if(area2.name.len){ area1.name = area2.name; }

        area1.total_employees += area2.total_employees;
        area1.total_salary += area2.total_salary;
        join_name_list(area2.min_names, area1.min_names, area2.min_salary, area1.min_salary, true);
        join_name_list(area2.max_names, area1.max_names, area2.max_salary, area1.max_salary, false);
      }

      //surnames
      for(auto iter = it->surnames.begin(); iter != it->surnames.end(); iter++){
        Surname& surname1 = d.surnames[iter->first];
        Surname& surname2 = iter.value();
        surname1.total_employees += surname2.total_employees;
        join_name_list(surname2.max_names, surname1.max_names, surname2.max_salary, surname1.max_salary, false);
      }
    }

    std::ios_base::sync_with_stdio(false);

    //write results

    //global
    for(auto it = d.min_names.begin(); it != d.min_names.end(); it += 2){
      std::cout << "global_min|" << *it << ' ' << *(it + 1) << '|' << std::fixed << std::setprecision(2) << (double)((double)d.min_salary * 0.01) << '\n';
    }

    for(auto it = d.max_names.begin(); it != d.max_names.end(); it += 2){
      std::cout << "global_max|" << *it << ' ' << *(it + 1) << '|' << std::fixed << std::setprecision(2) << (double)((double)d.max_salary * 0.01) << '\n';
    }

    std::cout << "global_avg|" << std::fixed << std::setprecision(2) << (double)((double)d.total_salary * 0.01) / (double)d.total_employees << '\n';

    //areas
    const Area* least_employees = nullptr;
    const Area* most_employees = nullptr;

    for(auto& pair : d.areas){
      const Area& area = pair.second;
      if(area.total_employees > 0){
        std::cout << "area_avg|" << area.name << '|' << std::fixed << std::setprecision(2) << (double)((double)area.total_salary * 0.01 / area.total_employees) << '\n';

        for(auto it = area.min_names.begin(); it != area.min_names.end(); it += 2){
          std::cout << "area_min|" << area.name << '|' << *it << ' ' << *(it + 1) << '|' << std::fixed << std::setprecision(2) << (double)((double)area.min_salary * 0.01) << '\n';
        }

        for(auto it = area.max_names.begin(); it != area.max_names.end(); it += 2){
          std::cout << "area_max|" << area.name << '|' << *it << ' ' << *(it + 1) << '|' << std::fixed << std::setprecision(2) << (double)((double)area.max_salary * 0.01) << '\n';
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
              std::cout << "last_name_max|" << surname_str << '|' << name << ' ' << surname_str << '|' << std::fixed << std::setprecision(2) << (double)((double)surname.max_salary * 0.01) << '\n';
            }
        }
    }

    ::munmap(const_cast<char*>(mapping_start), length_to_map);
    close(file);
}