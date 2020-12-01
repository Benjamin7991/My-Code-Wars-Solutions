def number(bus_stops):
    on = [x[0] for x in bus_stops]
    off = [x[1] for x in bus_stops]
    
    return sum(on)-sum(off)
