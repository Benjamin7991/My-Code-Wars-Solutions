def solve(a,b):
    both = [x for x in a if x in b]
    return ''.join([x for x in a+b if x not in both])
