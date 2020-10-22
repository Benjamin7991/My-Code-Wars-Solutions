def find_short(s):
    x = sorted([len(x) for x in s.split()])
    return x[0]
