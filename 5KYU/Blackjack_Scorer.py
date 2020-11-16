def score_hand(cards):
    hand = []
    
    for item in cards:
        if item.isnumeric():
            hand.append(int(item))
        if item == 'J' or item == 'Q' or item == 'K':
            hand.append(10)
        if item == 'A':
            hand.append(11)
    
    while sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)
