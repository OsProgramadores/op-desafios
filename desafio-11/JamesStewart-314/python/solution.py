import os
from itertools import count
from collections import defaultdict
from typing import Generator

def sieve_of_eratosthenes_prime_generator() -> Generator[int, None, None]:
    yield 2
    sieve_dict: dict[int, int] = {}
    num_counter: count = count(start=3, step=2)

    for current_num in num_counter:
        if current_num not in sieve_dict:
            yield current_num
            sieve_dict[current_num * current_num] = current_num
        else:
            current_num_key: int = current_num + (sieve_dict[current_num] << 1)
            while sieve_dict.get(current_num_key):
                current_num_key += (sieve_dict[current_num] << 1)
            sieve_dict[current_num_key] = sieve_dict[current_num]
            del sieve_dict[current_num]


def find_biggest_seq(pi_digits: str, upper_limit: int | float = 10e4) -> str:
    prime_numbers: set[str] = set()
    for prime_number in sieve_of_eratosthenes_prime_generator():
        if prime_number >= upper_limit:
            break
        str_num: str = str(prime_number)
        prime_numbers.update(str_num.zfill(z_qty) for z_qty in range(1, 5))

    prim_seq: defaultdict[int, str] = defaultdict(str)
    for idx in range(2, len(pi_digits)):
        curent_num: str = ""
        for qty in range(4):
            try:
                curent_num += pi_digits[(s := idx + qty)]
                if not curent_num in prime_numbers:
                    continue
                if len(prim_seq[(t := s + 1)]) < len(prim_seq[idx]) + len(curent_num):
                    prim_seq[t] = prim_seq[idx] + curent_num
            except IndexError:
                break

    return max(prim_seq.values(), key=len, default='')


if __name__ == '__main__':
    file_path: str = os.path.join(os.path.dirname(__file__), "pi-1M.txt")
    try:
        print(find_biggest_seq(open(file_path, "r").readline().strip()))
    except FileNotFoundError as error:
        raise Exception(f"Error: Could open file \'{file_path}\'.") from error
