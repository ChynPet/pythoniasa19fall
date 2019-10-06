"""
Assignment 2-B
==============

Wrap Assignment 1-B in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-ru.txt').read_text()
True
"""

def poem():
    start = ['Вот дом, который построил Джек.','А это пшеница,', 'А это весёлая птица-синица,','Вот кот,','Вот пёс без хвоста,','А это корова безрогая,','А это старушка, седая и строгая,','А это ленивый и толстый пастух,','Вот два петуха,']
    attribute = ['В доме, который построил Джек.','Которая в тёмном чулане хранится', 'Которая часто ворует пшеницу,', 'Который пугает и ловит синицу,', 'Который за шиворот треплет кота,','Лягнувшая старого пса без хвоста,', 'Лягнувшую старого пса без хвоста,','Которая доит корову безрогую,', 'Который бранится с коровницей строгою,','Которые будят того пастуха,']

    txt = f'{start[0]}\n'

    for i in range(1,len(start)):
        txt += f'\n{start[i]}\n'
        j = i
        while j >=  0:
            if i >= 6:
                if j < 5:
                    txt += f'{attribute[j]}\n'
                elif j >= 5:
                    txt += f'{attribute[j+1]}\n'
            else:
                txt += f'{attribute[j]}\n'
            j -= 1
    return txt


if __name__ == '__main__':
    import doctest
    doctest.testmod()
