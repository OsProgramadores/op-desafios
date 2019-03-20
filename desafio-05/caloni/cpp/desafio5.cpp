#include <boost/iostreams/device/mapped_file.hpp>

#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <memory>
#include <set>
#include <sstream>
#include <string>
#include <thread>
#include <unordered_map>
#include <vector>

using namespace std;


typedef long long int LongInteger;

struct Chunk 
{
	const char* begin;
	const char* end;
};

struct Employee 
{
	Chunk name;
	Chunk surname;
	int salary;
	Chunk area;
	bool surname_max = false;
};

struct Area
{
	string name;
	vector<Employee> area_max;
	vector<Employee> area_min;
	double avg_salary = 0.0;
	LongInteger total_employees = 0;
	LongInteger total_salaries = 0;
};

struct ParseChunk
{
	shared_ptr<thread> thread_chunk;
	Chunk data_chunk;
	map<string, Area> areas;
	unordered_map<string, vector<Employee>> surname_max;
};


template<typename Cmp>
inline bool compare_exchange_employees(vector<const Area*>& lst_change, const Area& area_cmp, Cmp cmp)
{
	if (lst_change.size())
	{
		if (cmp(area_cmp.total_employees, (*lst_change.begin())->total_employees))
			lst_change = vector<const Area*>{ &area_cmp };
		else if (area_cmp.total_employees == (*lst_change.begin())->total_employees)
			lst_change.push_back(&area_cmp);
		return true;
	}
	else lst_change = vector<const Area*>{ &area_cmp };
	return false;
}


template<typename Cmp>
inline bool compare_exchange_salary(vector<Employee>& lst_change, const Employee& employee, Cmp cmp)
{
	if (lst_change.size())
	{
		if (cmp(employee.salary, lst_change.begin()->salary))
			lst_change = vector<Employee>{ employee };
		else if (employee.salary == lst_change.begin()->salary)
			lst_change.push_back(employee);
		return true;
	}
	else lst_change = vector<Employee>{ employee };
	return false;
}


template<typename Cmp>
inline bool compare_exchange_salary(vector<Employee>& lst_change, const vector<Employee>& lst_cmp, Cmp cmp)
{
	if (lst_change.size())
	{
		if (lst_cmp.size())
		{
			if (cmp(lst_cmp.begin()->salary, lst_change.begin()->salary))
				lst_change = lst_cmp;
			else if (lst_cmp.begin()->salary == lst_change.begin()->salary)
				lst_change.insert(lst_change.begin(), lst_cmp.begin(), lst_cmp.end());
			return true;
		}
	}
	else lst_change = lst_cmp;
	return false;
}


void parse(ParseChunk* data)
{
	Employee employee;
	string surname;
	string area_name;
	Area* area;
	vector<Employee>* employees;
	auto mystrchr = [&](const char* str, char ch) { while (*str && *str != ch) ++str; return str; };
	auto myatoi = [&](const char* beg, const char* end) 
	{ 
		int ret = 0; 
		while (beg < end) {
			char c = *beg++; 
			if (c == '.') continue; 
			ret = ret * 10 + c - '0'; } 
		return ret;
	};
	const char* curr = mystrchr(data->data_chunk.begin, '"');
	const char* end;

	while (curr && curr < data->data_chunk.end)
	{
		switch (curr[1])
		{
		case 'i': // employee
			curr += 2;
			curr = mystrchr(curr + 1, ',');
			curr += 6;
			curr = mystrchr(mystrchr(curr + 1, ':') + 1, '"') + 1;
			end = mystrchr(curr, '"');
			employee.name = Chunk{ curr, end };

			curr = end + 11;
			curr = mystrchr(mystrchr(curr + 1, ':') + 1, '"') + 1;
			end = mystrchr(curr, '"');
			employee.surname = Chunk{ curr, end };

			curr = end + 9;
			curr = mystrchr(curr + 1, ':') + 1;
			end = mystrchr(curr, '.') + 3;
			employee.salary = myatoi(curr, end);

			curr = end + 6;
			curr = mystrchr(mystrchr(curr + 1, ':') + 1, '"') + 1;
			end = mystrchr(curr, '"');
			employee.area = Chunk{ curr, end };

			curr = end + 1;
			curr = mystrchr(curr, '}');

			area_name = string(employee.area.begin, employee.area.end);
			area = &data->areas[area_name];

			compare_exchange_salary(area->area_max, employee, greater<LongInteger>());
			compare_exchange_salary(area->area_min, employee, less<LongInteger>());

			surname = string(employee.surname.begin, employee.surname.end);
			employees = &data->surname_max[surname];
			compare_exchange_salary(*employees, employee, greater<LongInteger>());

			++area->total_employees;
			area->total_salaries += employee.salary;

			break;


		case 'c': // area
			curr += 6;
			curr = mystrchr(mystrchr(curr + 1, ':') + 1, '"') + 1;
			end = mystrchr(curr, '"');
			area_name = string(curr, end);

			curr = end + 6;
			curr = mystrchr(mystrchr(curr + 1, ':') + 1, '"') + 1;
			end = mystrchr(curr, '"');
			data->areas[area_name].name = string(curr, end);

			curr = end + 1;
			curr = mystrchr(curr, '}');
			break;
		}

		curr = mystrchr(curr + 1, '"');
	}
}


