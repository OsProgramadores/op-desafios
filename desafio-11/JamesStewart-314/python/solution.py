import os
import math
from itertools import count
from collections import defaultdict
from typing import Generator

def get_set_primes(num_digits: int, upper_limit: int) -> set[str]:
    primes_set: set[str] = set()
    current_num: str = '2'
    primes_set.update(current_num.zfill(z_qty) for z_qty in range(1, num_digits))
    sieve_dict: dict[int, int] = {}
    num_counter: count = count(start=3, step=2)
    for current_num in num_counter:
        if current_num >= upper_limit:
            return primes_set
        if current_num not in sieve_dict:
            sieve_dict[current_num * current_num] = current_num
            current_num: str = str(current_num)
            primes_set.update(current_num.zfill(z_qty) for z_qty in range(1, num_digits))
        else:
            current_num_key: int = current_num + (sieve_dict[current_num] << 1)
            while sieve_dict.get(current_num_key):
                current_num_key += (sieve_dict[current_num] << 1)
            sieve_dict[current_num_key] = sieve_dict[current_num]
            del sieve_dict[current_num]


def print_biggest_seq(file_path: str, upper_limit: int = 10 ** 4) -> str:
    try:
        pi_digits: str = open(file_path, "r").readline().rstrip()
    except FileNotFoundError as error:
        raise Exception(f"Error: Could open file \'{file_path}\'.") from error

    try:
        pi_digits: str = pi_digits[pi_digits.index('.') + 1:]
    except ValueError:
        pass

    prime_numbers: set[str] = get_set_primes(int(math.log10(upper_limit)) + 1, upper_limit)

    prim_seq: defaultdict[int, str] = defaultdict(str)
    for idx in range(len(pi_digits)):
        current_num: str = ""
        for qty in range(4):
            try:
                current_num += pi_digits[(s := idx + qty)]
            except IndexError:
                break
            if not current_num in prime_numbers:
                continue
            if len(prim_seq[(t := s + 1)]) < len(prim_seq[idx]) + len(current_num):
                prim_seq[t] = prim_seq[idx] + current_num

    print(max(prim_seq.values(), key=len, default=''))

if __name__ == '__main__':
    file_path: str = os.path.join(os.path.dirname(__file__), "pi-1M.txt")
    print_biggest_seq(file_path)
