def valid_ISBN10(isbn): 
    obj = [int(x) if x.isnumeric() else 10 for x in isbn]
    test = (sum([x[0]*x[1] for x in list(zip(obj,range(1,len(isbn)+1)))]))
    
    
    if len(isbn) != 10:
        return False
    for char in isbn[0:len(isbn)-1]:
        if char == 'X' or char.isalpha():
            return False
    else:
        return test % 11 == 0
