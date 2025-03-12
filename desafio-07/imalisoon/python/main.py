import sys

def python_tac(file_path):
    with open(file_path, 'rb') as file:
        file.seek(0, 2)
        file_size = file.tell()

        block_size = 400000
        position = file_size - block_size

        while position >= 0:
            file.seek(position, 0)
            data = file.read(block_size)

            lines = data.splitlines()

            remainder_line = len(lines[0])
            lines = lines[1:]

            reversed_lines = reversed(lines)
            for line in reversed_lines:
                print(line.decode('utf8'))

            position -= block_size - remainder_line

        position2 = position + block_size
        file.seek(0)
        data = file.read(position2)

        lines = data.splitlines()

        reversed_lines = reversed(lines)
        for line in reversed_lines:
            print(line.decode('utf8'))


def main():
    _file = sys.argv

    if len(_file) == 2:
        python_tac(_file)

    elif len(_file) <= 1:
        print("[USO] python main arquivo.txt")

    else:
        print("[ERRO] passe apenas 1 argumento.")


if __name__ == "__main__":
    main()
