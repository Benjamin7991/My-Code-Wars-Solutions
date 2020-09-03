def simple_transposition(text):
    str1 = text[::2]
    result = ''
    for i in range(len(text)):
        if i % 2 != 0:
            result += text[i]
    return str1 + result
