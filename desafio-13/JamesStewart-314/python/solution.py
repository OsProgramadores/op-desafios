import re
import sys
from typing import TypeAlias

coord_pos: TypeAlias = tuple[int, int]

def map_position_to_board(coordinate_pos: coord_pos) -> str:
    return f"{chr(97 + coordinate_pos[1])}{8 - coordinate_pos[0]}"


def map_board_to_position(board_pos: str) -> coord_pos:
    return (8 - int(board_pos[1]), ord(board_pos[0]) - 97)


def get_possible_knight_moves(current_position: coord_pos) -> set[coord_pos]:
    set_pos_moves: set[coord_pos] = set()

    if (tmp_pos_1 := current_position[0] + 2) <= 7:
        if (tmp_pos_2 := current_position[1] + 1) <= 7:
            set_pos_moves.add((tmp_pos_1, tmp_pos_2))
        if (tmp_pos_2 := current_position[1] - 1) >= 0:
            set_pos_moves.add((tmp_pos_1, tmp_pos_2))

    if (tmp_pos_1 := current_position[1] + 2) <= 7:
        if (tmp_pos_2 := current_position[0] + 1) <= 7:
            set_pos_moves.add((tmp_pos_2, tmp_pos_1))
        if (tmp_pos_2 := current_position[0] - 1) >= 0:
            set_pos_moves.add((tmp_pos_2, tmp_pos_1))

    if (tmp_pos_1 := current_position[0] - 2) >= 0:
        if (tmp_pos_2 := current_position[1] + 1) <= 7:
            set_pos_moves.add((tmp_pos_1, tmp_pos_2))
        if (tmp_pos_2 := current_position[1] - 1) >= 0:
            set_pos_moves.add((tmp_pos_1, tmp_pos_2))

    if (tmp_pos_1 := current_position[1] - 2) >= 0:
        if (tmp_pos_2 := current_position[0] - 1) >= 0:
            set_pos_moves.add((tmp_pos_2, tmp_pos_1))
        if (tmp_pos_2 := current_position[0] + 1) <= 7:
            set_pos_moves.add((tmp_pos_2, tmp_pos_1))

    return set_pos_moves


class ChessKnight:
    _board_positions: set[coord_pos] = {(p1, p2) for p1 in range(8) for p2 in range(8)}

    _positions_mapping: dict[coord_pos, set[coord_pos]] = dict(zip(_board_positions,
                                                        (get_possible_knight_moves(pos)\
                                                         for pos in _board_positions)))

    def __init__(self, knight_position,
                 m_list: list[coord_pos] | None = None,
                 m_set: set[coord_pos] | None = None):
        self.current_position: coord_pos = knight_position
        self.knight_mov_history_list: list[coord_pos] = m_list or [knight_position]
        self.knight_mov_history_set: set[coord_pos] = m_set or {coord_pos}

    def __repr__(self) -> str:
        return f"ChessKnight<{self.current_position},"\
               f"{self.knight_mov_history_list},"\
               f"{self.knight_mov_history_set}>"

    @classmethod
    def move_knight(cls, knight, new_pos: coord_pos):
        new_knight = cls(new_pos,
                        [*knight.knight_mov_history_list, new_pos],
                        {*knight.knight_mov_history_set, new_pos})
        return new_knight

    @staticmethod
    def get_next_knight_moves(knight)-> set[coord_pos]:
        return ChessKnight._positions_mapping[knight.current_position] -\
               knight.knight_mov_history_set

    @staticmethod
    def next_knight_movement_size(knight, new_pos: coord_pos) -> int:
        return len(ChessKnight.get_next_knight_moves(ChessKnight.move_knight(knight, new_pos)))

    @staticmethod
    def get_warnsdorff_move(knight, pos_moves: set[coord_pos]) -> coord_pos:
        return min(pos_moves, key=lambda x: ChessKnight.next_knight_movement_size(knight, x))


def knight_tour(knight: ChessKnight) -> list[coord_pos]:
    if len(knight.knight_mov_history_list) == 64:
        return knight.knight_mov_history_list

    for _ in range(len(n_moves := ChessKnight.get_next_knight_moves(knight))):
        current_movement: tuple[int, int] = ChessKnight.get_warnsdorff_move(knight, n_moves)
        if (res := knight_tour(ChessKnight.move_knight(knight, current_movement))):
            return res
        n_moves.remove(current_movement)

    return None


if __name__ == '__main__':
    if len(sys.argv) != 2 or not re.match(r"^[a-h][1-8]$", (init_pos := sys.argv[1].lower())):
        print("Error: Provide just one argument representing a valid chess board position. "\
              "E.g.: \"python solution.py a3\".")
        sys.exit()

    initial_position: coord_pos = map_board_to_position(init_pos)
    final_path: list[coord_pos] = knight_tour(ChessKnight(initial_position))

    for position in map(map_position_to_board, final_path):
        print(position)
