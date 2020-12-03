import math
def sum_square_even_root_odd(nums):
    return round(sum([x**2 if x %2 ==0 else math.sqrt(x) for x in nums]),2)
