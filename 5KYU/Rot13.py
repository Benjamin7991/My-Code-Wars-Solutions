def rot13(message):
    string1 = 'abcdefghijklmnopqrstuvwxyz'
    string2 ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    list1 = []
    
    for char in message:
        if char in string1: 
            old_index = string1.find(char)
            new_index = (old_index + 13) % 26
            new_char = string1[new_index]
            list1.append(new_char)
        if char in string2:
            old_index = string2.find(char)
            new_index = (old_index + 13) % 26
            new_char = string2[new_index]
            list1.append(new_char)
        if char not in string1 and char not in string2:
            list1.append(char)
    
    return ''.join(list1)
