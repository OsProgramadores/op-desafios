#!/usr/bin/env python3

"""Challenge 05 written in Python."""
import sys
from functools import reduce
from mmap import ACCESS_READ, mmap
from multiprocessing import Pool, cpu_count


def get_chunks(mmap_obj, num_chunks, start, end):
    """Generate the file chunks."""
    chunk_size = (end - start + 1) // num_chunks
    mmap_obj.seek(start)
    for i in range(num_chunks):
        chunk_start = mmap_obj.tell()
        if i == num_chunks - 1:
            chunk_end = end
        else:
            chunk_end = chunk_start + chunk_size - 1
            chunk_end = mmap_obj.find(b'}', chunk_end)
            mmap_obj.seek(chunk_end + 1)
        chunk = mmap_obj[chunk_start : chunk_end + 1]
        yield chunk


def get_employees(chunk):
    """Generate the employees data."""
    employee = {}
    start = chunk.find(b'{')
    while start != -1:
        start = chunk.find(b',', start + 1)
        start = chunk.find(b':', start + 1) + 1
        end = chunk.find(b'"', start + 1)
        employee['name'] = chunk[start + 1 : end].decode()

        start = chunk.find(b':', end + 1) + 1
        end = chunk.find(b'"', start + 1)
        employee['surname'] = chunk[start + 1 : end].decode()

        employee['full_name'] = f'{employee["name"]} {employee["surname"]}'

        start = chunk.find(b':', end + 1) + 1
        end = chunk.find(b',', start + 1)
        employee['salary'] = float(chunk[start:end])

        start = chunk.find(b':', end + 1) + 1
        end = chunk.find(b'"', start + 1)
        employee['area_code'] = chunk[start + 1 : end].decode()

        yield employee

        start = chunk.find(b'{', end + 1)


def process_chunk(chunk):
    """Process the file chunk and return the processing result."""
    result = {
        'min_salary': sys.float_info.max,
        'min_full_names': [],
        'max_salary': 0.0,
        'max_full_names': [],
        'num_employees': 0,
        'sum_salary': 0.0,
        'areas': {},
        'surnames': {},
    }

    for employee in get_employees(chunk):
        result['num_employees'] += 1
        result['sum_salary'] += employee['salary']

        if employee['salary'] == result['min_salary']:
            result['min_full_names'].append(employee['full_name'])
        elif employee['salary'] < result['min_salary']:
            result['min_salary'] = employee['salary']
            result['min_full_names'] = [employee['full_name']]

        if employee['salary'] == result['max_salary']:
            result['max_full_names'].append(employee['full_name'])
        elif employee['salary'] > result['max_salary']:
            result['max_salary'] = employee['salary']
            result['max_full_names'] = [employee['full_name']]

        try:
            area_info = result['areas'][employee['area_code']]
        except KeyError:
            result['areas'][employee['area_code']] = {
                'min_salary': employee['salary'],
                'min_full_names': [employee['full_name']],
                'max_salary': employee['salary'],
                'max_full_names': [employee['full_name']],
                'num_employees': 1,
                'sum_salary': employee['salary'],
            }
        else:
            area_info['num_employees'] += 1
            area_info['sum_salary'] += employee['salary']

            if employee['salary'] == area_info['min_salary']:
                area_info['min_full_names'].append(employee['full_name'])
            elif employee['salary'] < area_info['min_salary']:
                area_info['min_salary'] = employee['salary']
                area_info['min_full_names'] = [employee['full_name']]

            if employee['salary'] == area_info['max_salary']:
                area_info['max_full_names'].append(employee['full_name'])
            elif employee['salary'] > area_info['max_salary']:
                area_info['max_salary'] = employee['salary']
                area_info['max_full_names'] = [employee['full_name']]

        try:
            surname_info = result['surnames'][employee['surname']]
        except KeyError:
            result['surnames'][employee['surname']] = {
                'num_employees': 1,
                'max_salary': employee['salary'],
                'max_full_names': [employee['full_name']],
            }
        else:
            surname_info['num_employees'] += 1

            if employee['salary'] == surname_info['max_salary']:
                surname_info['max_full_names'].append(employee['full_name'])
            elif employee['salary'] > surname_info['max_salary']:
                surname_info['max_salary'] = employee['salary']
                surname_info['max_full_names'] = [employee['full_name']]

    return result


def get_area_names(chunk):
    """Return a dictionary with the area names and the area codes."""
    area_names = {}
    start = chunk.find(b'{',)
    while start != -1:
        start = chunk.find(b':', start + 1) + 1
        end = chunk.find(b'"', start + 1)
        area_code = chunk[start + 1 : end].decode()

        start = chunk.find(b':', end + 1) + 1
        end = chunk.find(b'"', start + 1)
        area_name = chunk[start + 1 : end].decode()

        area_names[area_code] = area_name

        start = chunk.find(b'{', end + 1)

    return area_names


