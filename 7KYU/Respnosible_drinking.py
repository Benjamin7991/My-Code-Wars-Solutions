def hydrate(drink_string): 
    result= sum([int(x) for x in drink_string if x.isnumeric()])
    
    if result == 1:
        return str(result) + ' glass of water'
    else:
        return str(result) + ' glasses of water'
