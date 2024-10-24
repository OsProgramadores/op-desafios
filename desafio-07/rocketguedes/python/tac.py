#!/usr/bin/python3

"""tac

Concatenate and print files in reverse.
"""

import os
import sys


def tac(filename: str) -> None:
    """Write each FILE to standard output, last line first."""

    with open(filename, 'rb') as file:
        file.seek(0, os.SEEK_END)

        position: int = file.tell()

        leftover: bytes = b''

        while position > 0:
            move_back = min(4096, position)

            position -= move_back

            file.seek(position)

            buffer = file.read(move_back) + leftover

            lines = buffer.splitlines(keepends=True)

            leftover = lines.pop(0)

            for line in reversed(lines):
                print(line.decode('utf-8'), end='')

        print(leftover.decode('utf-8'), end='')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "A tac(1) clone written in Python.\n\n"
            "Usage: python tac.py [FILE]...\n\n"
            "Write each FILE to standard output, last line first.")
        sys.exit()

    for i in range(1, len(sys.argv)):
        try:
            if os.path.isdir(sys.argv[i]):
                raise ValueError('Is a directory')
            if not os.path.isfile(sys.argv[i]):
                raise FileNotFoundError('No such file or directory')
        except (ValueError, FileNotFoundError) as err:
            sys.exit(f'\033[31m[tac error]\033[0m: {sys.argv[i]}: {str(err)}')
        else:
            tac(sys.argv[i])
