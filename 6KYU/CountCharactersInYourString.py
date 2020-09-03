def count(string):
    new_list = {}
    for i in str(string):
        if i in new_list:
            new_list[i] += 1
        else:
            new_list[i] = 1
    return new_list
