def duplicate_count(text):
    text=text.lower()
    new_list =[]
    list_of_repeats = {}
    for i in text:
        if i in list_of_repeats:
            list_of_repeats[i] += 1
        else:
            list_of_repeats[i] = 1
    for key in list_of_repeats:
        if list_of_repeats.get(key) >= 2:
            new_list.append(key)
    return len(new_list)
