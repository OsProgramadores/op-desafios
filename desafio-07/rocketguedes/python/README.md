# tac (clone written in Python)

Concatenate and print files in reverse.

## Features

* Can handle multiple files like original tac

## Use

```bash
python tac.py [FILE]...
```

Note: Make sure the file can be executed: `chmod +x tac.py`

```bash
./tac.py [FILE]...
```

## How it works

When opening the file, it starts reading 4KB at a time from the end of the file, saves the 4K in a variable called `buffer` and separates the lines found in the `buffer`, keeping the `\n`. This list of bytes is stored in the variable `lines`. After separating the lines, it may happen that the bytes in the first position of the list contain only a part of the text of the line present in the original file and not the entire line. With this in mind, we remove the bytes from the first position of the list `lines` and add them to a separate variable called `leftover` to later be appended to the end of the buffer in the next 4KB read.

In each loop, the list of bytes is written to the standard output line by line.

It may be that when reaching the end of the file there are no 4KB left to be read, so we always check at the beginning of the loop if the `position` (remaining bytes) is less than 4KB. If it is, we will read only the amount present in position and no longer 4KB.
