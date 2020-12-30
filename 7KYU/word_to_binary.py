def word_to_bin(word):
     return [format(ord(x), 'b').zfill(8) for x in word]
