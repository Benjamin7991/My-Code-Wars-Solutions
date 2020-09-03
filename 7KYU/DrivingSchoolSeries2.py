import math

def cost(mins):
    charge = 0
    mins_left = mins - 65
    if mins <= 65:
        return 30
    if mins_left <= 35:
        return 30 + 10
    
    else:
        charge = mins_left / 30
        charge = math.ceil(charge)
        charge = charge*10
        return charge + 30
