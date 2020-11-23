def row_weights(array):
    team1 = []
    team2 = []
    
    for i in range(len(array)):
        if i % 2 != 0:
            team2.append(array[i])
        else:
            team1.append(array[i])
            
    return sum(team1), sum(team2)
