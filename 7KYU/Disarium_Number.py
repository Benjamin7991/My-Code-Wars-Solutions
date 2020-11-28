def disarium_number(number):
    nums = [int(digit) for digit in str(number)]
    ref = enumerate(nums, 1)
    test =  [item[1]**item[0] for item in ref]
        
    if sum(test) == number:
        return 'Disarium !!'
    return 'Not !!'
