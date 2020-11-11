def max_gap(numbers):
    numbers = sorted(numbers)
    result = tuple(i - j for i, j in zip(numbers, numbers[1:]))
    return max([abs(x) for x in result])
