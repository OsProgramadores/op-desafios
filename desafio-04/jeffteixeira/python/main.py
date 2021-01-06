"""Counts the occurrences of each piece"""


from os import system
from time import sleep

def main():
    """Function main of the program"""
    pieces = get_pieces()
    count_pieces(pieces)
    show_pieces(pieces)


def get_pieces():
    """Function that returns a dictionary that represents the pieces"""
    return {
        0: { 'name': 'Vazio', 'current_quantity': 0, 'maximum_quantity': 64 },
        1: { 'name': 'Peão', 'current_quantity': 0, 'maximum_quantity': 16 },
        2: { 'name': 'Bispo', 'current_quantity': 0, 'maximum_quantity': 4 },
        3: { 'name': 'Cavalo', 'current_quantity': 0, 'maximum_quantity': 4 },
        4: { 'name': 'Torre', 'current_quantity': 0, 'maximum_quantity': 4 },
        5: { 'name': 'Rainha', 'current_quantity': 0, 'maximum_quantity': 2 },
        6: { 'name': 'Rei', 'current_quantity': 0, 'maximum_quantity': 2 }
    }


def count_pieces(pieces):
    """Function that counts the occurrences of each piece"""
    accepted_codes = list(pieces.keys())
    for i in range(1, 9):
        for j in range(1, 9):
            message = get_message(i, j, accepted_codes, pieces)
            code = get_valid_code(accepted_codes, message)
            piece = pieces[code]
            piece['current_quantity'] += 1
            if piece['current_quantity'] == piece['maximum_quantity']:
                print('\nThe code {} has reached its limit of {} occurrences!'
                .format(code, pieces[code]['maximum_quantity']))
                accepted_codes.remove(code)
                sleep(3)


def get_message(line, column, accepted_codes, pieces):
    """Function that returns a message with code and name of each piece"""
    message = '\n'
    for code in accepted_codes:
        message += '{}: {}\n'.format(code, pieces[code]['name'])
    message += '\nEnter a of the numeric codes above for line {} and column {}\n'.format(
        line, column)
    return message


def get_valid_code(accepted_codes, message):
    """Function that returns a valid code of a piece"""
    while True:
        try:
            system('clear')
            code = int(input(message))
            if code in accepted_codes:
                return code
            print('\nInvalid numeric code!')
            sleep(3)
        except ValueError:
            print('\nOnly numbers are acepted!')
            sleep(3)


def show_pieces(pieces):
    """Function that shows the name and occurrences of each piece"""
    print()
    for piece in list(pieces.values())[1:]:
        print('{}: {} peça(s)'.format(piece['name'], piece['current_quantity']))


if __name__ == "__main__":
    main()
