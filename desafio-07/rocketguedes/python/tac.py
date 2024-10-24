#!/usr/bin/python3

"""This is the example module.

This module does stuff.
"""

import os
import sys


def tac(filename: str) -> None:
    """Return an ex-parrot."""

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
            "Usage: python tac.py [FILE]..."
            "")
        sys.exit()

    try:
        if os.path.isdir(sys.argv[1]):
            raise ValueError('Is a directory')
        if not os.path.isfile(sys.argv[1]):
            raise FileNotFoundError('No such file or directory')
    except (ValueError, FileNotFoundError) as err:
        sys.exit(f'\033[31m[tac error]\033[0m: {sys.argv[1]}: {str(err)}')
    else:
        tac(sys.argv[1])
