"""
Assignment 1-A
==============

Update the Python script below to make it more compact and readable; use at least variables and f-strings.
For those who are already familiar with Python – write the best code you can to conform to the Zen of Python.

"""

text = '''
That kept the cock that crow'd in the morn, 
That waked the priest all shaven and shorn,
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That killed the rat, 
That ate the malt 
That lay in the house that Jack built.
'''

poem = f'''
This is the house that Jack built.

This is the malt 
{text[302:]}

This is the rat, 
{text[283:]}

This is the cat, 
{text[261:]}

This is the dog, 
{text[238:]}

This is the cow with the crumpled horn, 
{text[216:]}

This is the maiden all forlorn,
{text[172:]}

This is the man all tatter'd and torn, 
{text[135:]}

This is the priest all shaven and shorn, 
{text[90:]}

This is the cock that crow'd in the morn, 
{text[46:]}

This is the farmer sowing his corn, 
{text[1:]}
'''

print(poem)