"""
Assignment 2-B
==============

Wrap Assignment 1-B in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-ru.txt').read_text()
True
"""

def poem():
    return ''


if __name__ == '__main__':
    import doctest
    doctest.testmod()
