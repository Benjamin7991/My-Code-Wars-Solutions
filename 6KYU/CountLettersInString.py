def letter_count(s):
    s.lower()
    new_dict = {}
    for letter in s:
        keys = new_dict.keys()
        if letter in keys:
            new_dict[letter] += 1
        else:
            new_dict[letter] = 1
    return new_dict
