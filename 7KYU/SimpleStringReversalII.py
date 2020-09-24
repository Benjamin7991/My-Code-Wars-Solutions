def solve(st,a,b):
    reverse = st[a:b+1]
    return st[:a] + reverse[::-1] + st[b+1:]
