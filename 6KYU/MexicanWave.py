def wave(people):
    list = []
    for i in range(len(people)):
        if people[i] != " ": 
            list.append(people[:i] + people[i].upper() + people[i+1:])
    return list
