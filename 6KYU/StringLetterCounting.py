import collections

def string_letter_count(s):
    dict = {}
    new_str = ''
    for char in s:
        if char.isalpha():
            char = char.lower()
            new_str += char

    for char in new_str:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    od = collections.OrderedDict(sorted(dict.items()))
    res = ''.join(list((str(v) + k) for k,v in od.items()))
    return res
