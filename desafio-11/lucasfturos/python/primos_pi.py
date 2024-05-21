""" Author: Lucas Turos - @lucasfturos
    Description: Descobre a maior sequências de números primos no número de PI
"""

import sys
from math import sqrt
from typing import List, Set
from dataclasses import dataclass


@dataclass
class PrimesPi:
    """Classe para processar e encontrar a maior sequência de números primos em Pi"""

    filename: str
    pi_digits: str
    primes: Set[int]

    def is_prime(self, num: int) -> bool:
        """Função para testar se é um número primo"""
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        sqrt_num = int(sqrt(num))
        for i in range(3, sqrt_num + 1, 2):
            if num % i == 0:
                return False
        return True

    def generate_primes(self, limit: int) -> Set[int]:
        """Função para gerar os números primos"""
        primes = set()
        for i in range(2, limit + 1):
            if self.is_prime(i):
                primes.add(i)
        return primes

    def find_longest_prime_sequence(
        self, begin: int, seq: str, longer_seq: List[str]
    ) -> None:
        """Função para encontrar a maior sequência de dígitos que formam números primos"""
        char = ""
        current_sequence = ""
        num = 0
        for i in range(begin, begin + 4):
            try:
                char += self.pi_digits[i]
                num = int(char)
            except IndexError:
                break

            if num in self.primes:
                current_sequence = seq + char
                self.find_longest_prime_sequence(i + 1, current_sequence, longer_seq)

        if len(current_sequence) > len(longer_seq[0]):
            longer_seq.clear()
            longer_seq.append(current_sequence[::])

    def read_file(self) -> None:
        """Função para ler um arquivo"""
        try:
            with open(self.filename, encoding="utf-8") as file:
                self.pi_digits = file.read().strip()
            if self.pi_digits.startswith("3."):
                self.pi_digits = self.pi_digits[2:]
        except FileNotFoundError:
            print(f"Arquivo: {self.filename} não encontrado.")
            sys.exit(1)

    def run(self) -> None:
        """Função principal da classe, onde será feita leitura, busca e imprimir o resultado"""
        longer_seq = [""]
        self.primes = self.generate_primes(9973)
        self.read_file()
        for index in range(len(self.pi_digits)):
            self.find_longest_prime_sequence(index, "", longer_seq)
        print(longer_seq[0])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python primos_pi.py caminho/do/arquivo.txt")
        sys.exit(1)

    prime_finder = PrimesPi(sys.argv[1], "", set())
    prime_finder.run()
