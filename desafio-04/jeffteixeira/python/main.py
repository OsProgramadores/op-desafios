'''Counts pieces in the board'''

class Piece:
    '''A class that represents a piece of the board'''

    def __init__(self, code, name, quantity):
        ''''Constructs all the necessary atributes for the piece object'''
        self.set_code(code)
        self.set_name(name)
        self.set_quantity(quantity)

    def get_code(self):
        '''Returns the piece code'''
        return self.__code

    def set_code(self, code):
        '''Sets the piece code'''
        self.__code = code

    def get_name(self):
        '''Returns the piece name'''
        return self.__name

    def set_name(self, name):
        '''Sets the piece name'''
        self.__name = name

    def get_quantity(self):
        '''Returns the max quantity of the piece'''
        return self.__quantity

    def set_quantity(self, quantity):
        '''Sets the max quantity of the piece'''
        self.__quantity = quantity

    def __eq__(self, piece):
        return self.get_name() == piece.get_name() and self.get_code() == piece.get_code()


class Field:
    '''A class that represents a field of the board'''

    def __init__(self, piece=None):
        '''Constructs all the necessary atributes for the field object'''
        self.set_piece(piece)

    def get_piece(self):
        '''Returns the piece that is in the field or None if the field is empty'''
        return self.__piece


    def set_piece(self, piece):
        '''Sets a piece in the field'''
        self.__piece = piece


    def is_filled(self):
        '''Checks if the field is filled or not'''
        return self.get_piece() is not None


class Board:
    '''A class that represents a board'''

    def __init__(self):
        '''Constructs all the necessary atributes for the board object'''
        self.__lines = 8
        self.__columns = 8
        self.__pieces = [
            Piece(code=1, name='Peão', quantity=16),
            Piece(code=2, name='Bispo', quantity=4),
            Piece(code=3, name='Cavalo', quantity=4),
            Piece(code=4, name='Torre', quantity=4),
            Piece(code=5, name='Rainha', quantity=2),
            Piece(code=6, name='Rei', quantity=2)
        ]
        self.__fields = [[Field() for j in range(self.__columns)] for i in range(self.__lines)]

    def get_fields(self):
        '''Returns the fields of the board'''
        return self.__fields

    def get_field(self, position):
        '''Returns a field of the board'''
        line = position[0]
        column = position[1]
        return self.get_fields()[line][column]

    def get_pieces(self):
        '''Returns the pieces of the board'''
        return self.__pieces

    def get_piece(self, code):
        '''Returns a pice of the board'''
        return self.get_pieces()[code - 1]

    def get_valid_positions(self):
        '''Returns tha valid positions of the board'''
        positions = []
        for i in range(self.__lines):
            for j in range(self.__columns):
                position = (i, j)
                field = self.get_field(position)
                if not field.is_filled():
                    positions.append(position)
        return positions

    def add_piece(self, code, line, column):
        '''Adds a piece on the board'''
        codes = [piece.get_code() for piece in self.get_pieces()]
        position = (line, column)
        if code in codes:
            if position in self.get_valid_positions():
                field = self.get_field(position)
                piece = self.get_piece(code)
                occurrences = self.count_piece(piece)
                max_quantity = piece.get_quantity()
                if occurrences < max_quantity:
                    field.set_piece(piece)
                else:
                    print('\nPiece with code {} has reached its limit of {} occurrences!'.
                    format(piece.get_code(), occurrences))
            else:
                print('\nPosition ({}, {}) is invalid or is already filled!'.format(
                    position[0], position[1])
                )
        else:
            print('\nCode {} being inserted in position ({}, {}) is invalid!'.format(
                code, position[0], position[1])
            )

    def count_piece(self, piece):
        '''Counts the occurrences of a piece on the board'''
        quantity = 0
        if piece in self.get_pieces():
            for line in self.get_fields():
                for field in line:
                    if field.is_filled() and field.get_piece() == piece:
                        quantity += 1
        return quantity

    def __str__(self):
        result = ''
        for piece in self.__pieces:
            result += '\n{}: {} peça(s)'.format(piece.get_name(), self.count_piece(piece))
        return result


def main():
    '''Function main of the program'''

    b = Board()
    b.add_piece(code=4, line=0, column=0)
    b.add_piece(code=3, line=0, column=1)
    b.add_piece(code=2, line=0, column=2)
    b.add_piece(code=5, line=0, column=3)
    b.add_piece(code=6, line=0, column=4)
    b.add_piece(code=2, line=0, column=5)
    b.add_piece(code=3, line=0, column=6)
    b.add_piece(code=4, line=0, column=7)
    b.add_piece(code=1, line=1, column=0)
    b.add_piece(code=1, line=1, column=1)
    b.add_piece(code=1, line=1, column=2)
    b.add_piece(code=1, line=1, column=3)
    b.add_piece(code=1, line=1, column=4)
    b.add_piece(code=1, line=1, column=5)
    b.add_piece(code=1, line=1, column=6)
    b.add_piece(code=1, line=1, column=7)
    b.add_piece(code=1, line=6, column=0)
    b.add_piece(code=1, line=6, column=1)
    b.add_piece(code=1, line=6, column=2)
    b.add_piece(code=1, line=6, column=3)
    b.add_piece(code=1, line=6, column=4)
    b.add_piece(code=1, line=6, column=5)
    b.add_piece(code=1, line=6, column=6)
    b.add_piece(code=1, line=6, column=7)
    b.add_piece(code=4, line=7, column=0)
    b.add_piece(code=3, line=7, column=1)
    b.add_piece(code=2, line=7, column=2)
    b.add_piece(code=5, line=7, column=3)
    b.add_piece(code=6, line=7, column=4)
    b.add_piece(code=2, line=7, column=5)
    b.add_piece(code=3, line=7, column=6)
    b.add_piece(code=4, line=7, column=7)
    print(b)


if __name__ == '__main__':
    main()
