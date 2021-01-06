/* Desafio 5 em C++ por Jonathas Valeriano
 * Para compilar(gcc):
 * g++ -m64 -std=c++14 -pthread -Ofast -ftree-vectorize -funroll-loops -faggressive-loop-optimizations -o d5 -Ithird_part *.cpp
 *
 * Obs!: fork do source da solução C++ feita por Elias Correa.
 * Todos os créditos dos algoritmos e estruturas de dados para o dev original desta solução.
*/

#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <iomanip>

#include <cmath>

#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <chrono>
#include <fstream>
#include <sstream>
#include <atomic>
#include <mutex>

#include "TasksQueue_Manager.hpp"

//Hashed string
struct HString
{
    size_t hash{0};
    char *str, len{0};
};

inline bool operator == (const HString& a, const HString& b)
{
    return a.hash == b.hash;
}

inline std::ostream& operator << (std::ostream& os, const HString& hs)
{
    os.write(hs.str, hs.len);
    return os;
}

struct HStringHash
{
    inline size_t operator() (const HString& hs) const
    {
        return hs.hash;
    }
};

struct Surname
{
    std::vector<HString> max_names;
    HString surname_str;
    int total_employees{0};
    int max_salary{0};
    std::atomic<bool> m_lk{false};

    inline void lk()
    {
        bool expects{false};
        while(!m_lk.compare_exchange_weak(expects, true, std::memory_order_release, std::memory_order_relaxed))
        {
            expects = false;
        }
    }

    inline void unlk()
    {
        m_lk.store(false, std::memory_order_release);
    }
};

struct Area
{
    std::vector<HString> min_names, max_names;
    HString name;
    long long int total_salary{0};
    int total_employees{0};
    int min_salary = std::numeric_limits<int>::max(), max_salary{0};
};

#define _map_size_max_ 11000

template<
    typename Key,
    typename T,
    typename Hash = std::hash<HString>,
    size_t root_max_sz = _map_size_max_,
    int b_msz = 4,
    typename KV = std::pair<size_t, T>,
    typename Row = std::pair<size_t, std::array<KV, b_msz>>
>
class MT_HMap
{
    Row table[_map_size_max_];
    std::atomic<bool> lk_bucket[_map_size_max_]={false};
    Hash hash;

    inline bool try_lk(int n)
    {
        bool expects{false};
        while(!lk_bucket[n].compare_exchange_strong(expects, true, std::memory_order_release, std::memory_order_relaxed))
        {
            return false;
        }

        return true;
    }

    inline void lk(int n)
    {
        bool expects{false};
        while(!lk_bucket[n].compare_exchange_strong(expects, true, std::memory_order_release, std::memory_order_relaxed))
        {
            expects = false;
        }
    }
    
    inline void unlk(int n)
    {
        lk_bucket[n].store(false, std::memory_order_release);
    }

public:

    MT_HMap()
    {
        for(Row &r: table)
        {
            r.first = 0;
            for(auto &p: r.second)
            {
                p.first = 0;
            }
        }
    }

    inline const Row& get_bucket(int n) const
    {
        return table[n];
    }

    inline Row& get_bucket(int n)
    {
        return table[n];
    }

    inline T* at(Key& key)
    {
        const size_t cur_hash = hash(key);
        const size_t n = cur_hash % _map_size_max_;

        T *value{nullptr};

        Row &pair = table[n];

        auto &list = pair.second;
        size_t &hash_val = pair.first;

        retry:

        if(hash_val == cur_hash)
        {
            value = &list.back().second;
        }
        else if(hash_val > 0)
        {
            int sz = b_msz-1;
            for(auto &sn: list)
            {
                size_t &sn_h = sn.first;
                
                retry2:
                
                if(sn_h == cur_hash)
                {
                    value = &sn.second;
                    break;
                }
                else if(sn_h == 0)
                {
                    if(!try_lk(n)){ goto retry2; }
                    if(sn_h != 0){ unlk(n); goto retry2; }
                    
                        value = &sn.second;
                        value->surname_str.str = key.str;
                        value->surname_str.len = key.len;
                        sn_h = cur_hash;
                        
                    unlk(n);
                    break;
                }
                else if(--sz == 0){ break; }
            }
        }
        else
        {
            if(!try_lk(n)){  goto retry;  }
            if(hash_val != 0){ unlk(n); goto retry; }
            
            auto &v = list[b_msz-1];
            v.first = cur_hash;
            value = &v.second;
            value->surname_str.str = key.str;
            value->surname_str.len = key.len;
            hash_val = cur_hash;

            unlk(n);
        }

        return value;
    }
};

