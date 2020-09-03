def find_outlier(integers):
    even_count = 0
    odd_count = 0
    for number in integers:
        if number % 2 != 0:
            odd_count += 1
        if number % 2 == 0:
            even_count += 1
        
    if odd_count > even_count:
        for number in integers:
            if number % 2 == 0:
                return number
    if odd_count < even_count:
        for number in integers:
            if number % 2 != 0:
                return number
