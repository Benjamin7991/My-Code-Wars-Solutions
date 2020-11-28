import itertools
def solve(arr):
    res = sorted(list(itertools.product(*arr)))
    li = []
    test = len(set([x for x in res if x not in li]))
    return test