struct ThreadData
{
    char *buffer;
    size_t total_salary{0};
    size_t buffer_len;
    size_t buffer_offset;
    int total_employees{0};
    int min_salary = std::numeric_limits<int>::max(), max_salary{0};
    std::vector<HString> min_names, max_names;

    MT_HMap<HString, Surname, HStringHash> *surnames{nullptr};
    Area areas[2]{ Area() };
};


template<typename Container>
inline void add_min_name(Container& list, int& list_salary, const HString& name, const HString& surname, int salary)
{
    if(list_salary == salary)
    {
        list.emplace_back(std::move(name));
        list.emplace_back(std::move(surname));
    }
    else if(list_salary == 0 || salary < list_salary)
    {
        list_salary = salary;
        list.clear();
        list.emplace_back(std::move(name));
        list.emplace_back(std::move(surname));
    }
}

template<typename Container>
inline void add_max_name(Container& list, int& list_salary, const HString& name, const HString& surname, int salary)
{
    if(list_salary == salary)
    {
        list.emplace_back(std::move(name));
        list.emplace_back(std::move(surname));
    }
    else if(list_salary == 0 || salary > list_salary)
    {
        list_salary = salary;
        list.clear();
        list.emplace_back(std::move(name));
        list.emplace_back(std::move(surname));
    }
}

template<typename Container>
inline void add_max_surname(Container& list, int& list_salary, const HString& name, int salary)
{
    if(list_salary == salary)
    {
        list.emplace_back(std::move(name));
    }
    else if(salary > list_salary || list_salary == 0)
    {
        list_salary = salary;
        list.clear();
        list.emplace_back(std::move(name));
    }
}

template<typename Container>
inline void join_name_list(const Container& source_list, Container& dest_list, int source_salary, int& dest_salary, bool keep_min)
{
    if(source_salary == 0) return;

    if(source_salary == dest_salary)
    {
        dest_list.insert(dest_list.end(), source_list.begin(), source_list.end());
    }
    else if(dest_salary == 0 ||
            (keep_min && source_salary < dest_salary) ||
            (!keep_min && source_salary > dest_salary))
    {
        dest_salary = source_salary;
        dest_list = source_list;
    }
}

inline char *get_string(char *c, HString& hs, bool recycle = false)
{
    while(*c != ':') ++c;
    c += 2;
    char *start = c;
    if(recycle && *(c + hs.len) == '"' && *(c + hs.len + 1) == ',')
    {
        c += hs.len;
    }
    else
    {
        c+=2;
        while(*c != '"') ++c;
    }

    hs.len = static_cast<size_t>(c - start);
    hs.str = start;
    return ++c;
}

inline char* get_hashed(char* c, unsigned salt, HString& hs)
{
    while(*c != ':') ++c;
    c += 2;
    char *start = c;

    unsigned h = salt;
    while (*c != '"')
    {
        h = h * 101 + (unsigned char) *c++;
    }

    hs.hash = h;
    hs.len = static_cast<size_t>(c - start);
    hs.str = start;

    return ++c;
}

inline char* get_string_hashed(char *c, HString& hs, size_t salt = 0)
{
    while(*c != ':') ++c;
    c += 2;
    char *start = c;

    //calc X31 hash while reading
    size_t h{salt};
    for(; *c != '"'; ++c)
    {
        h = (h << 5) - h + *c;
    }

    hs.hash = h;
    hs.len = static_cast<size_t>(c - start);
    hs.str = start;

    return ++c;
}

inline char *get_string_hashed(char *c, HString& hs, int max, int jump)
{
    while(*c != ':') ++c;
    c += 2;
    char *start = c;

    //calc X31 hash while reading
    size_t h{1};
    for(h = 0; *c != '"'; ++c)
    {
        h = (h << 5) - h + *c;
        if(--max == 0){ break; }
    }

    c = c + (max? 0: max);

    hs.hash = h;
    hs.len = static_cast<size_t>(c - start);
    hs.str = start;

    return ++c;
}

inline char *get_string_hashed_n(char *c, HString& hs, int n = 0)
{
    while(*c != ':') ++c;
    c += 2;
    char *start = c;

    //calc X31 hash while reading
    size_t h;
    if(n >= 6)
    {
        int i=0;
        for(h = 0; *c != '"'; ++c)
        {
            if(i++ < n){ h = (h << 5) - h + *c; }
        }
    }
    else
    {
        for(h = 0; *c != '"'; ++c)
        {
            h = (h << 5) - h + *c;
        }
    }

    hs.hash = h;
    hs.len = static_cast<size_t>(c - start);
    hs.str = start;

    return ++c;
}

