def fly_by(lamps, drone):
    list = []
    i = len(drone) 
    first_part = lamps[:i]
    last_part = lamps[i:]
    for items in first_part:
        if items == 'x':
            first_part= first_part.replace(items, 'o')
    return first_part + last_part
