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

    def _convert_symbol(self, old_symbol: str, new_symbol: str) -> str:
        if new_symbol == '*':
            return old_symbol
        if new_symbol == '_':
            return ' '
        return new_symbol

    def _restore_initial_state(self) -> None:
        self._turing_rules.clear()
        self._tape_position = 0
        self._current_state = '0'

    def process_datafile(self, file_path: str) -> None:
        try:
            datafile_obj: TextIO = open(file_path, "r")
        except FileNotFoundError:
            print(f"Error: Could not open datafile \'{file_path}\'.")
            return

        for data_line in datafile_obj:
            self._restore_initial_state()
            data_line: list[str] = data_line.strip().split(',')
            turing_rules_file_path: str = os.path.join(os.path.dirname(file_path), data_line[0])

            try:
                turing_rules_file: TextIO = open(turing_rules_file_path, "r")
            except FileNotFoundError:
                print(f"Error: Could not open turing rules file \'{turing_rules_file_path}\'.")
                continue

            for rule_line in turing_rules_file:
                rule_line = rule_line.strip()
                if not rule_line or rule_line[0] == ';':
                    continue

                try:
                    rule_line = rule_line[:rule_line.index(';')].strip()
                except ValueError:
                    pass

                rule_line_splitted: list[str] = rule_line.split()
                sym_dir_stt = (rule_line_splitted[2], rule_line_splitted[3], rule_line_splitted[4])

                self._turing_rules.setdefault(rule_line_splitted[0], {}).\
                                   setdefault(rule_line_splitted[1], sym_dir_stt)

            turing_rules_file.close()

            content_tape: list[str] = list(data_line[1])
            valid_result: bool = True
            while True:
                if not (self._current_state in self._turing_rules or\
                        '*' in self._turing_rules):
                    print(f"{data_line[0]},{data_line[1]},ERR")
                    valid_result = False
                    break

                symbols_map: dict[str, tuple[str, str, str]]
                current_symbol: str = content_tape[self._tape_position] if\
                                      content_tape[self._tape_position] != ' ' else '_'

                if self._current_state in self._turing_rules and current_symbol in\
                   self._turing_rules[self._current_state]:
                    symbols_map = self._turing_rules[self._current_state]
                elif '*' in self._turing_rules and current_symbol in self._turing_rules['*']:
                    symbols_map = self._turing_rules['*']
                elif self._current_state in self._turing_rules and\
                     '*' in self._turing_rules[self._current_state]:
                    symbols_map = self._turing_rules[self._current_state]
                elif '*' in self._turing_rules and '*' in self._turing_rules['*']:
                    symbols_map = self._turing_rules['*']
                else:
                    print(f"{data_line[0]},{data_line[1]},ERR")
                    valid_result = False
                    break

                if not (current_symbol in symbols_map or '*' in symbols_map):
                    print(f"{data_line[0]},{data_line[1]},ERR")
                    valid_result = False
                    break

                transformation: tuple[str, str, str] = symbols_map.get(current_symbol) or\
                                                       symbols_map['*']
                content_tape[self._tape_position] = self._convert_symbol(current_symbol,
                                                                         transformation[0])

                if (new_pos := TurMach._direction_map.get(transformation[1])) is None:
                    print(f"{data_line[0]},{data_line[1]},ERR")
                    valid_result = False
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
            if valid_result:
                print(f"{data_line[0]},{data_line[1]},{''.join(content_tape).strip()}")

        datafile_obj.close()
        self._restore_initial_state()

        return


if __name__ == '__main__':
    machine: TurMach = TurMach()
    machine.process_datafile(os.path.join(os.path.dirname(__file__), "datafile"))