static inline char* meiyan_hash(char *key, HString& hs)
{
    while(*key != ':') ++key;
    key += 2;
    char *start = key;

    for(; *key != '"'; ++key){}

    int count = static_cast<int>(key-start);

    char* c = start;

    typedef uint32_t* P;
    uint32_t h = 0x811c9dc5;
    while (count >= 8) 
    {
        h = (h ^ ((((*(P)c) << 5) | ((*(P)c) >> 27)) ^ *(P)(c + 4))) * 0xad3e7;
        count -= 8;
        c += 8;
    }
    #define tmp h = (h ^ *(uint16_t*)c) * 0xad3e7; c += 2;
    if (count & 4) { tmp tmp }
    if (count & 2) { tmp }
    if (count & 1) { h = (h ^ *c) * 0xad3e7; }
    #undef tmp

    hs.hash = h ^ (h >> 16);
    hs.len = static_cast<size_t>(key - start);
    hs.str = start;

    return ++c;
}

char* hash_string(char *c, HString& hs)
{
    while(*c != ':') ++c;
    c += 2;
    char *start = c;

    uint32_t hash = 1;

    for(; *c != '"'; )
    {
        hash += *c++;
        hash += (hash << 10);
        hash ^= (hash >> 6);
    }

    hash += (hash << 3);
    hash ^= (hash >> 11);
    hash += (hash << 15);

    hs.hash = hash;
    hs.len = static_cast<size_t>(c - start);
    hs.str = start;

    return ++c;
}

///* CRC-32C (iSCSI) polynomial in reversed bit order. */
#define POLY 0x82f63b78
char* crc32c(uint32_t crc, char *c, HString& hs)
{
    while(*c != ':') ++c;
    c += 2;
    char *start = c;

    int k;

    crc = ~crc;
    while (*c != '"') 
    {
        crc ^= *c++;
        for (k = 0; k < 8; k++)
            crc = crc & 1 ? (crc >> 1) ^ POLY : crc >> 1;
//            crc = (crc >> 1) ^ (POLY & (0 - (crc & 1)));
    }

    hs.hash = ~crc;
    hs.len = static_cast<size_t>(c - start);
    hs.str = start;

    return ++c;
}

inline char *get_number(char *c, int& num)
{
    while(*c != ':') ++c;
    ++c;
    for(num = 0; *c != '.'; ++c)
        num = num * 10 + (*c - '0');
    num = num * 10 + (*++c - '0');
    num = num * 10 + (*++c - '0');
    return ++c;
}

struct SNS
{
    HString surname, name;
    size_t salary;

    SNS(HString& surname_, HString& name_, size_t salary_)
    : surname{surname_}, name{name_}, salary{salary_}
    {}
};

struct cmp_sns
{
    bool operator()(const SNS& a, const SNS& b) const
    {
        if(a.surname.hash < b.surname.hash){ return true; }
        else if(a.surname.hash == b.surname.hash)
        {
            if(a.salary > b.salary){ return true; }
        }

        return false;
    }

    bool operator()(const SNS* a, const SNS* b) const
    {
        if(a->surname.hash < b->surname.hash){ return true; }
        else if(a->surname.hash == b->surname.hash)
        {
            if(a->salary > b->salary){ return true; }
        }

        return false;
    }
};

struct cmp_sns_less
{
    bool operator()(const SNS& a, const SNS& b) const
    {
        if(a.surname.hash < b.surname.hash){ return true; }

        return false;
    }
};

