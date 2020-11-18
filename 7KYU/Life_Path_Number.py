def life_path_number(birthdate):
    birthdate = birthdate.split('-')
    
    year = sum([int(char) for char in birthdate[0]])
    month = sum([int(char) for char in birthdate[1]])
    day = sum([int(char) for char in birthdate[2]])
    
    while year > 10:
        year = sum(map(int, str(year)))
    while year > 10:
        month = sum(map(int, str(month)))
    while year > 10:
        day = sum(map(int, str(day)))
        
    summed =  year + month + day
    
    while summed >= 10:
        summed= sum(map(int, str(summed)))
        
    return summed 
