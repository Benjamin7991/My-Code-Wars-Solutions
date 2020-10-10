def sort_array(source_array):
    odds = sorted([x for x  in source_array if x % 2 != 0 or x ==1])
    
    for i in range(len(source_array)):
        if source_array[i] not in odds:
            odds.insert(i, source_array[i])
    return odds