int main(int argc, char* argv[])
{
	if (argc == 2)
	{
		const char* fileName = argv[1];

		boost::iostreams::mapped_file_source fileMap;
		fileMap.open(fileName);
		if (fileMap.is_open())
		{
			const char* data = fileMap.data();

			size_t cores = std::thread::hardware_concurrency();
			size_t chunkSize = fileMap.size() / cores;

			vector<ParseChunk> chunks(cores);

			for( size_t i = 0; i < cores; ++i )
			{
				const char* begin = data + (i * chunkSize);
				const char* end = data + ( (i+1) * chunkSize);
				chunks[i].data_chunk = Chunk{ begin, end };
				chunks[i].thread_chunk = make_shared<thread>(parse, &chunks[i]);
			}

			ParseChunk total;
			Area global;

			for (const auto& chunk : chunks)
			{
				chunk.thread_chunk->join();

				for (const auto& area : chunk.areas)
				{
					Area& total_area = total.areas[area.first];
					total_area.total_employees += area.second.total_employees;
					total_area.total_salaries += area.second.total_salaries;
					compare_exchange_salary(total_area.area_max, area.second.area_max, greater<LongInteger>());
					compare_exchange_salary(total_area.area_min, area.second.area_min, less<LongInteger>());
					if( area.second.name.size() )
						total_area.name = area.second.name;
				}

				for (const auto& surname_max : chunk.surname_max )
				{
					const string& surname = surname_max.first;
					vector<Employee>& total_surname = total.surname_max[surname];
					bool exchange = compare_exchange_salary(total_surname, surname_max.second, greater<LongInteger>());
					total_surname.begin()->surname_max = exchange;
				}
			}

			vector<const Area*> most_employees, least_employees;

			for (auto& area : total.areas)
			{
				if (area.second.total_employees)
				{
					area.second.avg_salary = ( double(area.second.total_salaries) / 100.0 ) / double(area.second.total_employees);
					global.total_employees += area.second.total_employees;
					global.total_salaries += area.second.total_salaries;
					compare_exchange_salary(global.area_max, area.second.area_max, greater<LongInteger>());
					compare_exchange_salary(global.area_min, area.second.area_min, less<LongInteger>());
					compare_exchange_employees(most_employees, area.second, greater<LongInteger>());
					compare_exchange_employees(least_employees, area.second, less<LongInteger>());
				}
			}
			global.avg_salary = ( double(global.total_salaries) / 100.0 ) / double(global.total_employees);

			auto out_salary = [](LongInteger salary) -> string
			{
				ostringstream os;
				os << (salary / 100) << '.' << setfill('0') << setw(2) << (salary % 100);
				return os.str();
			};

			for (const auto& emp : global.area_max)
				cout << "global_max|" << string(emp.name.begin, emp.name.end) << ' ' << string(emp.surname.begin, emp.surname.end) << '|' << out_salary(emp.salary) << '\n';
			for (const auto& emp : global.area_min)
				cout << "global_min|" << string(emp.name.begin, emp.name.end) << ' ' << string(emp.surname.begin, emp.surname.end) << '|' << out_salary(emp.salary) << '\n';
			cout << "global_avg|" << fixed << setprecision(2) << global.avg_salary << '\n';
			for (const auto& area : total.areas)
			{
				for (const auto& emp : area.second.area_max)
					cout << "area_max|" << area.second.name << '|' << string(emp.name.begin, emp.name.end) << ' ' << string(emp.surname.begin, emp.surname.end) << '|' << out_salary(emp.salary) << '\n';
				for (const auto& emp : area.second.area_min)
					cout << "area_min|" << area.second.name << '|' << string(emp.name.begin, emp.name.end) << ' ' << string(emp.surname.begin, emp.surname.end) << '|' << out_salary(emp.salary) << '\n';
				if( area.second.total_employees )
					cout << "area_avg|" << area.second.name << '|' << fixed << setprecision(2) << area.second.avg_salary << '\n';
			}
			for (const auto& emp : most_employees)
				cout << "most_employees|" << emp->name << '|' << emp->total_employees << '\n';
			for (const auto& emp : least_employees)
				cout << "least_employees|" << emp->name << '|' << emp->total_employees << '\n';
			for (const auto& emps : total.surname_max)
			{
				if (emps.second.begin()->surname_max || emps.second.size() > 1)
				{
					string surname = string(emps.second.begin()->surname.begin, emps.second.begin()->surname.end);
					for (const auto& emp : emps.second)
						cout << "last_name_max|" << surname << '|' << string(emp.name.begin, emp.name.end) << ' ' << surname << '|' << out_salary(emp.salary) << '\n';
				}
			}

			fileMap.close();
		}
	}
	else cout << "How to use: program <input-file>\n";
}