void parse_json_chunk(ThreadData *data, TTasks::Task& task)
{
    ::madvise(data->buffer, data->buffer_len, MADV_SEQUENTIAL | MADV_WILLNEED);

    int salary, id_offset = 0;
    HString name_str, surname_str, area_str;

    Area *area;
    Surname *surname;
    auto *surnames_map = data->surnames;

    char *c = data->buffer;
    char *c_end = data->buffer + data->buffer_len;

    for(;;)
    {
        while(c != c_end && *c != '"') ++c;

        if(c == c_end)
          break;
        else
          ++c;

        switch(*c)
        {
            case 'i': {//employee (starts with i of id)
                //ignore id
                c += 4;
                const char* s = c;
                if(id_offset == 0)
                {
                    while(*c != ',')
                    {
                        ++id_offset;
                        ++c;
                    }
                }
                else 
                {
                    if(*(c + id_offset) == ',')
                    {
                        c += id_offset;
                    }
                    else if(*(c + id_offset + 1) == ',')
                    {
                        ++id_offset;
                        c += id_offset;
                    }
                    else
                    {
                        while(*c != ',') ++c;
                    }
                }

                c += 7;
                c = get_string(c, name_str, true);

                c += 12;
                s = c;
                c = get_hashed(c, 1, surname_str);

                c += 10;
                c = get_number(c, salary);

                c += 6;
                c = get_string_hashed(c, area_str);

                data->total_salary += salary;
                ++data->total_employees;
                if(salary <= data->min_salary)
                {
                    add_min_name(data->min_names, data->min_salary, name_str, surname_str, salary);
                }
                if(salary >= data->max_salary)
                {
                    add_max_name(data->max_names, data->max_salary, name_str, surname_str, salary);
                }

                area = &data->areas[ !(area_str.hash == 2064) ];

                ++area->total_employees;
                area->total_salary += salary;
                
                if(salary <= area->min_salary)
                {
                    add_min_name(area->min_names, area->min_salary, name_str, surname_str, salary);
                }
                if(salary >= area->max_salary)
                {
                    add_max_name(area->max_names, area->max_salary, name_str, surname_str, salary);
                }

                surname = surnames_map->at(surname_str);

                ++surname->total_employees;
                if(salary >= surname->max_salary)
                {
                    surname->lk();
                    if(salary >= surname->max_salary){
                        add_max_surname(surname->max_names, surname->max_salary, name_str, salary);
                    }
                    surname->unlk();
                }

                break;
            }
            case 'c': {//area (starts with c of code)
                c += 6;
                c = get_string_hashed(c, area_str);

                c += 6;
                c = get_string(c, name_str);

                if(area_str.hash == 2064){ data->areas[0].name = name_str; }
                else if(area_str.hash == 2065){ data->areas[1].name = name_str; }

                break;
            }
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

int main(int argc, char *argv[])
{
//    ScopedTimer timer{"\nTotal elapsed time"};

    if(argc != 2 && argc != 3){
        std::cout << "Usage: d5 [num_threads] <file>";
        return 1;
    }

    std::string filename;
    int file;
    int num_threads;

    if(argc == 3)
    {
        num_threads = atoi(argv[1]);
        filename = argv[2];
        file = open64( argv[2], O_RDWR | O_NOATIME, 0644 );
    }
    else
    {
        num_threads = std::thread::hardware_concurrency();
        filename = argv[1];
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

    posix_fadvise64(file, 0, file_size, POSIX_FADV_SEQUENTIAL | POSIX_FADV_WILLNEED);

    size_t offset{0};
    const int64_t aligned_offset = make_offset_page_aligned(offset);
    const int64_t length_to_map = offset - aligned_offset + file_size;

    char* mapping_start = static_cast<char*>(
        ::mmap64(
            0,
            length_to_map,
            PROT_READ,
            MAP_SHARED | MAP_POPULATE | MAP_NONBLOCK,
            file,
            aligned_offset
        )
    );

    int num_tasks = num_threads;

    if(filename.find( "10K") != std::string::npos ||
       filename.find( "50K") != std::string::npos ||
       filename.find("100K") != std::string::npos){ num_tasks = 1; }

    std::vector<ThreadData> data(num_tasks);

    char *mmap_init = mapping_start + offset - aligned_offset;

    size_t buffer_size = std::ceil(file_size / num_tasks);

//    std::cout << "num_tasks: " << num_tasks << ", threads: " << num_threads << "\n";

    using namespace TTasks;

    TasksQueue_Manager tasksManager{7};
    std::atomic<int> running_tasks{num_tasks};

    MT_HMap<HString, Surname, HStringHash> surnames_map;

    Task rootTask = tasksManager.enqueue_task(LONG_TASK,
     [mmap_init, buffer_size, &data, num_tasks, &running_tasks, file_size, &surnames_map](Task&& task) mutable {
        size_t current_pos{0};
        size_t read_size{0};
        bool last_chunk{false};
        for(int i = 0; i < num_tasks; ++i){
//            std::cout << "i = " << i << std::endl;
            if(i == num_tasks - 1){ buffer_size = file_size - current_pos; last_chunk = true; }

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
            d.surnames = &surnames_map;

            current_pos += read_size+1;

            task.enqueue_sub_task([&d, &running_tasks](Task&& subtask) mutable {
                parse_json_chunk(&d, subtask);
                running_tasks.fetch_sub(1, std::memory_order_seq_cst);
            });
        }

        task.co_join();
    });

    rootTask.self_run();

    while(running_tasks.load(std::memory_order_relaxed) > 0){ rootTask.co_wait(4); }
    while(!rootTask.can_stop()){ rootTask.co_wait(4); }

//    return 0;

    ThreadData &d = data[0];
    {
//        ScopedTimer t{"time to join surnames maps"};
        //join threads results
        for(std::vector<ThreadData>::iterator it = data.begin() + 1; it != data.end(); ++it)
        {
            //global
            d.total_employees += it->total_employees;
            d.total_salary += it->total_salary;
            join_name_list(it->min_names, d.min_names, it->min_salary, d.min_salary, true);
            join_name_list(it->max_names, d.max_names, it->max_salary, d.max_salary, false);

            //areas
            for(int i=0; i<2; i++)
            {
                Area& area1 = d.areas[i];
                Area& area2 = it->areas[i];

                if(area2.name.len){ area1.name = area2.name; }

                area1.total_employees += area2.total_employees;
                area1.total_salary += area2.total_salary;
                join_name_list(area2.min_names, area1.min_names, area2.min_salary, area1.min_salary, true);
                join_name_list(area2.max_names, area1.max_names, area2.max_salary, area1.max_salary, false);
            }
        }

    }

    std::ios_base::sync_with_stdio(false);

    //write results
    {
//        ScopedTimer timer{"time to write results to stringstream"};
        std::stringstream ss;

        //global
        for(auto it = d.min_names.begin(); it != d.min_names.end(); it += 2)
        {
            ss << "global_min|" << *it << ' ' << *(it + 1) << '|' << std::fixed << std::setprecision(2) << (double)((double)d.min_salary * 0.01) << '\n';
        }

        for(auto it = d.max_names.begin(); it != d.max_names.end(); it += 2)
        {
            ss << "global_max|" << *it << ' ' << *(it + 1) << '|' << std::fixed << std::setprecision(2) << (double)((double)d.max_salary * 0.01) << '\n';
        }

        ss << "global_avg|" << std::fixed << std::setprecision(2) << (double)((double)d.total_salary * 0.01) / (double)d.total_employees << '\n';

        //areas
        const Area* least_employees = nullptr;
        const Area* most_employees = nullptr;

        for(Area &area : d.areas)
        {
            if(area.total_employees > 0)
            {
                ss << "area_avg|" << area.name << '|' << std::fixed << std::setprecision(2) << (double)((double)area.total_salary * 0.01 / area.total_employees) << '\n';

                for(auto it = area.min_names.begin(); it != area.min_names.end(); it += 2)
                {
                    ss << "area_min|" << area.name << '|' << *it << ' ' << *(it + 1) << '|' << std::fixed << std::setprecision(2) << (double)((double)area.min_salary * 0.01) << '\n';
                }

                for(auto it = area.max_names.begin(); it != area.max_names.end(); it += 2)
                {
                    ss << "area_max|" << area.name << '|' << *it << ' ' << *(it + 1) << '|' << std::fixed << std::setprecision(2) << (double)((double)area.max_salary * 0.01) << '\n';
                }

                if(most_employees == nullptr || area.total_employees > most_employees->total_employees)
                {
                    most_employees = &area;
                }

                if(least_employees == nullptr || area.total_employees < least_employees->total_employees)
                {
                    least_employees = &area;
                }
            }
        }

        ss << "least_employees|" << least_employees->name << '|' << least_employees->total_employees << '\n';
        ss << "most_employees|" << most_employees->name << '|' << most_employees->total_employees << '\n';

        {
//            ScopedTimer timer{"time to print surnames"};
            //surnames
            for(int i=0; i<_map_size_max_; i++)
            {
                auto &bucket = d.surnames->get_bucket(i);
                if(bucket.first == 0){ continue; }

                auto &list = bucket.second;

                for(auto &kv: list)
                {
                    const Surname &surname = kv.second;
                    const HString& surname_str = surname.surname_str;

                    if(surname.total_employees > 1)
                    {
                        for(auto& name : surname.max_names)
                        {
                            ss << "last_name_max|" << surname_str << '|' << name
                               << ' ' << surname_str << '|' << std::fixed << std::setprecision(2) << (double)((double)surname.max_salary * 0.01) << '\n';
                        }
                    }

                }
            }
        }

        {
//            ScopedTimer timer{"time to write results"};
            std::cout << ss.rdbuf();
        }
    }

    ::munmap(const_cast<char*>(mapping_start), length_to_map);
    close(file);
}
