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
    board = get_board()
    count_pieces(pieces, board)
    show_pieces(pieces)


def get_board():
    """Function that returns a filled matrix that represents the board"""
    board = []
    for i in range(8):
        line = []
        for j in range(8):
            number = int(input('Line {} and column {}: '.format(i + 1, j + 1)))
            line.append(number)
        board.append(line)
    return board


def count_pieces(pieces, board):
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
