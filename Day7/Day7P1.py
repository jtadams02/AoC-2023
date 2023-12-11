from collections import defaultdict
infile = open("inputTest.txt",'r')
card_vals = {
    'A' : 14,
    'Q' : 12,
    'K' : 13,
    'J' : 11,
    'T' : 10
}

def determine_hand(hand):
    print(hand)
    # So I am just going to use flags to determine what kind of pairs
    rank = 0
    # We need a high card value
    high_val = 0
    card_map = defaultdict(lambda: 0) # Creates a default dict of all values 0
    curr_set = []
    i = 0
    while i < len(hand)+1:
        if curr_set:
            if i < len(hand) and curr_set[-1] == hand[i]:
                # Append and keep going
                curr_set.append(hand[i])
            else:
                print(curr_set)
                # If they are not equal we need to do calculate what hand we have
                high_val = max(card_map[curr_set[-1]],high_val) # Get the high val JIC
                if len(curr_set) == 2:
                    if rank == 3:
                        # We have a full house
                        rank = 4
                    elif rank == 1:
                        rank = 2 # Otherwise we have a 2 pair
                    else:
                        rank = 1
                elif len(curr_set) == 3:
                    if rank == 1:
                        # We have a full house
                        rank = 4
                    else:
                        rank = 3
                elif len(curr_set) == 4:
                    rank = 5
                elif len(curr_set) == 5:
                    rank = 6
                # But now we need to reset curr set and add
                if i < len(hand):
                    curr_set = [hand[i]]
        else:
            curr_set.append(hand[i])
        i += 1
    # Now we should have all our vals I guess?
    return rank
hands = {
    0 : [], # High card
    1 : [], # One Pair
    2 : [], # Two pair
    3 : [], # Three of a kind
    4 : [], # Full house (3 pair and 2 pair)
    5 : [], # 4 of a kind
    6 : [] # 5 of a kind
}

n = infile.readline().rstrip('\n')

while n:
    hand = n.split(' ')
    
    sorted_hand = ''.join(sorted(hand[0]))
    new_hand = []
    for char in hand[0]:
        if not char.isnumeric():
            # Use the map
            char = card_vals[char]
        new_hand.append(int(char))
    hand[0] = new_hand
    hands[determine_hand(sorted_hand)].append(hand)
    
    n = infile.readline().rstrip('\n')
count = 0
for key in hands:
    count += len(hands[key])
    hands[key] = sorted(hands[key],reverse=True)
winnings = 0
for i in range(6,-1,-1):
    for hand in hands[i]:
        winnings += (int(hand[1])*count)
        count -= 1
print(winnings)
    