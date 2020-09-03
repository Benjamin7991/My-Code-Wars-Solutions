def solution(s):
    final_string = ""
    for char in s:
        if char.isupper() == True:
            final_string += ' ' + char
        else:
            final_string += char
    return final_string
