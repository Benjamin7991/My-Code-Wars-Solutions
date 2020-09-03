def square_digits(num):
    num = str(num)
    new_string = ''
    for x in num:
        squared = int(x)**2
        new_string += str(squared)
    return int(new_string)
