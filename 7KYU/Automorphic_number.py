def automorphic(n):
    squared = n**2
    if str(n) in str(squared):
        return 'Automorphic'
    return 'Not!!'