def join_results(result_1, result_2):
    """Join result_1 into result_2 and return result_2."""
    result_2['num_employees'] += result_1['num_employees']
    result_2['sum_salary'] += result_1['sum_salary']

    if result_1['min_salary'] == result_2['min_salary']:
        result_2['min_full_names'].extend(result_1['min_full_names'])
    elif result_1['min_salary'] < result_2['min_salary']:
        result_2['min_salary'] = result_1['min_salary']
        result_2['min_full_names'] = result_1['min_full_names']

    if result_1['max_salary'] == result_2['max_salary']:
        result_2['max_full_names'].extend(result_1['max_full_names'])
    elif result_1['max_salary'] > result_2['max_salary']:
        result_2['max_salary'] = result_1['max_salary']
        result_2['max_full_names'] = result_1['max_full_names']

    for area_code, area_info_1 in result_1['areas'].items():
        try:
            area_info_2 = result_2['areas'][area_code]
        except KeyError:
            result_2['areas'][area_code] = area_info_1
        else:
            area_info_2['num_employees'] += area_info_1['num_employees']
            area_info_2['sum_salary'] += area_info_1['sum_salary']

            if area_info_1['min_salary'] == area_info_2['min_salary']:
                area_info_2['min_full_names'].extend(
                    area_info_1['min_full_names']
                )
            elif area_info_1['min_salary'] < area_info_2['min_salary']:
                area_info_2['min_salary'] = area_info_1['min_salary']
                area_info_2['min_full_names'] = area_info_1['min_full_names']

            if area_info_1['max_salary'] == area_info_2['max_salary']:
                area_info_2['max_full_names'].extend(
                    area_info_1['max_full_names']
                )
            elif area_info_1['max_salary'] > area_info_2['max_salary']:
                area_info_2['max_salary'] = area_info_1['max_salary']
                area_info_2['max_full_names'] = area_info_1['max_full_names']

    for surname, surname_info_1 in result_1['surnames'].items():
        try:
            surname_info_2 = result_2['surnames'][surname]
        except KeyError:
            result_2['surnames'][surname] = surname_info_1
        else:
            surname_info_2['num_employees'] += surname_info_1['num_employees']

            if surname_info_1['max_salary'] == surname_info_2['max_salary']:
                surname_info_2['max_full_names'].extend(
                    surname_info_1['max_full_names']
                )
            elif surname_info_1['max_salary'] > surname_info_2['max_salary']:
                surname_info_2['max_salary'] = surname_info_1['max_salary']
                surname_info_2['max_full_names'] = (
                    surname_info_1['max_full_names']
                )

    return result_2


def show_result(result):
    """Show result information."""
    for full_name in result['min_full_names']:
        print(f'global_min|{full_name}|{result["min_salary"]:.2f}')
    for full_name in result['max_full_names']:
        print(f'global_max|{full_name}|{result["max_salary"]:.2f}')
    print(f'global_avg|{result["avg_salary"]:.2f}')

    least_employees = {
        'num_employees': result['num_employees'],
        'area_names': [],
    }

    most_employees = {
        'num_employees': 0,
        'area_names': [],
    }

    for area_info in result['areas'].values():
        if area_info['num_employees'] == least_employees['num_employees']:
            least_employees['area_names'].append(area_info['name'])
        elif area_info['num_employees'] < least_employees['num_employees']:
            least_employees['num_employees'] = area_info['num_employees']
            least_employees['area_names'] = [area_info['name']]

        if area_info['num_employees'] == most_employees['num_employees']:
            most_employees['area_names'].append(area_info['name'])
        elif area_info['num_employees'] > most_employees['num_employees']:
            most_employees['num_employees'] = area_info['num_employees']
            most_employees['area_names'] = [area_info['name']]

        for full_name in area_info['min_full_names']:
            print(f'area_min|{area_info["name"]}|{full_name}|{area_info["min_salary"]:.2f}')
        for full_name in area_info['max_full_names']:
            print(f'area_max|{area_info["name"]}|{full_name}|{area_info["max_salary"]:.2f}')
        print(f'area_avg|{area_info["name"]}|{area_info["avg_salary"]:.2f}')

    for area_name in least_employees['area_names']:
        print(f'least_employees|{area_name}|'
              + f'{least_employees["num_employees"]}')
    for area_name in most_employees['area_names']:
        print(f'most_employees|{area_name}|{most_employees["num_employees"]}')

    for surname, surname_info in result['surnames'].items():
        if surname_info['num_employees'] > 1:
            for full_name in surname_info['max_full_names']:
                print(f'last_name_max|{surname}|{full_name}|{surname_info["max_salary"]:.2f}')


def main():
    """Represent the entry point of script."""
    try:
        json_file = sys.argv[1]
    except IndexError:
        sys.exit(f'Usage: {sys.argv[0]} <file>')

    num_processes = cpu_count()

    try:
        with open(json_file, encoding='UTF-8') as file_obj:
            with mmap(file_obj.fileno(), 0, access=ACCESS_READ) as mmap_obj:
                areas_start = mmap_obj.rfind(b'[')
                areas_end = mmap_obj.rfind(b']')
                chunk = mmap_obj[areas_start : areas_end + 1]
                area_names = get_area_names(chunk)

                employees_start = mmap_obj.find(b'[')
                employees_end = mmap_obj.rfind(
                    b']', employees_start + 1, areas_start
                )
                chunks = get_chunks(
                    mmap_obj, num_processes, employees_start, employees_end
                )

                with Pool(num_processes) as pool:
                    results = pool.map(process_chunk, chunks)
                final_result = reduce(join_results, results)
                final_result['avg_salary'] = (
                    final_result['sum_salary'] / final_result['num_employees']
                )
                for area_code, area_info in final_result['areas'].items():
                    area_info['name'] = area_names[area_code]
                    area_info['avg_salary'] = (
                        area_info['sum_salary'] / area_info['num_employees']
                    )
                show_result(final_result)
    except FileNotFoundError:
        sys.exit(f'File {json_file} not found')
    except OSError:
        sys.exit('I/O error')


if __name__ == '__main__':
    main()
