def solve(a,b):
    l = []
    
    for item in b:
        if item in a:
            l.append(a.count(item))
        if item not in a:
            l.append(0)
    return l
