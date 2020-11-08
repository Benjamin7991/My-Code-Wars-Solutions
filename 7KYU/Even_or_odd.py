def even_or_odd(s):
    even_count = 0
    odd_count = 0
    
    for num in s:
        if int(num) % 2 == 0:
            even_count += int(num)
        else:
            odd_count += int(num)
            
    if even_count > odd_count:
        return 'Even is greater than Odd'
    elif odd_count > even_count:
        return 'Odd is greater than Even'
    return 'Even and Odd are the same'
