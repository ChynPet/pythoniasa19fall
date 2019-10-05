"""
Assignment 2-A
==============

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""
def poem():
    def punctuatuin(x): 
        if x==-2:
            return ""
        elif x==-1:
            return "."
        else:
            return ","

    verb = ['This is','That kept','That waked','That married','That kissed','That milked','That tossed','That worried','That killed','That ate','That lay']
    noun = ['the farmer', 'the cock', 'the priest', 'the man', 'the maiden', 'the cow', 'the dog', 'the cat', 'the rat', 'the malt', 'the house']
    attribute = ['sowing his corn','that crowed in the morn','all shaven and shorn','all tattered and torn','all forlorn','with the crumpled horn', 'that Jack built']

    #Creating sentences to start a verse 
    sentence_start = [f'{verb[0]} {noun[i]}{" " + attribute[i] if i < len(attribute)-1 else ""}' for i in range(len(noun))]
    sentence_start[-1] += ' ' + attribute[-1]
    #Creating verse sentences
    sentence = [f'{verb[i+1]}{" in " if i+1 == len(noun)-1 else " "}{noun[i+1]}{" " + attribute[i+1] if i+1 < len(attribute)-1 else ""}' for i in range(len(noun)-1)]
    sentence[-1] += ' ' + attribute[-1]

    i = -1
    txt = f'{sentence_start[-1]}.\n'
    #Creating poem
    while (i > -len(sentence_start)):
        txt += f'\n{sentence_start[i-1]}{"," if i != -1 else ""}\n'
        j = i
        while (j <= -1):
            txt += f'{sentence[j]}{punctuatuin(j)}\n'
            j += 1
        i -= 1
    return txt


if __name__ == '__main__':
    import doctest
    doctest.testmod()
