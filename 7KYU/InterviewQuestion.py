def get_strings(city):
    city = city.lower()
    dict = {}
    for i in city:
        if i == ' ':
            city = city.replace(i, '')
    for char in city:
        if char not in dict:
            dict[char] = '*'
        else:
            dict[char] += '*'
    return ','.join('{}:{}'.format(key, val) for key, val in dict.items())
