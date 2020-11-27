def modified_sum(a, n):
    summed = sum([x**n for x in a])
    
    return summed - sum(a)
