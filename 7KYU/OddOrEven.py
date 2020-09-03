def odd_or_even(arr):
    total_sum = sum(arr)
    if total_sum % 2 == 0:
        return "even"
    else:
        return "odd"
