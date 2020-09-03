def balance(left, right):
    left_list = []
    right_list = []
    count = 0
    for char in left:
        if char == '?':
            left_list.append(3)
        if char == '!':
            left_list.append(2)
    #return sum(left_list) 
    for char in right:
        if char =='?':
            right_list.append(3)
        if char == '!':
            right_list.append(2)
    #return sum(right_list)
    if sum(left_list) > sum(right_list):
        return "Left"
    if sum(right_list) > sum(left_list):
        return "Right"
    if sum(left_list) == sum(right_list):
        return "Balance"
