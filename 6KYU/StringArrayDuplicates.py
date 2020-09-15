import re

def dup(arry):
    list = []
    for words in arry:
        list.append(re.sub(r'([a-z])\1+', r'\1', words))
    return list
