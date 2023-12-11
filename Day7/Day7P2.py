from collections import defaultdict
infile = open("input.txt",'r')
card_vals = {
    'A' : 14,
    'Q' : 12,
    'K' : 13,
    'J' : 1,
    'T' : 10
}
def determine_hand(hand,j_count):
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
                l = len(curr_set) + j_count
                if l == 2:
                    if rank == 3:
                        # We have a full house
                        rank = max(rank,4)
                    elif rank == 1:
                        rank = max(rank,2) # Otherwise we have a 2 pair
                    else:
                        rank = max(rank,1)
                elif l == 3:
                    if rank == 1:
                        # We have a full house
                        rank = max(rank,4)
                    else:
                        rank = max(rank,3)
                elif l == 4:
                    rank = max(rank,5)
                elif l == 5:
                    rank = max(rank,6)
                # But now we need to reset curr set and add
                if i < len(hand):
                    curr_set = [hand[i]]
        else:
            if i < len(hand):
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
    # So lets try removing all the jokers from the hand
    no_jokes = ''
    j_count = 0
    for char in sorted_hand:
        if char != 'J':
            no_jokes += char
        else:
            j_count += 1
    new_hand = []
    for char in hand[0]:
        if not char.isnumeric():
            # Use the map
            char = card_vals[char]
        new_hand.append(int(char))
    hand[0] = new_hand
    hands[determine_hand(no_jokes,j_count)].append(hand)
    
    n = infile.readline().rstrip('\n')
count = 0
print(hands)
for key in hands:
    count += len(hands[key])
    hands[key] = sorted(hands[key],reverse=True)
winnings = 0
for i in range(6,-1,-1):
    for hand in hands[i]:
        winnings += (int(hand[1])*count)
        count -= 1
print(winnings)
    