def coin_combo(cents):
    pennies = 0
    nickels = 0
    dimes = 0
    quarters = 0
    
    
    while cents - 25 >= 0:
        cents = cents - 25
        quarters += 1
        
    while cents - 10 >= 0:
        cents = cents - 10
        dimes += 1
        
    while cents - 5 >= 0:
        cents = cents - 5
        nickels += 1
        
    while cents - 1 >= 0:
        cents = cents -1
        pennies += 1
        
    return [pennies, nickels, dimes, quarters]
