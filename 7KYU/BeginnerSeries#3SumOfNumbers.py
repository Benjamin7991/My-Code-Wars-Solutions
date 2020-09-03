def get_sum(a,b):
    if a > b:
        return sum(range(b, a + 1))
    if a < b:
        return sum(range(a, b +1))
    if a == b:
        return a
