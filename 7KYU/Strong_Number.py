def strong_num(number):
    digits = [x for x in str(number)]
    l = []
    
    factorial = 1
    
    for digit in digits:
        factorial = 1
        #if int(n) >= 1:
        for i in range (1,int(digit)+1):
            factorial = factorial * i
        l.append(factorial)
        
    if sum(l) == number:
        return 'STRONG!!!!'
    else:
        return 'Not Strong !!'
