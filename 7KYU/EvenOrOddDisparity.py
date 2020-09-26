def solve(a):
    
    numbers = []
    even_count = 0
    odd_count = 0
    
    for item in a:
        if type(item) == int:
            numbers.append(item)
            
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    return even_count - odd_count
