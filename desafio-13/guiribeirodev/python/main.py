"""
Main module


Completes the knight's tour challenge using the warnsdorff algorithm.

author: guiribeirodev

versão: 1.0
"""
import re
import sys


def is_valid_input(arg):
    pattern = r"^[a-hA-H][1-8]$"

    if re.match(pattern, arg):
        return True

    return False


def get_input():
    if len(sys.argv) > 1:
        arg = sys.argv[1]

        if is_valid_input(arg):
            return True, arg.strip().lower()

        print("Argumento inválido, insira um argumento válido, ex: a3")
        return False

    print("Por favor insira um argumento, ex: a3")
    return False


def create_board(size):
    board = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(0)
        board.append(row)
    return board


def is_valid_move(y, x, board):
    size = len(board)
    is_valid = 0 <= y < size and 0 <= x < size and board[y][x] == 0
    return is_valid


def count_valid_moves(y, x, board):
    moves_y = [2, 1, -1, -2, -2, -1, 1, 2]
    moves_x = [1, 2, 2, 1, -1, -2, -2, -1]
    count = 0

    for _, (move_y, move_x) in enumerate(zip(moves_y, moves_x)):
        new_y = y + move_y
        new_x = x + move_x

        if is_valid_move(new_y, new_x, board):
            count += 1
    # for i in range(len(moves_y)):
    #     new_y = y + moves_y[i]
    #     new_x = x + moves_x[i]

    #     if is_valid_move(new_y, new_x, board):
    #         count += 1

    return count


def get_next_move(y, x, board):
    moves_y = [2, 1, -1, -2, -2, -1, 1, 2]
    moves_x = [1, 2, 2, 1, -1, -2, -2, -1]
    min_count = float('inf')
    next_y = -1
    next_x = -1

    for _, (move_y, move_x) in enumerate(zip(moves_y, moves_x)):
        new_y = y + move_y
        new_x = x + move_x

        if is_valid_move(new_y, new_x, board):
            count = count_valid_moves(new_y, new_x, board)

            if count < min_count:
                min_count = count
                next_y = new_y
                next_x = new_x

    return next_y, next_x


def warnsdorff(size, board, start_y, start_x):
    characters_board = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numbers_board = [8, 7, 6, 5, 4, 3, 2, 1]

    current_y = numbers_board.index(int(start_y))
    current_x = characters_board.index(start_x)

    print(f'{characters_board[current_x]}{numbers_board[current_y]}')

    move_number = 1
    board[current_y][current_x] = move_number

    while move_number < size * size:
        next_y, next_x = get_next_move(current_y, current_x, board)

        if next_y == -1 and next_x == -1:
            break

        current_y = next_y
        current_x = next_x

        print(f'{characters_board[current_x]}{numbers_board[current_y]}')

        move_number += 1
        board[current_y][current_x] = move_number

    return board


def main():
    size_board = 8
    board = create_board(size_board)

    value_input = get_input()

    if value_input:
        start_y = value_input[1][1]
        start_x = value_input[1][0]

        warnsdorff(size_board, board, start_y, start_x)


main()
