import os
from typing import TextIO

class TurMach:
    _direction_map: dict[str, int] = {'l': (-1), 'r': 1, '*': 0}

    def __init__(self) -> None:
        self._turing_rules: dict[str, dict[str, tuple[str, str, str]]] = {}
        self._tape_position: int = 0
        self._current_state: str = '0'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}<{self._turing_rules}, "\
               f"{self._tape_position}, {self._current_state}>"

    @staticmethod
    def _convert_symbol(old_symbol: str, new_symbol: str) -> str:
        if new_symbol == '*':
            return old_symbol
        if new_symbol == '_':
            return ' '
        return new_symbol

    def _restore_initial_state(self) -> None:
        self._turing_rules.clear()
        self._tape_position = 0
        self._current_state = '0'

    def _check_state(self, state: str | None = None) -> bool:
        state = state if state is not None else self._current_state
        return state in self._turing_rules

    def _check_symbol(self, symbol: str, state: str | None = None) -> bool:
        state = state if state is not None else self._current_state
        return symbol in self._turing_rules[state]

    def _check_exists_valid_rule(self) -> bool:
        current_state_rule: bool = self._current_state in self._turing_rules
        generic_state_rule: bool = '*' in self._turing_rules

        return current_state_rule or generic_state_rule

    def process_datafile(self, file_path: str) -> None:
        try:
            datafile_obj: TextIO = open(file_path, "r")
        except FileNotFoundError as error:
            raise Exception(f"Error: Could not open datafile \'{file_path}\'.") from error

        for data_line in datafile_obj:
            self._restore_initial_state()
            data_line: list[str] = data_line.rstrip().split(',')
            turing_rules_file_path: str = os.path.join(os.path.dirname(file_path), data_line[0])

            try:
                turing_rules_file: TextIO = open(turing_rules_file_path, "r")
            except FileNotFoundError as error:
                raise Exception(f"Error: Could not open file \'{turing_rules_file_path}\'.")\
                      from error

            for rule_line in turing_rules_file:
                rule_line = rule_line.rstrip()
                if not rule_line or rule_line[0] == ';':
                    continue

                try:
                    rule_line = rule_line[:rule_line.index(';')].rstrip()
                except ValueError:
                    pass

                rule_line_splitted: list[str] = rule_line.split()

                self._turing_rules.setdefault(rule_line_splitted[0], {}).\
                                   setdefault(rule_line_splitted[1], rule_line_splitted[2:])

            content_tape: list[str] = list(data_line[1])
            is_valid_result: bool = True
            while True:
                if not self._check_exists_valid_rule():
                    is_valid_result = False
                    break

                symbols_map: dict[str, tuple[str, str, str]]
                current_symbol: str = content_tape[self._tape_position].replace(' ', '_')

                if self._check_state() and self._check_symbol(current_symbol):
                    symbols_map = self._turing_rules[self._current_state]
                elif self._check_state('*') and self._check_symbol(current_symbol, '*'):
                    symbols_map = self._turing_rules['*']
                elif self._check_state() and self._check_symbol('*'):
                    symbols_map = self._turing_rules[self._current_state]
                elif self._check_state('*') and self._check_symbol('*', '*'):
                    symbols_map = self._turing_rules['*']
                else:
                    is_valid_result = False
                    break

                if not (current_symbol in symbols_map or '*' in symbols_map):
                    is_valid_result = False
                    break

                transformation: tuple[str, str, str] = symbols_map.get(current_symbol) or\
                                                       symbols_map['*']
                content_tape[self._tape_position] = TurMach._convert_symbol(current_symbol,
                                                                         transformation[0])

                if (new_pos := TurMach._direction_map.get(transformation[1])) is None:
                    is_valid_result = False
                    break

                if new_pos == (-1) and self._tape_position == 0:
                    content_tape.insert(0, ' ')
                elif new_pos == 1 and self._tape_position == len(content_tape) - 1:
                    content_tape.append(' ')
                    self._tape_position += 1
                else:
                    self._tape_position += new_pos

                if transformation[2].startswith('halt'):
                    break

                self._current_state = transformation[2]

            final_message: str = f"{data_line[0]},{data_line[1]},"
            if is_valid_result:
                final_message += f"{''.join(content_tape).strip()}"
            else:
                final_message += "ERR"

            print(final_message)

        self._restore_initial_state()

        return


if __name__ == '__main__':
    machine: TurMach = TurMach()
    machine.process_datafile(os.path.join(os.path.dirname(__file__), "datafile"))
