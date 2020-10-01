def to_weird_case(string):
    result = []
    string = string.split(' ')
    for word in string:
        new_word = ''
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            if i % 2 != 0:
                new_word += word[i].lower()
        result.append(new_word)
    return ' '.join(result)
