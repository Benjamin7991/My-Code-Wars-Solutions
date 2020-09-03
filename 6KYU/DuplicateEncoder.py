def duplicate_encode(word):
    word = word.lower()
    lst_word = list(word)
    return "".join(")" if list(word).count(letter) > 1 else "(" for letter in lst_word)
