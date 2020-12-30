"""Counts the pieces of the board"""


def main():
    """Function main of the program"""
    pieces = {
        1: { 'name': 'Peão', 'quantity': 0 },
        2: { 'name': 'Bispo', 'quantity': 0 },
        3: { 'name': 'Cavalo', 'quantity': 0 },
        4: { 'name': 'Torre', 'quantity': 0 },
        5: { 'name': 'Rainha', 'quantity': 0 },
        6: { 'name': 'Rei', 'quantity': 0 }
    }
    board = get_valid_board()
    count_pieces_on_the_board(board, pieces)
    show_pieces(pieces)


def get_valid_board():
    """Function that returns a filled matrix that represents the board"""
    board = []
    for i in range(8):
        line = []
        for j in range(8):
            message = 'Enter a number to line {} and column {} between 0 and 8: '.format(
                i + 1, j + 1
            )
            number = get_valid_number(message)
            line.append(number)
        board.append(line)
    if is_valid(board):
        return board
    print('Invalid board!\n')
    return get_valid_board()


def get_valid_number(message):
    """Function that returns a valid number between 0 and 8"""
    while True:
        try:
            number = int(input(message))
            if 0 <= number <= 8:
                return number
        except ValueError:
            print('Only numbers are acepted!')


def is_valid(board):
    """Function that checks if the board is valid or not"""
    quantity_per_number = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0
    }
    for line in board:
        for number in line:
            quantity_per_number[number] += 1
    return quantity_per_number[1] <= 16 and \
        quantity_per_number[2] <= 4 and \
            quantity_per_number[3] <= 4 and \
                quantity_per_number[4] <= 4 and \
                    quantity_per_number[5] <= 2 and \
                        quantity_per_number[6] <= 2


def count_pieces_on_the_board(board, pieces):
    """Function that counts the occurrences of each piece on the board"""
    for line in board:
        for number in pieces.keys():
            pieces[number]['quantity'] += line.count(number)


def show_pieces(pieces):
    """Function that shows the name and occurrences of each piece on the board"""
    print()
    for piece in pieces.values():
        print('{}: {} peça(s)'.format(piece['name'], piece['quantity']))


if __name__ == "__main__":
    main()
