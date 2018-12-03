"""
    Handler
    ~~~~~~~~~~~~~~~
    Covert the string to a mapped one and write it to a new file
    :copyright: (c) 2018 by Andy.
"""
import os
import numpy

__all__ = ['convert_char']
MAPPINGS = {'A': 0, 'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'H': 6,
            'I': 7, 'K': 8, 'L': 9, 'M': 10, 'N': 11, 'P': 12, 'Q': 13,
            'R': 14, 'S': 15, 'T': 16, 'V': 17, 'W': 18, 'Y': 19,
            'X': 20, 'O': 20, 'U': 20, 'B': 21, 'Z': 21, 'J': 21}
MAPPINGS_S = {k: str(v) for k, v in MAPPINGS.items()}


def mapper(s):
    return ','.join(map(lambda c: MAPPINGS_S.get(c, ''), s))


def reader(fp):
    while True:
        content = fp.readline()
        if content:
            yield content.strip()
        else:
            break


def is_avail_path(p):
    if not os.path.exists(p) or os.path.exists(p) and os.path.getsize(p) == 0:
        return True
    return False


def convert_char(s_path, t_path):
    """
    covert the character from string to a mapped one and write to a new file
    :param s_path: source path
    :param t_path: target path
    :return:
    """
    if not is_avail_path(t_path):
        raise OSError('[Warning] the target path is invalid, please select another one')
    with open(s_path, mode='r') as f1, open(t_path, mode='a') as f2:
        for num, line in enumerate(reader(f1)):
            f2.write(mapper(line) + '\n')
            if num % 100 == 0 and num // 100 > 0:
                print('[Info] %d hundred lines have been written' % (num // 100))


def spawn_matrix(fp):
    """
    spawn matrix from a file
    :param fp: file descriptor
    :return: a matrix with shape(300, ?)
    """
    sentinel = 0
    arr = []
    while True:
        line = fp.readline()
        if not line:
            yield numpy.asarray(arr)
            break
        arr.append([int(n) for n in line.split(',')])
        sentinel += 1
        if sentinel == 300:
            yield numpy.asarray(arr)
            arr.clear()
            sentinel = 0


if __name__ == '__main__':
    # convert_char('1_7.txt', 'test.txt')
    with open('test.txt') as f:
        gen = spawn_matrix(f)
        print(next(gen))
        print(next(gen))
    # print(list(map(lambda l: l.split(','), islice(reader(f), 0, 2))))

