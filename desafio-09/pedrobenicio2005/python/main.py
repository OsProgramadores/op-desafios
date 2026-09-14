import sys

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

CHAR_TO_VALUE = {c: i for i, c in enumerate(ALPHABET)}


def parse_number(text, base):
    """Converte a string 'text' na base informada para um inteiro python.

    Retorna None se houver algum erro (digito invalido ou negativo).
    """
    if not text:
        return None

    value = 0
    for char in text:
        digit = CHAR_TO_VALUE.get(char)
        if digit is None or digit >= base:
            return None
        value = value * base + digit
    return value


def to_base(value, base):
    """Converte um inteiro python para string na base informada."""
    if value == 0:
        return "0"

    digits = []
    while value > 0:
        value, remainder = divmod(value, base)
        digits.append(ALPHABET[remainder])
    return "".join(reversed(digits))


def process_line(line):
    """Processa uma linha da entrada e devolve a strig de saida."""
    parts = line.split()
    if len(parts) != 3:
        return "???"

    base_in_str, base_out_str, number_str = parts

    try:
        base_in = int(base_in_str)
        base_out = int(base_out_str)
    except ValueError:
        return "???"

    if not (2 <= base_in <= 62) or not (2 <= base_out <= 62):
        return "???"

    if number_str.startswith("-"):
        return "???"

    value = parse_number(number_str, base_in)
    if value is None:
        return "???"

    max_value = parse_number("z" * 32, 62)
    if value > max_value:
        return "???"

    return to_base(value, base_out)


def main():
    """Le da entrada padrao e escreve na saida  padrao."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        print(process_line(line))


if __name__ == "__main__":
    main()
