def more_zeros(s):
    binary =  [format(ord(x), 'b') for x in s]

    result = []
    final_answer= []
    
    for number in binary:
        ones = number.count('1')
        zeros = number.count('0')
        ans = zeros - ones
        result.append(ans)    
    
    d = dict(zip(s, result))
    
    for k,v in d.items():
        if v > 0:
            final_answer.append(k)
    return final_answer
