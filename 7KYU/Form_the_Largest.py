def max_number(n):
    new = sorted([str(x) for x in str(n)])[::-1]
    
    return int(''.join(new))
