def find_it(seq):
    for letters in seq:
        if (seq.count(letters)) % 2 != 0:
            return letters
