'''Count the occurrences of each piece on the board'''


from os import system


PIECES = [
    {'code': 1, 'name': 'Peão', 'quantity': 16},
    {'code': 2, 'name': 'Bispo', 'quantity': 4},
    {'code': 3, 'name': 'Cavalo', 'quantity': 4},
    {'code': 4, 'name': 'Torre', 'quantity': 4},
    {'code': 5, 'name': 'Rainha', 'quantity': 2},
    {'code': 6, 'name': 'Rei', 'quantity': 2}
]


board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]


def count_code(code):
    '''Returns the number of occurrences of a code on the board'''
    counter = 0
    for row in board:
        counter += row.count(code)
    return counter


def get_piece_codes():
    '''Returns a list with the codes of the pieces'''
    codes = [piece.get('code') for piece in PIECES]
    return codes


def get_piece(code):
    '''Returns the piece that has the code passed as a parameter'''
    piece = PIECES[code - 1]
    return piece


def the_board_is_filled():
    '''Returns True if the board is filled. Otherwise, returns False'''
    for piece in PIECES:
        code = piece.get('code')
        max_quantity = piece.get('quantity')
        current_quantity = count_code(code)
        if current_quantity < max_quantity:
            return False
    return True


def the_line_is_filled(line):
    '''Returns True if a line of the board is filled. Otherwise, returns False'''
    for code in board[line]:
        if code == 0:
            return False
    return True


def get_valid_code():
    '''Returns a valid code of a piece'''
    while True:
        try:
            system('clear')
            print_board()
            show_pieces_code_and_name()
            code = int(input('\nCode: '))
            codes = get_piece_codes()
            if code in codes:
                piece = get_piece(code)
                current_quantity = count_code(code)
                max_quantity = piece.get('quantity')
                if current_quantity < max_quantity:
                    break
                piece = get_piece(code)
                quantity = piece.get('quantity')
                name = piece.get('name')
                print('\nPiece with code {} and name {} has reached its limit of {} occurrences!'.
                format(code, name, quantity))
                input('\nPress ENTER to continue... ')
            else:
                print('\nInvalid code!')
                input('\nPress ENTER to continue... ')
        except ValueError:
            print('\nOnly numbers are acepted!')
            input('\nPress ENTER to continue... ')
    return code


def get_valid_line(code):
    '''Returns a valid line of the board'''
    while True:
        try:
            system('clear')
            print_board()
            print('Code: {}\n'.format(code))
            line = int(input('Line: '))
            if line in range(8):
                if not the_line_is_filled(line):
                    break
                print('\nThe line {} is filled!'.format(line))
                input('\nPress ENTER to continue... ')
            else:
                print('\nInvalid line!')
                input('\nPress ENTER to continue... ')
        except ValueError:
            print('\nOnly numbers are acepted!')
            input('\nPress ENTER to continue... ')
    return line


def get_valid_column(code, line):
    '''Returns a valid column of the board'''
    while True:
        try:
            system('clear')
            print_board()
            print('Code: {}\n'.format(code))
            print('Line: {}\n'.format(line))
            column = int(input('Column: '))
            if column in range(8):
                if board[line][column] == 0:
                    break
                print('\nThe line {} and column {} is filled!'.format(line, column))
                input('\nPress ENTER to continue... ')
            else:
                print('\nInvalid column!')
                input('\nPress ENTER to continue... ')
        except ValueError:
            print('\nOnly numbers are acepted!')
            input('\nPress ENTER to continue... ')
    return column


def print_board():
    '''Show the board'''
    print('     _______________________________')
    print(' ___|_0_|_1_|_2_|_3_|_4_|_5_|_6_|_7_|')
    for i, row in enumerate(board):
        print('|_{}_|'.format(i), end='')
        for j, code in enumerate(row):
            if j == len(row) - 1:
                print('_{}_|'.format(code))
            else:
                print('_{}_|'.format(code), end='')
    print()


def show_pieces_code_and_name():
    '''Show the code and name of each piece'''
    for piece in PIECES:
        code = piece.get('code')
        name = piece.get('name')
        if count_code(code) < piece.get('quantity'):
            print('{}: {}'.format(code, name))


def show_pieces_name_and_occurrences():
    '''Show the name and the number of occurrences of each piece on the board'''
    system('clear')
    for piece in PIECES:
        code = piece.get('code')
        name = piece.get('name')
        occurrences = count_code(code)
        print('{}: {} peça(s)'.format(name, occurrences))


def main():
    '''Function main of the program'''
    system('clear')
    while True:
        try:
            if the_board_is_filled():
                print('\nThe board is filled!')
                input('\nPress ENTER to continue... ')
                break
            system('clear')
            print_board()
            print('1 - Insert piece on the bord\n2 - End program\n\nOption: ', end='')
            option = int(input())
            if option < 1 or option > 2:
                print('\nInvalid option!')
                input('\nPress ENTER to continue... ')
            if option == 2:
                break
            if option == 1:
                code = get_valid_code()
                line = get_valid_line(code)
                column = get_valid_column(code, line)
                board[line][column] = code
                print('\nPiece inserted successfully!')
                input('\nPress ENTER to continue... ')
        except ValueError:
            print('\nOnly numbers are acepted!')
            input('\nPress ENTER to continue... ')
    show_pieces_name_and_occurrences()


if __name__ == '__main__':
    main()
