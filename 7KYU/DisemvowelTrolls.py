def disemvowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_string = ""
    for chars in str(string):
        if chars not in vowels:
            new_string += chars
    return new_string
