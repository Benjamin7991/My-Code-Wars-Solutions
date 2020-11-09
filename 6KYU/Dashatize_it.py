import re

def dashatize(num):
    num = ''.join([x for x in str(num) if x.isnumeric()])
    li = []
    pattern = r'--'
    
    test = list(''.join([('-'+str(x)+'-') if int(x) % 2 != 0 and num is not None else x for x in num]))

    if len(test) >= 1:
        if test[-1] == '-':
            test.pop()
        if test[0] == '-':
            test.pop(0)
    answer = ''.join(test)
    if answer == '' or num is None:
        return 'None'
    
    return re.sub(pattern, '-', answer)
