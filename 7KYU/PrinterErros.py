def printer_error(s):
    range = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    errors = int()
    denominator = len(s)
    for letters in s:
        if letters not in range:
            errors += 1
        else:
            pass
    return str(errors) + "/" + str(denominator)
