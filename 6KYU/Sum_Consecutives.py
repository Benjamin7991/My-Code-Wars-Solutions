from itertools import groupby

def sum_consecutives(s):
    return [sum(g) for _, g in groupby(s)]
