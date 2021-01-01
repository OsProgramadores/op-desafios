"""Counts the occurrences of each piece"""


def main():
    """Function main of the program"""
    pieces = get_pieces()
    count_pieces(pieces)
    show_pieces(pieces)


def get_pieces():
    """Function that returns a dictionary that represents the pieces"""
    return {
        1: { 'name': 'Peão', 'current_quantity': 0, 'maximum_quantity': 16 },
        2: { 'name': 'Bispo', 'current_quantity': 0, 'maximum_quantity': 4 },
        3: { 'name': 'Cavalo', 'current_quantity': 0, 'maximum_quantity': 4 },
        4: { 'name': 'Torre', 'current_quantity': 0, 'maximum_quantity': 4 },
        5: { 'name': 'Rainha', 'current_quantity': 0, 'maximum_quantity': 2 },
        6: { 'name': 'Rei', 'current_quantity': 0, 'maximum_quantity': 2 }
    }


def count_pieces(pieces):
    """Function that counts the occurrences of each piece"""
    accepted_codes = [0, 1, 2, 3, 4, 5, 6]
    for i in range(8):
        for j in range(8):
            msg = 'Line {} and column {}: '.format(i + 1, j + 1)
            code = get_valid_code(accepted_codes, msg)
            if code > 0:
                piece = pieces[code]
                piece['current_quantity'] += 1
                if piece['current_quantity'] == piece['maximum_quantity']:
                    print('\nThe code {} has reached its limit of {} occurrences!\n'
                    .format(code, pieces[code]['maximum_quantity']))
                    accepted_codes.remove(code)


def get_valid_code(accepted_codes, message):
    """Function that returns a valid code of a piece"""
    message_with_accepted_codes = ', '.join(list(map(str, accepted_codes)))
    while True:
        try:
            code = int(input(message))
            if code in accepted_codes:
                return code
            print('\nAccepted codes: {}\n'.format(message_with_accepted_codes))
        except ValueError:
            print('\nOnly numbers are acepted!\n')


def show_pieces(pieces):
    """Function that shows the name and occurrences of each piece"""
    print()
    for piece in pieces.values():
        print('{}: {} peça(s)'.format(piece['name'], piece['current_quantity']))


if __name__ == "__main__":
    main()
