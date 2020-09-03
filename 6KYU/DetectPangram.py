def is_pangram(s):
    new_dict = {}
    s = s.lower()
    new_list = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letters in alphabet:
        if letters in s:
            if letters not in new_dict:
                new_dict[letters] = 1
            else:
                new_dict[letters] + 1
        else:
            new_dict[letters] = 0
                
    for value in new_dict.values():
        new_list.append(value)
    if 0 in new_list:
        return False
    return True
