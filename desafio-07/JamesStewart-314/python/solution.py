import os
from typing import Final, Generator

MEGABYTE_IN_BYTES: Final[int] = 1_048_576
CHUNK_SIZE: int = 100
CHUNK_SIZE_IN_BYTES: int = CHUNK_SIZE * MEGABYTE_IN_BYTES


def process_buffer(bin_string_buffer: str) -> Generator[str | bool, None, str]:
    bin_string_buffer_list: list[str] = bin_string_buffer.split(b"\n")
    while len(bin_string_buffer_list) > 1:
        yield bin_string_buffer_list.pop()

    # Throws false to signal the sending of the remaining buffer contents.
    yield False
    yield bin_string_buffer_list[0]


def tac_python(file_path: str) -> None:
    try:
        with open(file_path, "rb") as bin_file:
            bin_file.seek(0, 2)
            bin_file.seek(bin_file.tell() - 1)
            file_cursor_position: int = bin_file.tell()
            string_buffer: str = b""

            while file_cursor_position != 0:
                old_file_cursor_position: int = bin_file.tell()
                file_cursor_position = max(0, file_cursor_position - CHUNK_SIZE)

                bin_file.seek(file_cursor_position)
                string_buffer = bin_file.read(old_file_cursor_position - file_cursor_position)\
                      + string_buffer
                bin_file.seek(file_cursor_position)

                for word in (str_gen := process_buffer(string_buffer)):
                    if word is not False:
                        print(word.decode("utf-8"))
                        continue
                    break
                string_buffer = next(str_gen)
            print(string_buffer.decode("utf-8"))

    except FileNotFoundError:
        print("Error: File path is invalid or doesn\'t exist.")


if __name__ == '__main__':
    tac_python(os.path.join(os.path.dirname(__file__), "1GB.txt"))
