import collections

def solve(arr):
    f = collections.Counter(arr)
    arr.sort(key = lambda x:(-f[x], x))
    return arr
