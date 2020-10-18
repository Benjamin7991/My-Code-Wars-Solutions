def high_and_low(numbers):
    nums = [int(x) for x in numbers.split(' ')]
    
    maxi = max(nums)
    mini = min(nums)
    answer = ''
    result = []
    result.append(str(maxi))
    result.append(str(mini))
    
    return ' '.join(result)
