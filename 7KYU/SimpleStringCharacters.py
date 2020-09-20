def solve(s):
    upper_count = 0
    lower_count = 0
    num_count = 0
    spec_count = 0
    for char in s:
        
        if char.isupper():
            upper_count += 1

        if char.islower():
            lower_count += 1
            
        if char.isnumeric():
            num_count += 1
        
        if not char.isalpha() and not char.isnumeric():
            spec_count += 1
    return [upper_count, lower_count, num_count, spec_count]
