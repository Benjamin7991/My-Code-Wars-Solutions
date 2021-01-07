def variance(numbers): 
    avg = sum(numbers) / len(numbers)
    new_l = []
    
    for x in numbers:
        new_x = (x-avg)**2
        new_l.append(new_x)
    
    return (sum(new_l) / len(numbers))
