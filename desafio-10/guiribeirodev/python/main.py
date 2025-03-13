import sys

class TuringMachine:
    def __init__(self):
        self._rules = None
        self._tape = None
        self._tape_position = 0
        self._current_state = "0"
        self._result = None


    def _prepare_tape(self, input_string):
        self._tape = list(input_string.replace(" ", "_"))


    def _read_rules(self, rules_file):
        rules = []
        with open(rules_file, "r") as file:
            lines = file.read().splitlines()

        for rule in lines:
            rule = rule.split(";")[0].strip()
            rule_parts = rule.split(" ")
            if rule_parts and len(rule_parts) == 5:
                rules.append({
                    "current_state": rule_parts[0],
                    "current_symbol": rule_parts[1],
                    "new_symbol": rule_parts[2],
                    "direction": rule_parts[3],
                    "new_state": rule_parts[4],
                })

        self._rules = rules


    def _match_rule(self, state, symbol):
        for rule in self._rules:
            if rule["current_state"] == state and rule["current_symbol"] == symbol:
                return rule

        for rule in self._rules:
            if (rule["current_state"] == state or rule["current_state"] == "*") and (
                rule["current_symbol"] == symbol or rule["current_symbol"] == "*"
            ):
                return rule

        return None


    def _next_direction(self, direction):
        if direction == "r":
            self._tape_position += 1
            if self._tape_position >= len(self._tape):
                self._tape.append("_")

        elif direction == "l":
            self._tape_position -= 1
            if self._tape_position < 0:
                self._tape.insert(0, "_")
                self._tape_position = 0


    def result(self):
        return self._result


    def run(self, rules_file, input_string):
        self._read_rules(rules_file)
        self._prepare_tape(input_string)

        while True:
            current_symbol = self._tape[self._tape_position]
            current_rule = self._match_rule(self._current_state, current_symbol)

            if current_rule is None:
                self._result = "ERR"
                return self

            if current_rule["new_symbol"] != "*":
                self._tape[self._tape_position] = current_rule["new_symbol"]

            if "halt" in current_rule["new_state"]:
                self._result = "".join(self._tape).replace("_", " ").strip()
                return self

            self._next_direction(current_rule["direction"])
            self._current_state = current_rule["new_state"]


def main(datafile):
    with open(datafile, "r") as file:
        programs = file.read().splitlines()

    for line in programs:
        rules, input_data = line.split(",")

        machine = TuringMachine().run(rules, input_data)
        result = machine.result()

        print(f"{line},{result}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: python main.py datafile")
        sys.exit(1)

    datafile_path = sys.argv[1]
    main(datafile_path)
