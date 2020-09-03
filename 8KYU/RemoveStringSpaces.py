def no_space(x):
    new_string = ''
    for chars in x:
        if chars != ' ':
            new_string += chars
    return new_string
