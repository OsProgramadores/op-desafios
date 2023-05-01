'unix_tac with python by @hoklifter'
from file_read_backwards import FileReadBackwards as reverse_read

with reverse_read('1GB', encoding='utf-8') as source_file:
    for source_line in source_file:
        print(source_line)
