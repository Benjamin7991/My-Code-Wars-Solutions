def count_deaf_rats(town):
    town = town.split('P')
    left = town[0]
    right = town[1]
    
    for char in right:
        if char == ' ':
            right = right.replace(char, '')
            
    for char in left:
        if char == ' ':
            left = left.replace(char, '')
            
    n = 2
    left = [left[i:i+2] for i in range(0,len(left), n)]
    right = [right[i:i+2] for i in range(0, len(right), n)]
    
    left_count = left.count('O~')
    right_count = right.count('~O')
    
    return left_count + right_count
