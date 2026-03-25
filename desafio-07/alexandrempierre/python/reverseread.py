'''reverseread module

Reads the file from end to start.
'''


__all__ = ['reverse_readlines', 'reverse_readchars']
__author__ = 'Alexandre Pierre'


def reverse_readchars(fp):
    '''Read chars from end to start.'''
    position = fp.seek(0, 2)
    while position != 0:
        position = fp.seek(-1, 1)
        yield fp.read(1)
        fp.seek(-1, 1)

def reverse_readlines(fp):
    '''Read lines from last to first. The actual tac function.'''
    stream = reverse_readchars(fp)
    next(stream, b'')
    line = b''
    for c in stream:
        if c == b'\n':
            yield line[::-1]
            line = b''
        else:
            line += c
    yield line[::-1]
