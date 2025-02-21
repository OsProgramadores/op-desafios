import sys


class TuringMachine:
    def __init__(self, rules, input_string):
        self.rules = rules
        self.tape = list(input_string)
        self.current_state = "0"
        self.tape_position = 0
        self.current_rule = None

    def match_rule(self, state, symbol):
        for rule in self.rules:
            if rule["current_state"] == state and rule["current_symbol"] == symbol:
                self.current_rule = rule
                return rule

        for rule in self.rules:
            if (rule["current_state"] == state or rule["current_state"] == "*") and (
                rule["current_symbol"] == symbol or rule["current_symbol"] == "*"
            ):
                self.current_rule = rule
                return rule

        self.current_rule = None
        return None

    def next_direction(self, direction):
        if direction == "r":
            self.tape_position += 1

            if self.tape_position >= len(self.tape):
                self.tape.append("_")

        elif direction == "l":
            self.tape_position -= 1

            if self.tape_position < 0:
                self.tape.insert(0, "_")
                self.tape_position = 0

    def run(self):
        while True:
            current_symbol = self.tape[self.tape_position]
            self.match_rule(self.current_state, current_symbol)

            if self.current_rule is None:
                return "ERR"

            if self.current_rule["new_symbol"] != "*":
                self.tape[self.tape_position] = self.current_rule["new_symbol"]

            if "halt" in self.current_rule["new_state"]:
                result = "".join(self.tape).replace("_", " ").strip()
                return result

            self.next_direction(self.current_rule["direction"])
            self.current_state = self.current_rule["new_state"]


def read_rules(rules_file):
    rules = []
    with open(rules_file, "r") as file:
        lines = file.read().splitlines()

    for rule in lines:
        rule = rule.split(";")[0].strip()
        rule_parts = rule.split(" ")

        if rule_parts and len(rule_parts) == 5:
            rules.append(
                {
                    "current_state": rule_parts[0],
                    "current_symbol": rule_parts[1],
                    "new_symbol": rule_parts[2],
                    "direction": rule_parts[3],
                    "new_state": rule_parts[4],
                }
            )

    return rules


def main(datafile):
    with open(datafile, "r") as file:
        programs = file.read().splitlines()

        for line in programs:
            [rules, input_data] = line.split(",")

            input_data = input_data.replace(" ", "_")
            rules = read_rules(rules)
            machine = TuringMachine(rules, input_data)
            result = machine.run()

            print(f"{line},{result}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: python main.py datafile")
        sys.exit(1)

    datafile_path = sys.argv[1]
    main(datafile_path)
