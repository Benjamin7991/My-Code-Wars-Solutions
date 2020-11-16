def meeting(s):
    s = s.upper().split(';')
    result = []
    answer = []
    test = ''
    dam = ''
    
    for item in s:
        new_item = tuple(item.split(':'))
        result.append(new_item)
        result = sorted(result)
    
    for item in result:
        x = item[1], item[0]
        answer.append(x)
        answer = sorted(answer)
    
    for tup in answer:
        test += str(tup)
    
    for char in test:
        if char != "'":
            dam += char
    return dam
