def iq_test(numbers):
    no_odds = 0
    no_evens = 0
    numbers = numbers.split()
    for i in range(0, len(numbers)):
        if (int(numbers[i]) % 2) == 0:
            no_evens += 1
        else:
            no_odds += 1
    if no_odds > no_evens:
        for i in range(0, len(numbers)):
            if (int(numbers[i]) % 2 == 0):
                position = i + 1
    else:
        for i in range(0, len(numbers)):
            if (int(numbers[i]) % 2 != 0):
                position = i + 1
    return position
